
from django.contrib import admin
from django.urls import path, include
#from generator import hacks

from generator import main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('generator.urls')),
    path('api/v1/accounts', include('django.contrib.auth.urls')),

]
