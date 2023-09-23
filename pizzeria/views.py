from datetime import date, timedelta

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

menu = [{'title': 'Pizza', 'url_name': 'pizza'},
        {'title': 'News', 'url_name': 'news'},
        {'title': 'Promo codes and promotions', 'url_name': 'Promocode'},
        {'title': "Cart", "url_name": "cart"},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        ]


def main(request):
    pizzas = PizzaType.objects.all()
    weather = get_weather()

    filtered_pizzas = []

    for pizza in pizzas:
        if pizza.size.name == 'middle':
            filtered_pizzas.append(pizza)

    context = {"pizzas": filtered_pizzas,
               'weather': weather,
               'menu': menu, }

    return render(request, 'pizzeria/main.html', context=context)


def get_weather():
    appid = '91d45fb3f775b8f850579a41205a2a39'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()

    return res["main"]["temp"]


def about(request):
    return HttpResponse("About")


def pizza(request):
    return HttpResponse('Pizza')


def news(request):
    return HttpResponse('News')


def contacts(request):
    return HttpResponse("Contacts")


def logIn(request):
    return HttpResponse("LogIn")


def cart(request):
    return HttpResponse("cart")
