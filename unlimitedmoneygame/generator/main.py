

from nowpayment import NowPayments
payments = NowPayments("0X69GM1-0YQMQM3-GH4TPKG-YP685FF")

from nowpay import NOWPayments
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
#lucifer = NOWPayments("0X69GM1-0YQMQM3-GH4TPKG-YP685FF")

import random
from .models import Invoice, KeySeed

#status = payment.create_payment(100,'USD','btc')
status = ""

#status = payments.payment.get_payment_status(4710396570)


scheduler = BackgroundScheduler()



 

keygenone = random.randint(100000,999990)
keygentwo = random.randint(100000,999990)
keygenthree = random.randint(100000,999990)
keygenfour= random.randint(100000,999990)
KeyCode = ('{}-{}-{}-{}').format(keygenone,keygentwo,keygenthree,keygenfour)

#ThisInv = Invoice.objects.get(payment_id = 6201324434)
#NewKey = KeySeed(p_namer = "", p_keyseed = KeyCode, p_amounted = ThisInv.price_amount *0.995, p_timer = 0, p_activated = False)

# after 60 minutes delete invoice
#next step return the invoice, and make a screen where they can pay, then make a system that allows you to track the payments, update the amounts in the invoices and so forth. x the price amount by 
#99.5 for crypto


def checkup():
    try:
        x = Invoice.objects.filter(payment_status = 'waiting')
        
        for i in range(len(x)):      
            x[i].payment_id
            status = payments.payment.get_payment_status(x[i].payment_id)
            ThisInv = Invoice.objects.get(payment_id = x[i].payment_id)
            ThisInv.pay_amount = status['pay_amount'] 
            ThisInv.amount_received = status['actually_paid']
            Invoice.save(ThisInv)
            print(status)

            if status['actually_paid'] >= status['pay_amount']:

                keygenone = random.randint(100000,999999)
                keygentwo = random.randint(100000,999999)
                keygenthree = random.randint(100000,999999)
                keygenfour= random.randint(100000,999999)
                KeyCode = ('{}-{}-{}-{}').format(keygenone,keygentwo,keygenthree,keygenfour)

                try:
                    KeySeed.objects.get(p_keyseed = KeyCode)
                except:
                    ThisInv.payment_status = "complete"
                    ThisInv.pay_amount = status['pay_amount'] 
                    ThisInv.amount_received = status['actually_paid']
                    Invoice.save(ThisInv)

                    #thisinv.payamount convert to usd in btc with coinbase api, and then give them that amount. in p_amounted
                    NewKey = KeySeed(p_namer = ThisInv.username, p_keyseed = KeyCode, p_amounted = ThisInv.price_amount *.995, p_timer = 0, p_activated = False)
    except:
        print("noobjects")
    



            
#function, every 600 seconds take that away and if it is at 0 delete the payment. from frontend only grab the payment from backend.

scheduler.add_job(checkup, "interval", seconds = 5)

scheduler.start()
