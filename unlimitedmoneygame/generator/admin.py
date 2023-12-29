from django.contrib import admin

# Register your models here.


from .models import User,glitch, Playing, Game, APIKEY, DeletedInvoice,Invoice,KeySeed,Modifiers,black, Money, PlayingMode, Ticket, Level, Market, Trade, Chat,Messages,Slot,Inventory,Luck,TradeSpace,LuckCalc



admin.site.register(glitch)
admin.site.register(Playing)
admin.site.register(Game)
admin.site.register(Modifiers)
admin.site.register(black)
admin.site.register(Money)
admin.site.register(PlayingMode)
admin.site.register(Ticket)
admin.site.register(Market)
admin.site.register(Level)
admin.site.register(Trade)
admin.site.register(Chat)
admin.site.register(Messages)
admin.site.register(Inventory)
admin.site.register(Slot)
admin.site.register(Luck)
admin.site.register(TradeSpace)
admin.site.register(LuckCalc)
admin.site.register(User)
admin.site.register(KeySeed)
admin.site.register(Invoice)
admin.site.register(DeletedInvoice)
admin.site.register(APIKEY)