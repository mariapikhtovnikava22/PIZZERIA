from django.urls import path, include

from .views import *

urlpatterns = [

    path('', main, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('personal_account/', personal_account, name='personal_account'),
    path('pizza/<int:pizza_id>/', pizza, name='pizza'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', registration, name='registration'),
    path('cart/', cart, name='cart'),
    path('faq/', faq, name='faq'),
    path('reviews/', add_review, name='reviews'),
    path('news/', news_list, name='news_list'),
    path('news/<int:article_id>/', news_detail, name='news_detail'),
    path('infos', info, name='info'),
    path('test', test, name='tests'),
    path('check', check, name='check')

]
