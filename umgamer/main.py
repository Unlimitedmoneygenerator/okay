from .models import Game, Playing, Modifiers, Money, glitch, PlayingMode, Ticket, Level, Trade
import time
from django.db.models import F
import random
from django.db.models import Min
from django.db.models import Q

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
iter_time = 5
#add one week season for season seed
_seasonseed ={"_4week":2419200,"_8week":4838400,"_10week":6048000,"_12week":7257600,"_random":(random.randint(4800, 7257600)),"_36week":7257600 }
_indexseed = {1:_seasonseed['_4week'],2:_seasonseed['_8week'],3:_seasonseed['_10week'],4:_seasonseed['_12week'],5:_seasonseed['_random']}
_seasontype = (random.randint(1,5))
_seasontimer = 0
                                                                                                            #try week long round point blank period game starts off order per 5 secs can inc if you need try 7 secs too
sorestackmax = 40
_roundseed ={"_30mins":1800,"_1hour":3600,"_3hour":10800,"_12hour":43200,"_random":(random.randint(300, 86400))} #add 15 minute round , update 3(for a million players add, a 2 week to a month round(special round)) add 72 hour round. #may need a later patch to make rounds shorter after people learn the game. the players not knowing about luck is temporary therefore you will have to patch it up but for now no patch needed.
_indexround = {1:_roundseed['_30mins'],2:_roundseed['_1hour'],3:_roundseed['_3hour'],4:_roundseed['_12hour'],5:_roundseed['_random']} # ADD A SIXTH ROUND SEED 6 HOURS ADD A SEVENTTH ROUND 15 MINUTES
_roundtype = (random.randint(1,5)) 
_roundtimer = 0





def display():
    varvar = Playing.objects.get(p_name = 'VarVar')
    print(varvar.p_orders)
    try:
        tickets = Ticket.objects.filter(p_name = 'VarVar')
        print(tickets.p_amount)
    except:
          print("no tickets")
    
    TMONEY = False
    #order_list = Playing.objects.values_list('p_name', 'p_luck')
    #min = order_list.order_by('p_luck').last()
    #print(min, 'mini')
    #Trade.objects.filter( secactive = 0).delete() dnddiok3diondd
   # Trade.objects.all().update(
     #     secactive = F("secactive") - iter_time
    #) # dont forget

    try:
        _Playingt = PlayingMode.objects.get(s_playing = True)
        Playtime = _Playingt.s_playing
        #print('goood')
    except:
        _Playingt = PlayingMode.objects.filter(s_playing = False).update(
             s_playing=True
        )

        _Playingt = PlayingMode.objects.get(s_playing = True)
        print("gooft", "ariie")
    
    if _Playingt.s_playing == True:
        _Gamelibb =[]
        #try:
        Game.objects.filter(seshcount = 1).update(
             roundtime = F("roundtime") + iter_time,
             seasontime = F("seasontime") + iter_time

             )
                        
        #Season.save()
            #try:
        Playing.objects.all().update( 
             P_tmoney = False
        )
        Players = Playing.objects.all()
        lover = True
        if lover ==True:
        #try: #try
            Season = Game.objects.get(seshcount = 1)
            
            if Season.seasontime <= Season.seasonseed: ###
                    #print(Season.seasontime, 'season')
                    if Season.roundtime <= Season.roundseed:


                        

                        #Ticket.objects.all().update(
                             #p_gmoney = False 
                        #)

                        
                        
                        _Playsize = []
                        _Gamelibb = []
                        _updlist = []
                        badu = 0
                        Playing.objects.filter(p_orders = 0).update(
                              p_playing = False
                              
                        )

                        
                        Playing.objects.filter(~Q(p_orders = 0)).update(
                                      p_playing = True

                                      
                                )

                        dad = random.randint(0,5000)

                        if dad <=1000:
                              orders = random.randint(0,10)

                              Playing.objects.filter(~Q(p_money = 0)).update(
                                    p_money = F('p_money') - 1,
                                    p_orders = F('p_orders') + orders
                              )

                              Playing.objects.filter(p_name = "VarVar").update(
                                    p_orders = F('p_orders') - orders,
                                    p_money = F('p_money') + 1
                              )
                        if dad >4000:
                              Playing.objects.filter(p_orders = 0).update(
                                    p_orders = F('p_orders') + random.randint(0,30)
                              )

                        if dad <1000:
                              Playing.objects.filter(p_money = 0).update(
                                    p_money = F('p_money') + random.randint(0,5)
                              )  

                        print("finished")
                        _totplayer = []
                        ACTPLAYER = Playing.objects.filter(p_playing = True)
                        if len(ACTPLAYER) >= 1:
                            try:
                                ACTPLAYER.update(
                                        p_orders = F("p_orders") - 1,
                                        P_tmoney = True,
                                        p_luck = F('p_luck') + 0.2,
                                        p_exp = F('p_exp') + 1,
                                    )
                                TMONEY = True
                            except:
                                
                                Idus = 0
                            
                            print('jurl')
                            for i in range(len(ACTPLAYER)):
                                _Playerluck = ACTPLAYER[i].p_luck
                                _Playerluck = _Playerluck + 1
                                _Playername = ACTPLAYER[i].p_name
                                for i in range(round(_Playerluck)):
                                    
                                    _totplayer.append(_Playername)
                           
                                    
                                
                                
    

                    

                            wingod = Modifiers.objects.get(seasoncounter = 1)
                            winsplit = wingod.winnersplit
                            winsplit = str(winsplit)
                            winsplit = float(winsplit)
                            totalwinpull = len(_totplayer)
                            winpick = (random.randint(0,totalwinpull))
                            prize = (len(ACTPLAYER))

                            lovett = prize * winsplit
                            x = Money.objects.get(s_winners = "love")
                            UMGTAXED = prize*0.01
                            #print(UMGTAXED, "UMG")

                            Money.objects.all().update(
                                  s_total_umg = F("s_total_umg") + UMGTAXED
                            )
                            

                            luck = {2:0.01}
                            gotluck = luck[2]

                       


                            def win(winner, winnings, lck):
                                try:
                                    _winplayer = _totplayer[winner]
                                    _winplayer = Playing.objects.get(p_name = _winplayer)
                                    #print(winner)
                                    #print(_totplayer[winner].p_name)
                                    _lrand = (random.randint(1,5))
                                    pass
                                except:
                                    winner = winner - 1
                                    _winplayer = _totplayer[winner]
                                    _winplayer = Playing.objects.get(p_name = _winplayer)
                                    #print(winner, "unhandled exception")
                                    #print(_totplayer[winner - 1].p_name)
                                    _lrand = (random.randint(1,5))
                                    pass
                                finally:
                                
                                    god=0
                                    
                                try:
                                      winner = Playing.objects.get(p_name = _winplayer.p_name)
                                    
                                except:
                                      winner = Playing.objects.filter(p_name = _winplayer.p_name)
                                      winner = winner[0]
                              

                                
                                
                                
                                if _winplayer.p_name == winner.p_name:
                                        bestrare = 0.99
                                        nestrare = 0.90
                                        eggrare = 0.45
                                        god=0#print(i,2)      
                                        try:
                                                    #remember to add fraud prevent from leaving game before we take luck away
                                            if winner.p_inventory[0].s_status == "PlayerPay": #PlayerPay
                                                    
                                                        
                                                                if winner.p_name == _winplayer.p_name:
                                                                    print("good girl")
                                                                    if winner.p_inventory[0].s_rarity == "Real":
                                                                        
                                                                        print(winner.p_luck, 1,winner.p_name)
                                                                        del winner.p_inventory[0]
                                                                        winner.p_luck = winner.p_luck * bestrare
                                                                        print(winner.p_luck, 2, winner.p_name)
                                                                        Playing.save(winner)
                                                                        #print("goodd")
                                                                        for i in range(len(_Gamelibb)):
                                                                            if _Gamelibb[i].p_name == winner.p_name:
                                                                                _Gamelibb[i].p_luck = winner.p_luck
                                                                                
                                                                                break
                                                                            else:
                                                                                god=0#print("incorrect") 
                                                            
                                                                    elif winner.p_inventory[0].s_rarity == "Legendary":
                                                                    
                                                                        del winner.p_inventory[0]
                                                                        winner.p_luck = winner.p_luck * nestrare
                                                                        Playing.save(winner)
                                                                        
                                                                        for i in range(len(_Gamelibb)):
                                                                            if _Gamelibb[i].p_name == winner.p_name:
                                                                                _Gamelibb[i].p_luck = winner.p_luck
                                                                                break
                                                                            else:
                                                                                god=0#print("incorrect") 
                                                                        #_GAMELIBB[i].p_luck = _GAMELIBB[i].p_luck * nestrare
                                                                        #print("success", "planb")
                                                                        #finish these
                                                                    else:
                                                                        
                                                                        del  winner.p_inventory[0]
                                                                        winner.p_luck = winner.p_luck * eggrare
                                                                        Playing.save(winner)
                                                                        for i in range(len(_Gamelibb)):
                                                                            if _Gamelibb[i].p_name == winner.p_name:
                                                                                _Gamelibb[i].p_luck = winner.p_luck
                                                                                break
                                                                            else:
                                                                                god=0
                                                                        #_GAMELIBB[i].p_luck = _GAMELIBB[i].p_luck * eggrare
                                                                        print("success", "pottle, wdw",_Gamelibb[i].p_name)

                                                                    print(_Gamelibb[i].p_name, _Gamelibb[i].p_luck, _Gamelibb[i].p_money, "locale")
                                                                    print(_winplayer.p_name, _winplayer.p_luck, _winplayer.p_money, "winner")
                                                            
                                            elif _winplayer.p_name == winner.p_name:
                                                            print("except", winner.p_money,winner.p_luck,winner.p_name, "elif" , gotluck)
                                                            holdwinnerdata = _winplayer.p_luck
                                                            winner.p_luck = winner.p_luck * gotluck
                                                            Playing.save(winner)
                                                            print("except", winner.p_money,winner.p_luck,winner.p_name, "elif", gotluck )
                                                            
                                                            
                                                    
                                                    
                                        except:
                                                if _winplayer.p_name == winner.p_name:

                                                        holdwinnerdata = winner.p_luck
                                                        winner.p_luck = winner.p_luck * gotluck
                                                        #winner.p-playing = false
                                                        Playing.save(winner)
                                                        #print(_winplayer.p_name, winner.p_name,winner.p_luck,winner.p_money,gotluck, "resolve")
                            win(winpick, lovett, luck)
                            
                                  
                            
                            sorewinners = []
                            sorelosers = []
                            sorelist = []


                            soresgod = Modifiers.objects.get(seasoncounter = 1)
                            sores = random.randint(1,soresgod.sores)
                            
                                #two versions for sore winners
                            
                                #print()

                            #if < 30 for gamelength create a new list
                                
                                    
                            def sorepicks(sorese): #second version
                                    for i in range(sorese):
                                        try:
                                            length = len(_totplayer)
                                            length = length - 1
                                            thiswin = (random.randint(0, length))
                                            wone = _totplayer[thiswin]
                                            
                                        except:
                                            length = len(_totplayer)
                                            thiswin = (random.randint(0, length))
                                            wone = _totplayer[thiswin]
                                            print("good boy")
                                    
                                  
                                        try:
                                            findwinner = Playing.objects.get(p_name = _totplayer[thiswin])
                                            
                                        except:
                                            thiswin = (random.randint(0, length))
                                            print("random dancing")
                                            findwinner = Playing.objects.get(p_name = _totplayer[thiswin])
                                            
                                        
                                        #findwinner = Playing.objects.get(p_name = sorelosers[thiswin].p_name)
                                        Mods = Modifiers.objects.get(seasoncounter = 1)
                                        xio = str(Mods.soresplit)
                                        xzo = float(xio)
                                        #findwinner = Playing.objects.filter(p_name = sorelosers[thiswin].p_name).update(
                                            # p_money = F("p_money") + .29
                                        #)
                                        Winning_S = Ticket(p_gmoney = True, p_name = findwinner.p_name, p_amount = prize * soresgod.soresplit/sorese, p_class = "Sore Loser")
                                        sorelist.append(Winning_S)
                                        #Ticket.save(Winning_S)
                                        
                                        if _totplayer[thiswin] == findwinner.p_name:
                                                findwinner.p_playing = False
                                                #print(findwinner.p_name,findwinner.p_money,findwinner.p_luck, "hello", prize * Mods.soresplit/sorese) #2
                                                findwinner.p_money = findwinner.p_money + prize* xzo/sorese
                                                findwinner.p_exp = findwinner.p_exp + prize* xzo/sorese
                                                Playing.save(findwinner)
                                                
                                                    

                                        
                                                    
                                        else:
                                                god=0
                                                #print("not correct player")

                           

                            try:
                                    _winnplayer = _totplayer[winpick]
                                    _winnplayer = Playing.objects.get(p_name = _winnplayer)
                                    #print(_winnplayer.p_name, "good")
                            except:
                                    winpick = winpick - 1
                                    _winnplayer = _totplayer[winpick]  
                                    _winnplayer = Playing.objects.get(p_name = _winnplayer)  
                                    print(_winnplayer.p_name, "bad at least have same name") 
                            

                                    #print( "love")

                            
                                
                            

                                    
                                
                           

                            
                            sorepicks(sores)

                            Ticket.objects.all().update(
                                    p_gmoney = False 
                                    )
                            
                            Ticket.objects.bulk_create(sorelist)








                    
                    
                            
                                                    #print("no drop",Bad)



                            
                            try:
                                    if TMONEY == True:
                                        JWONplayer = Playing.objects.get(p_name = _winnplayer.p_name)
                                        JWONplayer.p_money = JWONplayer.p_money + lovett
                                        JWONplayer.p_playing = False
                                        JWONplayer.p_exp = JWONplayer.p_exp + lovett
                                        Playing.save(JWONplayer)
                                        TMONEY = False
                                        Winning_T = Ticket(p_gmoney = True, p_name = JWONplayer.p_name, p_amount = lovett, p_class = "Winner")
                                        Ticket.save(Winning_T)
                                    
                                    #print(JWONplayer.p_money,JWONplayer.p_name,JWONplayer.p_luck)   
                            except:
                                    print("was not able to get player")

                    elif Season.roundtime >= Season.roundseed:
                        intnum = 120
                        intnum = float(intnum)
                        love = True
                        if love == True:
                            Ticket.objects.all().update(
                                    p_gmoney = False 
                                    )
                            Winning_S = Ticket(p_gmoney = True, p_name = "Intermission", p_amount = intnum, p_class = "Please wait, before placing any orders, if you place any orders they will be disregarded.")
                            Ticket.save(Winning_S)
                            print(Season.roundtime, "done")
                            Season.roundtime = 0
                            Season.roundseed =  _indexround[random.randint(1,5)]
                            Newrnd = Game.objects.get(seshcount = 1)
                            Newrnd.roundtime = 0
                            
                            Payours = Modifiers.objects.get(seasoncounter = 1)
                            Payours.sores = random.randint(50, 120)
                            Modifiers.save(Payours)
                            Game.save(Season)

                            Game.save(Newrnd)
                            winnersare = (random.randint(2, 10)) #0.7
                            winnersare = winnersare * 0.1
                            winnersare = winnersare - 0.1
                            soresgets = 0.99 - winnersare
                            intnum = float(intnum)
                            umgtaxd = 1 - (soresgets+winnersare)
                            print(winnersare, soresgets, umgtaxd)
                            #soresget = newtotal - #winnersare

                            Modifiers.objects.all().update(
                                    winnersplit = winnersare,
                                    soresplit = soresgets,
                                    umgtax = umgtaxd
                                )
                            
                            #roundtoken = game(_roundtimer, _indexround[random.randint(1,5)])
                            print(Season.roundtime, Season.roundseed)
                            Playing.objects.all().update(
                                p_luck = 1,
                                p_orders = 0,
                                p_playing = False
                            )
                            #Playing.objects.filter(p_playing = False).update(
                                #p_luck = 1,
                                #p_orders = 0
                            #)
                            #Playing.objects.filter(p_playing = True).update(
                               # p_luck = 1,
                                #p_orders = 0
                            #)

                            listobj = []
                            kia = Playing.objects.filter(p_id = 5)
                            for i in range(len(kia)):
                                  varer = random.randint(0,100)
                                  varer = float(varer)
                                  kia[i].p_money = kia[i].p_money + varer
                                  kia[i].p_orders = random.randint(0, 100)

                                  kiasix = Playing(p_name = kia[i].p_name, p_storedluck = 0, p_slot = "None", p_id = 5, p_money = kia[i].p_money, p_luck = 1, p_level = kia[i].p_level, p_orders = kia[i].p_orders, p_exp = kia[i].p_exp, p_trades = False, P_tmoney = False,p_playing = True, p_forceluck = 0.001, p_inventory = [], p_friends = ["None"],p_acceptfriends = False,p_messages = "None", p_messagesaccept = False,p_banned ="None")
                                  listobj.append(kiasix)
    



                                  #Playing.save(kia[i])

                            Playing.objects.filter(p_id = 5).delete()

                            Playing.objects.bulk_create(listobj)
                                
                            print("intermission", "car")
                            for love in range(24):
                                time.sleep(5)
                                print("coco")
                                intnum = intnum - 5
                                Ticket.objects.all().update(
                                    p_gmoney = False 
                                    )
                                Winning_S = Ticket(p_gmoney = True, p_name = "Intermission", p_amount = intnum, p_class = "Please wait.")

                                Ticket.save(Winning_S)
                                Season.seasontime = Season.seasontime + 5 
                                Game.save(Season)

                            Playertime = PlayingMode.objects.all()
                            
                            #Playertime.s_playing = True
                            Playertime[0].s_playing = True
                            PlayingMode.save(Playertime[0])
                                
                            #music clear, import original soundtrack again play from top shuffle

                                     
                            
                
                #seasontoken = game(_seasontimer, _indexseed[random.randint(1,5)])
                #print(seasontoken.newseasonseed,seasontoken.newseasontiming)
                
                #reset(seasontoken)
                        
                        
                    
        
                        
                   
                
                

                    #def soreloss(soreloss):
                     

                
                
                    #_playerlibrary.index(_totplayer[winner])
    
                    #print(_playerlibrary)
                    #for i in range(playsize):
                        #if _playerlibrary[i].p_name == _totplayer[winner].p_name:
                            #_playerlibrary[i] = _totplayer[winner]
                            #print(_totplayer[winner].p_name,_playerlibrary[i].p_name, "done")
            
                            #print(_playerlibrary[i].p_money,_playerlibrary[i].p_luck, "love you")
                        #else:
                            #print('no')
                    

                    
                        #_totplayer.append(_locplname)
                   
                        #print(_curplayer.p_name)
                        #_totplayer = _totplayer + _locplayer.p_name
                        #print("LOVEEEEEEEEEEE",_totplayer)
                    #import winners of queue, #import drops
                    #queue =[]
                    #queue_luck =[]
                    #for i in range totalplayers:
                    #glitch drop try and find matching number
                    #then relay the information back over to main
                    #in main updatefunc() grabbing info from timeless
                #time.sleep(40)             
            else: 
                        if Season.seasontime >= Season.seasonseed:
                            #print(seasontoken.newseasonseed)
                            print("season is over") 
                            try:
                                Playertime = PlayingMode.objects.get(s_playing = True)
                                Playertime.s_playing = False
                                PlayingMode.save(Playertime)
                            except:
                                Playertime = PlayingMode.objects.get(s_playing = False)
                                Playertime.s_playing = False
                                PlayingMode.save(Playertime)

                            winnersare = (random.randint(2, 10)) #0.7
                            winnersare = winnersare * 0.1
                            winnersare = winnersare - 0.1
                            soresgets = 0.99 - winnersare
                            umgtaxd = 1 - (soresgets+winnersare)
                            print(winnersare, soresgets, umgtaxd)
                            #soresget = newtotal - #winnersare
                            Modifiers.objects.all().update(
                                    winnersplit = winnersare,
                                    soresplit = soresgets,
                                    umgtax = umgtaxd
                                )
                            
                            
                            #seasontoken = game(_seasontimer, _indexseed[random.randint(1,5)])
                            #print(seasontoken.newseasonseed,seasontoken.newseasontiming)
                            #del seasontoken
                            #reset(seasontoken)
                            #remember
                            #roundtoken = game(_roundtimer, _indexround[random.randint(1,5)])
                            #seasontoken = game(_seasontimer, _indexseed[random.randint(1,5)])
                            NewGame = Game.objects.get(seshcount = 1)
                            print("new game")
                            time.sleep(120)
                            NewGame.seasontime = 0 
                            NewGame.seasonseed = _indexseed[random.randint(1,5)]
                            NewGame.roundtime = 0
                            NewGame.roundseed = _indexround[random.randint(1,5)]

                            Game.save(NewGame)

                            
                            
                            
                            Playertime = PlayingMode.objects.get(s_playing = False)
                            Playertime.s_playing = True
                            PlayingMode.save(Playertime) 

                            
                            
                               # print(_Gamelibb[i].p_name, _Gamelibb[i].p_money,_Gamelibb[i].p_luck,"after")

                            

                        #elif _GAMELIB[i].p_tmoney == False:
                            
                            #time.sleep(3)    
            
       
                      
    else:
         xo = PlayingMode.objects.all()
         xo[0].s_playing = True
         PlayingMode.save(xo[0])
            
      

                        








                        #tmoney = false to each player after round
                         #for i in range():
                             #Playing(Playing[i]).save() save all player data at the end
                    

        

            

                

            #if Season.seasontime >= Season.seasonseed:
                #print("solid")
            #else:

               # print("god")


        #except:
            #print("god")

        
    


scheduler = BackgroundScheduler()
mainhand = BackgroundScheduler()


scheduler.add_job(display, "interval", seconds = 3)

scheduler.start()

 

#time.sleep(2)
#Season.seasontime = Season.seasontime + 2
#Season.save()
#print("five")