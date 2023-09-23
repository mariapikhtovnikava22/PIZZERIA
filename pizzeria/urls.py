from django.urls import path, include

from .views import *

urlpatterns = [

    path('', main, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('logIn/', logIn, name='logIn'),
    path('cart', cart, name='cart'),
    path('pizza', pizza, name='pizza'),
    path('news', news, name='news')



]
