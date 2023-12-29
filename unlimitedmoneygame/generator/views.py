from django.shortcuts import render
from django.conf import settings
import rest_framework
# Create your views here.
import json
import stripe

import random
from django.http import Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token

from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import PlayerSerializer, UserSerializer,APIListSerializer, LuckCalc,KeyListSerializer, InvoiceSerializer, ChatSerializer, WinnerSerializer,PlayerListSerializer,FLSerializer,FLTWOSerializer,FLTHREESerializer,FLFOURSerializer,FLFIVESerializer,FLSIXSerializer,ModifierSerializer, TradeFalseSerializer,PlayerSearchSerializer,AcceptedTradeSerializer,TradeSpaceSerializer,InventorySerializer
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .models import Playing, black, Game, Ticket, APIKEY, Modifiers, Trade, Inventory,TradeSpace,Chat,User,Invoice,DeletedInvoice,KeySeed

from nowpayment import NowPayments
payments = NowPayments("0X69GM1-0YQMQM3-GH4TPKG-YP685FF")

from nowpay import NOWPayments

#lucifer = NOWPayments("0X69GM1-0YQMQM3-GH4TPKG-YP685FF")




#status = payment.create_payment(100,'USD','btc')
status = ""

#status = payments.payment.get_payment_status(4710396570)


thatid = 0







#payments.payment.create_invoice(
    #price_amount = 1,
    #price_currency = 'USD'
     
#)
@api_view(['POST'])

def get_USER(request):
    token = request.data.get('token')
    x = Token.objects.filter(key = token).first()
    username = (x.user)
    Users = str(username)

    print(token, username)
    return Response({'username': Users})


@api_view(['POST'])

def GETMYKEY(request):
    username = request.data['username']
    
    TheseKeys = User.objects.filter(username = username).first()
    APIKEYS = APIKEY.objects.get(KEY = "0X69GM1-0YQMQM3-GH4TPKG-YP685FF")
    serializer = APIListSerializer(APIKEYS)
    return Response(serializer.data)



    


@api_view(['POST'])
def invoice(request):
    username = request.data['username']
    payment_status = int(request.data['payment_id'])
    status = payments.payment.get_payment_status(request.data['payment_id'])
    print(status)
    try:
        LastInv = Invoice.objects.filter(username = username).first()
        if LastInv.payment_status == "waiting":
            DeletedInv = DeletedInvoice(username = LastInv.username, pay_amount = LastInv.pay_amount, amount_received = LastInv.amount_received, address = LastInv.address,payment_id = LastInv.payment_id, payment_status = 'failed', price_amount = LastInv.price_amount, p_timer = 0, p_qrcode = "")
            DeletedInvoice.save(DeletedInv)
        else:
            DeletedInv = DeletedInvoice(username = LastInv.username, pay_amount = LastInv.pay_amount, amount_received = LastInv.amount_received, address = LastInv.address,payment_id = LastInv.payment_id, payment_status = 'Completed', price_amount = LastInv.price_amount, p_timer = 0, p_qrcode = "")
            DeletedInvoice.save(DeletedInv)

    except:
        print("no invoice to delete")
    try:

        Invoice.objects.filter(username = username).delete()
    except:
        print()

    qrcode = "https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=" +request.data['address']
    
    NewInvoice = Invoice(username = username, pay_amount = status['pay_amount'], amount_received = status['actually_paid'], address = request.data['address'],payment_id = request.data['payment_id'], payment_status = request.data['payment_status'], price_amount = request.data['price_amount'], p_timer = 86400,p_qrcode = qrcode )
    Invoice.save(NewInvoice)
  
    #next respond with serializer data.



@api_view(['POST'])
def GETMYKEYS(request):
    username = request.data['username']
    try:
        TheseKeys = KeySeed.objects.filter(p_namer = username)

    except:
        print()

    serializer = KeyListSerializer(TheseKeys, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def GETMYINVOICE(request):
    username = request.data['username']
    ThisInv = Invoice.objects.filter(username = username).first()
    serializer = InvoiceSerializer(ThisInv)
    return Response(serializer.data)

@api_view(['GET'])
def get_stripe_pub_key(request):
    pub_key = settings.STRIPE_PUB_KEY

    return Response({'pub_key': pub_key})

@api_view(['POST'])
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body)
    keyamount =data['keyamount']
    usernames = data['username']
    
    print(keyamount, "goef09jefoiefniewonfiwfniowpmdwpodlwqpdniqdm")
    if keyamount >= 1:
        price_id = settings.STRIPE_PRICE_ID_KEY_SEED
    else:
        print('not enough')


    Users = User.objects.filter(username = usernames).first()

    try:
        checkout_session = stripe.checkout.Session.create(
            client_reference_id = Users.id,
            success_url = '%s?session_id={CHECKOUT_SESSION_ID}' % settings.FRONTEND_WEBSITE_SUCCESS_URL,
            cancel_url = '%s'%settings.FRONTEND_WEBSITE_CANCEL_URL, 
            payment_method_types = ['card'],
            mode = 'payment',
            line_items = [
                {
                    'price':price_id,
                    'quantity':keyamount 

                    
                }
            ]

            

        )
       
        
        return Response({'sessionId': checkout_session['id']})
    except Exception as e:
        return Response({'error':str(e)})
        #charge 0.029% #+0.3
    

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key =settings.STRIPE_SECRET_KEY
    webhook_key = settings.STRIPE_WEBHOOK_KEY
    payload = request.body

    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header,webhook_key
        )
    except ValueError as e:
        return HttpResponse(status=404)
    except stripe.error.SignatureVerficiationError as e:
        return HttpResponse(status=404)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        Player = User.objects.get(pk=session.get('client_reference_id'))
        Player.stripe_customer_id = session.get('customer')
        love = session['amount_total']
        love = love/100

        thisguy  = (love - love * 0.029)
        if love <= 100:
            thisguy = thisguy - 0.3
        User.save(Player)

        
        keygenone = random.randint(100000,999999)
        keygentwo = random.randint(100000,999999)
        keygenthree = random.randint(100000,999999)
        keygenfour= random.randint(100000,999999)
        KeyCode = ('{}-{}-{}-{}').format(keygenone,keygentwo,keygenthree,keygenfour)

        try:
                    KeySeed.objects.get(p_keyseed = KeyCode)
        except:


                    #thisinv.payamount convert to usd in btc with coinbase api, and then give them that amount. in p_amounted
                    NewKey = KeySeed(p_namer = Player.username, p_keyseed = KeyCode, p_amounted = thisguy, p_timer = 1210000, p_activated = False)
                    KeySeed.save(NewKey)

        
        print(session, thisguy, love)


    return HttpResponse(status=200)

@api_view(['POST'])
def Keygen(request):
    
    Made = request.data.get('pname')
    
    
    Player = Playing.objects.get(p_name = Made)
    Luckview = LuckCalc.objects.get(pid = 555)

    print()


@api_view(['POST'])
def FL(request):
    
    Made = request.data.get('pname')
    Amount = request.data.get('LUCKAMOUNT') #luck
    Amount = float(Amount)
    Calc = 0
    Player = Playing.objects.get(p_name = Made)
    Luckview = LuckCalc.objects.get(pid = 555)
    
    if Player.p_level < 20:
        Multi = Luckview.downtwenty
        Multi = float(Multi)
        if Amount > 1:
            Calc = Amount/Multi
            if Calc <= Player.p_money:
                Playing.objects.filter(p_name = Made).update(
                    p_money = F("p_money") - Calc,
                    p_luck = F("p_luck") + Amount
                )
    elif Player.p_level < 40:
        Multi = Luckview.downforty
        Multi = float(Multi)
        if Amount > 1:
            Calc = Amount/Multi
            if Calc <= Player.p_money:
                Playing.objects.filter(p_name = Made).update(
                    p_money = F("p_money") - Calc,
                    p_luck = F("p_luck") + Amount
                )
    elif Player.p_level < 80:
        print('ybeeln;clwence;ncmwcnkwncwncwkcw kncwlkncwnkckn;wcnwclkwnklcwknlnclwndkncnkwnklcwknlcknlwdcknlwknlcnlwkcnkwnklclwkncnwnlckwnlkcnwlcnlwn')

        Multi = Luckview.downeighty
        Multi = float(Multi)
        if Amount > 1:
            Calc = Amount/Multi
            print(Calc)
            if Calc <= Player.p_money:
                Playing.objects.filter(p_name = Made).update(
                    p_money = F("p_money") - Calc,
                    p_luck = F("p_luck") + Amount
                )

                serializer = FLSerializer(Luckview)
                print(Luckview)
                return Response(serializer.data)
            

    elif Player.p_level < 160:
        Multi = Luckview.downsixteen
        Multi = float(Multi)
        if Amount > 1:
            Calc = Amount/Multi
            if Calc <= Player.p_money:
                Playing.objects.filter(p_name = Made).update(
                    p_money = F("p_money") - Calc,
                    p_luck = F("p_luck") + Amount
                )
    elif Player.p_level < 320:
        Multi = Luckview.downthirtytwo
        Multi = float(Multi)
        if Amount > 1:
            Calc = Amount/Multi
            if Calc <= Player.p_money:
                Playing.objects.filter(p_name = Made).update(
                    p_money = F("p_money") - Calc,
                    p_luck = F("p_luck") + Amount
                )
    elif Player.p_level < 999:
        Multi = Luckview.downthirtythree
        Multi = float(Multi)
        if Amount > 1:
            Calc = Amount/Multi
            if Calc <= Player.p_money:
                Playing.objects.filter(p_name = Made).update(
                    p_money = F("p_money") - Calc,
                    p_luck = F("p_luck") + Amount
                )

        
    
    
    print()

@api_view(['POST'])
def chat(request):
    
    Content = request.data.get('content')
    Made = request.data.get('pname')
    Player = Playing.objects.get(p_name = Made)

    if len(Content) <= 90:
        NewChat = Chat(p_name = Made, p_level = Player.p_level, p_content = Content, p_restricted = False)
        Chat.save(NewChat)
    



    
    print()



@api_view(['POST'])
def search(request):
    
    Made = request.data.get('won')
    Winners = Ticket.objects.filter(p_gmoney = True)
    serializer = WinnerSerializer(Winners, many = True)
    print(Winners)
    return Response(serializer.data)
    
    print()


    query = request.data.get('query', '')
    orders = request.data.get('orders', '')

    if query:
        player = Playing.objects.get(p_name = query)
        if orders <= player.p_money:
            player.p_money = player.p_money - orders
            player.p_orders = player.p_orders + orders
            Playing.save(player)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
    else:
        return Response("No Players Found")
    

@api_view(['POST'])
def orders(request):
    query = request.data.get('query', '')
    orders = request.data.get('orders', '')
    print(query)
    if query:
        player = Playing.objects.get(p_name = query)
        ord = float(orders)
        if ord <= player.p_money:
            player.p_money = player.p_money - ord
            player.p_orders = player.p_orders + ord
            Playing.save(player)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
    else:
        return Response("No Players Found")
    


@api_view(['POST'])
def won(request):
    
    Made = request.data.get('named')
    Magic = Ticket.objects.filter(p_name = Made)
    serializer = WinnerSerializer(Magic, many=True)
    print(Made, "nigga")
    return Response(serializer.data)
    
    print()



@api_view(['POST'])
def trade(request):
    
    Made = request.data.get('name')
    Magic = Trade.objects.filter(p_name = Made)
    serializer = WinnerSerializer(Magic, many=True)
    print(Made, "nigga")
    return Response(serializer.data)
    
    print()


@api_view(['POST'])
def acceptrade(request):
    
    Made = request.data.get('name')
    SP = request.data.get('secondpl')

    Seed = "{}{}".format(Made,SP)
    SeedTwo = "{}{}".format(SP,Made)

    print(Seed, SeedTwo, "god")
    try:
        Magic = Trade.objects.get(Key = Seed)
        Magic.accepted = True
        Trade.save(Magic)
        serializer = AcceptedTradeSerializer(Magic)
        print(serializer.data)
        return Response(serializer.data)
    except:
        Magic = Trade.objects.get(Key = SeedTwo)
        Magic.accepted = True
        Trade.save(Magic)
        serializer = AcceptedTradeSerializer(Magic)
        print(serializer.data)
        return Response(serializer.data)


    
    print()


@api_view(['POST'])
def showactrade(request):
    Made = request.data.get('pname')
    print(Made)
    try:
        Magic = Trade.objects.get(p_name = Made)
        if Magic.accepted == True:
                serializer = AcceptedTradeSerializer(Magic)
                print(serializer.data)
                return Response(serializer.data)
            

    except:
        try:
            Magic = Trade.objects.get(secp_name = Made)
            if Magic.accepted == True:
                serializer = AcceptedTradeSerializer(Magic)
                print(serializer.data)
                return Response(serializer.data)
        except:
            print("could find no active trades")

#make it so each glitch name must be unique
    

@api_view(['POST'])
def ACCEPTMYPART(request):
    Made = request.data.get('pname') #POST
    
    try:
        Magic = Trade.objects.get(p_name = Made)
        if Magic.accepted == True:
            if Magic.fp_accepted == True:
                Magic.fp_accepted = False
            else:
                Magic.fp_accepted = True



            
            Trade.save(Magic)
            print("god")
            serializer = AcceptedTradeSerializer(Magic)
            print(serializer.data)
            return Response(serializer.data)
            

    except:
        try:
            Magic = Trade.objects.get(secp_name = Made)
            if Magic.accepted == True:
                if Magic.secp_accepted == True:
                    Magic.secp_accepted = False
                else:
                    Magic.secp_accepted = True

                Trade.save(Magic)
                serializer = AcceptedTradeSerializer(Magic)
                print(serializer.data)
                return Response(serializer.data)
        except:
            print("could find no active trades")


    
@api_view(['POST'])
def deletemyitems(request):
    Made = request.data.get('pname')
    
    Magic = TradeSpace.objects.filter(p_name = Made)

    try:
        Lucifer = Trade.objects.get(p_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted = False
        Trade.save(Lucifer)
    except:
        Lucifer = Trade.objects.get(secp_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted = False
        Trade.save(Lucifer)

    for i in range(len(Magic)):
            _dupobj = Inventory(s_rarity = Magic[i].s_rarity, s_cooldown = defaultcd, p_name = Magic[i].p_name, s_name = Magic[i].s_name,s_status = Magic[i].s_status,s_durability = Magic[i].s_durability) 
            Inventory.save(_dupobj)


    Magic.delete()
    TradeSpace.save(Magic)

    serializer = TradeSpaceSerializer(Magic, many=True)
    print(serializer.data)
    return Response(serializer.data)



@api_view(['POST'])
def tradeshowinventory(request):
    Made = request.data.get('pname')
    try:
        Magic = Inventory.objects.filter(p_name = Made)
    except:
        Trade.objects.filter(p_name = Made).delete()
        Trade.objects.filter(secp_name = Made).delete()
        print("Player has no items to trade dis regard trade")
    
   
    serializer = InventorySerializer(Magic, many=True)
    print(serializer.data)
    return Response(serializer.data)
    
    print()



@api_view(['POST'])
def tradeshowothersinventory(request):
    Made = request.data.get('opposite')
    print(Made)
    try:
        Magic = TradeSpace.objects.filter(p_name = Made)
        serializer = TradeSpaceSerializer(Magic, many=True)
        print(serializer.data)
        return Response(serializer.data)
    except:
        print("Player has no items to trade dis regard trade")
    
    
    
    
    print()



defaultcd = 30
@api_view(['POST'])
def sendinventoryitem(request):
    Made = request.data.get('name')
    Itemname = request.data.get('item')
    Opp = ""

    print(Itemname)
    try:
        Lucifer = Trade.objects.get(p_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted= False
        Trade.save(Lucifer)
    except:
        Lucifer = Trade.objects.get(secp_name = Made)
        Lucifer.fp_accepted = False
        Lucifer.secp_accepted= False
        Trade.save(Lucifer)

    try:
        SeedKey = Trade.objects.get(p_name = Made)

        if SeedKey.p_name == Made:
            Opp = SeedKey.secp_name

        Keys = "{}{}".format(Made,Opp)
        BKeys = "{}{}".format(Opp,Made)

    except:
        SeedKey = Trade.objects.get(secp_name = Made)
        if SeedKey.secp_name == Made:
            Opp = SeedKey.p_name

        Keys = "{}{}".format(Made,Opp)
        BKeys = "{}{}".format(Opp,Made)


    try:
        Magic = Inventory.objects.filter(p_name = Made)

        for i in range(len(Magic)):
            if Magic[i].s_name == Itemname:#eventually itemname will be id
                #will eventually be an id 
                FindIT = Inventory.objects.get(s_name = Itemname)   #itemname  will transition to id
                
                NewItem  = TradeSpace(s_rarity = FindIT.s_rarity, s_cooldown = defaultcd, p_name = Made, s_name = FindIT.s_name,s_status = FindIT.s_status,s_durability = FindIT.s_durability,SeedKey = Keys, BackupKey =  BKeys) 
                TradeSpace.save(NewItem)  
                
                Inventory.delete(FindIT)
                serializer = TradeSpaceSerializer(Magic, many=True)
                print(serializer.data)
                return Response(serializer.data)
                
                
    except:
        print("no items found in inventory")

   

        
    
    
    
    print()


@api_view(['POST'])
def sendtrade(request):
    
    Made = request.data.get('requestedplayer')
    SP = request.data.get('FP')
    Magic = Playing.objects.get(p_name = Made)

    x = Made +SP
    print(Made)

    try:
        TryThis = Trade.objects.get(Key = Made+SP)
        print("There is already an active trade with this player")
    except:
        try:
            TryThis = Trade.objects.get(Key = SP+Made)
            print("There is already an active trade with this player")
        except:
            XAR = Trade.objects.filter(p_name = Made)
            if len(XAR) <1:
                NewTrade = Trade(p_name = Made, p_active = False, fp_accepted = False, secp_name = SP, secactive = 60, secp_accepted = False, middlestack = "", fpstack = "", spstack = "", Key = "{}{}".format(Made,SP), BackupKey = "{}{}".format(SP,Made), accepted = False)
                Trade.save(NewTrade)
                serializer = PlayerSearchSerializer(Magic)
                return Response(serializer.data)
            else:
                print("player already has an active trade")





@api_view(['POST'])
def moderntrade(request):
    
    Made = request.data.get('checkforplayer')
    try:
        Magic = Trade.objects.get(p_name = Made) #or Trade.objects.filter(p_name = Made)
        serializer = TradeFalseSerializer(Magic)#java gets all trades that are false
        #java gets all trades that are false
        return Response(serializer.data)
    except:
        try:
            Magic = Trade.objects.get(secp_name = Made) #or Trade.objects.filter(p_name = Made)
            serializer = TradeFalseSerializer(Magic)#java gets all trades that are false
            #java gets all trades that are false
            return Response(serializer.data)
        except:

            return Response()

            print("player has no incoming trades") #when creating a trade the selected players name will be the p_name so frontend will check for any incoming trades with p_name
    




@api_view(['POST'])
def playersearch(request):
    
    Made = request.data.get('requestedplayer')
    Magic = Playing.objects.get(p_name = Made)
    serializer = PlayerSearchSerializer(Magic)
    print(Made, "nigga")
    return Response(serializer.data)
    
    print()


from django.db.models import F

@api_view(['POST'])
def donate(request):
    
    Made = request.data.get('pname')
    Amount = request.data.get('Amnt')
    SP = request.data.get('stem')


    print("NIFEIONNNNNNNNNNNNNEIEII")


    try:
        Thisplayer = Playing.objects.get(p_name = Made)
        Donatedone = Playing.objects.get(p_name = SP)

        Amount = float(Amount)
        if Thisplayer.p_money >= Amount:
        
            Playing.objects.filter(p_name = Made).update(
                p_money = F("p_money") - Amount
            )

            Playing.objects.filter(p_name = SP).update(
                p_money = F("p_money") + Amount
            )

            print("love")
            




    except:
        Thisplayer = Playing.objects.get(p_name = Made)
        Donatedone = Playing.objects.get(p_name = SP)
        Amount = float(Amount)
        Amount = float(Amount)
        if Thisplayer.p_money >= Amount:
        
            Playing.objects.filter(p_name = Made).update(
                p_money = F("p_money") - Amount
            )

            Playing.objects.filter(p_name = SP).update(
                p_money = F("p_money") + Amount
            )

    



    



    serializer = PlayerSearchSerializer(Donatedone)
    print(serializer.data)
    return Response(serializer.data)
    
    print()





@api_view(['POST'])
def ForceLuck(request):
    
    Made = request.data.get('pname')
    Amount = request.data.get('Amnt')
    SP = request.data.get('stem')


    print("NIFEIONNNNNNNNNNNNNEIEII")


    try:
        Thisplayer = Playing.objects.get(p_name = Made)
        Donatedone = Playing.objects.get(p_name = SP)

        Amount = float(Amount)
        if Thisplayer.p_money >= Amount:
        
            Playing.objects.filter(p_name = Made).update(
                p_money = F("p_money") - Amount
            )

            Playing.objects.filter(p_name = SP).update(
                p_money = F("p_money") + Amount
            )

            print("love")
            




    except:
        Thisplayer = Playing.objects.get(p_name = Made)
        Donatedone = Playing.objects.get(p_name = SP)
        Amount = float(Amount)
        Amount = float(Amount)
        if Thisplayer.p_money >= Amount:
        
            Playing.objects.filter(p_name = Made).update(
                p_money = F("p_money") - Amount
            )

            Playing.objects.filter(p_name = SP).update(
                p_money = F("p_money") + Amount
            )

    



    



    serializer = PlayerSearchSerializer(Donatedone)
    print(serializer.data)
    return Response(serializer.data)
    
    print()