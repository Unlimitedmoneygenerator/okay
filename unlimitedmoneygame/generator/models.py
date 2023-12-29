from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
import random

from django.core.validators import MaxValueValidator, MinValueValidator 

STATIC = []

class APIKEY(models.Model):
     KEY = models.CharField(max_length = 255)

class Invoice(models.Model):
     username = models.CharField(max_length = 255)
     pay_amount = models.FloatField()
     amount_received = models.FloatField()
     address = models.CharField(max_length = 255)
     payment_id = models.CharField(max_length = 255)
     payment_status = models.CharField(max_length = 255)
     price_amount = models.PositiveIntegerField()
     p_timer = models.PositiveIntegerField()
     p_qrcode = models.CharField(max_length =255)

class DeletedInvoice(models.Model):
     username = models.CharField(max_length = 255)
     pay_amount = models.FloatField()
     amount_received = models.FloatField()
     address = models.CharField(max_length = 255)
     payment_id = models.CharField(max_length = 255)
     payment_status = models.CharField(max_length = 255)
     price_amount = models.PositiveIntegerField()
     p_timer = models.PositiveIntegerField()
     p_qrcode = models.CharField(max_length =255)

class User(AbstractUser):
     stripe_customer_id = models.CharField(max_length=255, blank =True, null=True)
     username = models.CharField(max_length = 16, unique = True)
     password = models.CharField(max_length = 255)
     email = models.CharField(max_length = 255)
     p_money = models.FloatField(null = True)
     p_storedluck = models.FloatField(null = True)
     p_luck = models.FloatField(null = True)
     p_level = models.PositiveIntegerField(null = True)
     p_orders = models.PositiveIntegerField(null = True)
     p_exp = models.PositiveIntegerField(null = True)  #(max_length=7, default='0000000', editable=False)
     p_trades = models.BooleanField(null = True)
     P_tmoney = models.BooleanField(null = True)
     p_playing = models.BooleanField(null = True)
     p_forceluck = models.DecimalField(null = True, max_digits=3, decimal_places=3)
     p_acceptfriends = models.BooleanField(null = True)
     p_messagesaccept = models.BooleanField(null = True)
     p_currentrade = models.CharField(max_length=32)
     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['email','password']


class KeySeed(models.Model):
     p_namer = models.CharField(max_length = 16)
     p_keyseed = models.CharField(max_length = 32)
     p_amounted = models.FloatField()
     p_timer = models.PositiveIntegerField()
     p_activated = models.BooleanField()

#if bitcoin timer = 0 
     
#if stripe timer = 1209600

class PayingUser(models.Model):
     app_user = models.ForeignKey(User, on_delete=models.CASCADE)
     payment_bool = models.BooleanField(default=False)
     stripe_checkout_id = models.CharField(max_length=500)


# Create your models here.
     
valid = 120
keyseedone = random.randint(1000,9999)
keyseedtwo = random.randint(1000,9999)
keyseedthree = random.randint(1000,9999)
keyseedfour = random.randint(1000,9999)

class PlayingMode(models.Model):
     s_playing = models.BooleanField()
     

class Tradesend():
     
     def __init__(self,playername,tradername, traderlevel, tradetime, tradedata) :
          self.playername = playername
          self.tradername = tradername
          self.traderlevel = traderlevel
          self.tradetime = tradetime
          self.tradedata = tradedata
          
     #class ONGOINGTRADE():
     def ongoing(self):
          aside = self.playername
          asidegave = []
          bsideaccept = False
          bside = self.tradername
          bsidegave = []
          bsideaccept = False

          #if True:
               #for i in range(len(bsidegave)):
                   # Again = Players.objects.get(aside)
                    #Again.p_inventory.append
                    
                    #aside. bsidegave[i]    
                


          
     
       
        


class TRADE(Tradesend):
     pass
     
tradefromVox = TRADE("Voxmelud","VoxMelud", 67, valid, [])


#leveling system
#   



class Inventory(models.Model):
    p_name = models.CharField(max_length=16)
    s_rarity = models.CharField(max_length=16)
    s_cooldown = models.PositiveIntegerField()
    s_name = models.CharField(max_length=16)
    s_status = models.CharField(max_length=16)
    s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
    def __str__(self):
         return "{}'s  {}".format(self.p_name, self.s_name)

        

class Money(models.Model):
     s_name = "Money"
     s_umg_order = models.PositiveIntegerField()
     s_won_order = models.PositiveIntegerField()
     s_sores_order =models.PositiveIntegerField()
     s_total_sores = models.PositiveIntegerField()
     s_total_umg = models.FloatField()
     s_total_won = models.PositiveIntegerField()
     s_winners = models.CharField(max_length=9999)
     s_losers = models.CharField(max_length=9999)

     def __str__(self):
          return self.s_name


class glitch(models.Model):
    s_rarity = models.CharField(max_length=16)
    s_name = models.CharField(max_length=16)
    s_status = models.CharField(max_length=16)
    s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
    def __str__(self):
         return self.s_status
    



class black(models.Model):
     name = models.CharField(max_length=16)

     def __str__(self):
          return self.name

class Playing(models.Model):
    p_name = models.CharField(max_length=16)
    p_id = models.PositiveIntegerField()
    p_money = models.FloatField()
    p_storedluck = models.FloatField()
    p_luck = models.FloatField()
    p_level = models.PositiveIntegerField()
    p_orders = models.PositiveIntegerField()
    p_exp = models.PositiveIntegerField()
    p_trades = models.BooleanField()
    P_tmoney = models.BooleanField()
    p_playing = models.BooleanField()
    p_forceluck = models.DecimalField(max_digits=3, decimal_places=3)
    p_inventory = models.JSONField()
    p_slot = models.JSONField()
    p_friends = models.JSONField()
    p_acceptfriends = models.BooleanField()
    p_messages = models.JSONField()
    p_messagesaccept = models.BooleanField()
    p_banned = models.JSONField()
    p_currentrade = models.CharField(max_length=32)
    
    #playerordersbeforewin, reset every round, every win, not sore loss.


    #for sorelosers and winners ticket store, orders placed before win,
    
         


    class Slot:
        SlotCapture = ""
        Slotz = []
    
    


    class Meta:
        ordering = ("p_name",)

    def __str__(self):
        return self.p_name
    
class LuckCalc(models.Model):
     downtwenty = models.DecimalField(max_digits=3, decimal_places=3) #0.001 base <
     downforty = models.DecimalField(max_digits=3, decimal_places=3) #0.003 base <
     downeighty = models.DecimalField(max_digits=3, decimal_places=3) #0.005 base <
     downsixteen = models.DecimalField(max_digits=3, decimal_places=3) #0.010 <
     downthirtytwo = models.DecimalField(max_digits=3, decimal_places=3) #0.015 <
     downthirtythree = models.DecimalField(max_digits=3, decimal_places=3) #0.027 #max level 320
     pid = models.PositiveIntegerField()

    
class Messages(models.Model):
     p_name = models.CharField(max_length=16)
     sp_name = models.CharField(max_length=16)
     Msgkey = models.CharField(max_length=32)
     keyMsg = models.CharField(max_length=32)
     Msgcontent = models.JSONField()

class Chat(models.Model):
     p_name = models.CharField(max_length=16)
     p_level = models.PositiveIntegerField()
     p_content = models.CharField(max_length=90)
     p_restricted = models.BooleanField()

class Slot(models.Model):
    s_rarity = models.CharField(max_length=16)
    p_name = models.CharField(max_length=16)
    s_cooldown = models.PositiveIntegerField()
    s_name = models.CharField(max_length=16)
    s_status = models.CharField(max_length=16)
    s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
    def __str__(self):
         return self.s_status

class TradeSpace(models.Model):
     s_rarity = models.CharField(max_length=16)
     p_name = models.CharField(max_length=16)
     s_cooldown = models.PositiveIntegerField()
     s_name = models.CharField(max_length=16)
     s_status = models.CharField(max_length=16)
     s_durability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
     SeedKey = models.CharField(max_length = 32)
     BackupKey = models.CharField(max_length = 32)

class Trade(models.Model):
     p_name = models.CharField(max_length=16)
     p_active = models.BooleanField()
     fp_accepted = models.BooleanField()
     secp_name = models.CharField(max_length=16)
     secactive = models.PositiveIntegerField()
     secp_accepted = models.BooleanField()
     middlestack = models.JSONField()
     fpstack = models.JSONField()
     spstack = models.JSONField()
     Key = models.CharField(max_length=27)
     BackupKey = models.CharField(max_length=27)
     accepted = models.BooleanField()


#Winning = Winners(p_name = "lovebug",amount = 1000,w_class = "winner")
#Winning.save()

class Ticket(models.Model):  #GIVE THE TICKETS ID , AND ORDERS PLACED FIELD
    p_gmoney = models.BooleanField()
    p_name = models.CharField(max_length=16)
    p_amount = models.FloatField()
    p_class = models.CharField(max_length=16)
    def __str__(self):
         return "{} :  {}".format(self.p_class,self.p_name)


class Market(models.Model):
     Marketname = "Market"
     owner = models.CharField(max_length=16)
     price = models.PositiveIntegerField()
     itemname = models.CharField(max_length=16)
     itemstatus = models.CharField(max_length=16)
     itemrarity = models.CharField(max_length=16)
     itemdurability = models.PositiveIntegerField(default= 1, validators=[MinValueValidator(1), MaxValueValidator(500)])
     itemid = models.PositiveIntegerField()
     imgurl = models.CharField(max_length=72)
     def __str__(self):
          return self.Marketname

class Level(models.Model):
     name = "Level"
     correspondinglevel = models.PositiveIntegerField()
     correspondingexp = models.PositiveIntegerField()
     def __str__(self):
          return ("{} {}".format(self.name,self.correspondinglevel,))
     
     

        
class Modifiers(models.Model):
     baseluck = models.DecimalField(max_digits=2, decimal_places=2)
     takemoney = models.PositiveIntegerField()
     baseforceluck = models.DecimalField(max_digits=3, decimal_places=3)
     sores = models.PositiveIntegerField()
     umgtax = models.FloatField()
     winnersplit = models.DecimalField(max_digits=2, decimal_places=2)
     soresplit = models.DecimalField(max_digits=2, decimal_places=2)
     seasoncounter = models.PositiveIntegerField()
     sorelosers = 0
     drops = 10
     m_name = "Modifiers"

     def __str__(self):
          return self.m_name
          

class Luck(models.Model):
     p_name = models.CharField(max_length=20)


class Game(models.Model):
    name = "season"
    seasontime = models.PositiveIntegerField()
    seasonseed = models.PositiveIntegerField()
    roundtime = models.PositiveIntegerField()
    roundseed = models.PositiveIntegerField()   
    roundcounter = models.PositiveIntegerField()
    seshcount = models.PositiveIntegerField()

    
    def __str__(self):
         return ("{} {}".format(self.name,self.roundcounter,))






#class Inventory(models.Model):
    #Inventoryis = models.ForeignKey(Players, on_delete=models.CASCADE)
    #p_glitches = models.ForeignKey(Inventoryis, on_delete=models.CASCADE)

