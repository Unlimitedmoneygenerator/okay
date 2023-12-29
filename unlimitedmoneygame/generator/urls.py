from django.urls import path, include

from generator import views

from .views import get_stripe_pub_key, create_checkout_session,stripe_webhook

urlpatterns = [
    path('orders/', views.search),
    path('ordersplace/', views.orders),
    path('wonplace/', views.won),
    path('tradeplace/', views.moderntrade),
    path('sendtrade/', views.sendtrade),
    path('tradeaccept/', views.acceptrade),
    path('donate/', views.donate),
    path('playersearch/', views.playersearch),
    path('inventorysearch/', views.tradeshowinventory),
    path('myotherguy/', views.tradeshowothersinventory),
    path('sendinventoryitem/', views.sendinventoryitem),
    path('deleteitems/', views.deletemyitems), 
    path('Acceptradepart/', views.ACCEPTMYPART), 
    path('GetUser/', views.get_USER), 
    path('showactivated/', views.showactrade),
    path('FL/', views.FL),
    path('invoice/', views.invoice),
    path('mydata/', views.GETMYINVOICE),
    path('stripe/get_stripe_pub_key/', get_stripe_pub_key, name='get_stripe_pub_key'),
    path('POSTCHAT/', views.chat),
    path('Donate/', views.GETMYKEY),
    path('GETMYKEYS/', views.GETMYKEYS),
    path('stripe/create_checkout_session/', create_checkout_session, name=" create_checkout_session"),
    path('stripe/webhook/', stripe_webhook, name='stripe_webhook')

    







]