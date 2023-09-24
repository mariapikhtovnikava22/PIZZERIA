from django.urls import path, include

from .views import *

urlpatterns = [

    path('', main, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('personal_account/', personal_account, name='personal_account'),
    path('order/<int:order_id>/', showcart, name='order'),
    path('pizza/<int:pizza_id>/', pizza, name='pizza'),
    path('news', news, name='news'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', registration, name='registration'),
    path('cart/', cart, name='cart')
]
