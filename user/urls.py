from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('kullanici/',views.kullanicikayit,name = "kullanicikayit"),
    path('cihaz/',views.cihazkayit,name = "cihazkayit"),
    path('cihaztanim/',views.cihaztanim,name = "cihaztanim"),
    path('cihazliste/',views.cihazliste,name = "cihazliste"),
    path('cihazekle/',views.stokcihazekle,name = "cihazekle")

]