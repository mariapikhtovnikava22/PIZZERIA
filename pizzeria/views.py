from datetime import date, timedelta

import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from django import forms

menu = [{'title': 'Pizza', 'url_name': 'pizza'},
        {'title': 'News', 'url_name': 'news'},
        {'title': 'Promo codes and promotions', 'url_name': 'Promocode'},
        {'title': "Cart", "url_name": "order"},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        # {'title': 'About us', 'url_name': 'about'},
        ]


def main(request):
    if request.method == 'GET':
        pizzas = PizzaType.objects.all()
        pizzas_names = {pizza.name for pizza in pizzas}
        p = [pizzas.filter(name=pname) for pname in pizzas_names]
        size = Size.objects.all()

        count = 0
        if request.user.is_authenticated and Client.objects.filter(user=request.user).exists():
            client = Client.objects.filter(user=request.user).first()
            cart_ = Cart.objects.filter(user=client).first()
            if not cart_.pizza:
                count = 0
            else:
                count = cart_.pizza.count()

        context = {"pizzas": pizzas,
                   'pizzass': p,
                   'menu': menu,
                   'size': size,
                   'count': count }

        return render(request, 'pizzeria/main.html', context=context)

    if request.method == 'POST':
        form = request.POST

        client = Client.objects.filter(user=request.user).first()
        cart_ = Cart.objects.filter(user=client).first()
        pizza_ = PizzaType.objects.filter(name=form['pizza_name'], price=float(form['size'].replace(',', '.'))).first()
        cart_.pizza.add(pizza_)
        cart_.save()

        return redirect('home')


def pizza(request, pizza_id):
    pizzas = PizzaType.objects.filter(size__name='small')
    size = Size.objects.all()

    context = {"pizzas": pizzas,
               'menu': menu,
               'size': size}

    return render(request, 'pizzeria/main.html', context=context)


def about(request):
    return HttpResponse("About")


def news(request):
    return HttpResponse('News')


def contacts(request):
    return HttpResponse("Contacts")


def personal_account(request):
    return render(request, 'pizzeria/personal.html')


def showcart(request, order_id):
    return HttpResponse(f"Cart for order #{order_id}")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# def get_weather():
#     appid = '91d45fb3f775b8f850579a41205a2a39'
#     url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
#
#     city = 'Minsk'
#     res = requests.get(url.format(city)).json()
#
#     return res["main"]["temp"]


class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
                message='Invalid phone number.'
            )
        ],
        required=True
    )
    address = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            client = Client.objects.create(user=user,
                                           address=request.POST.get('address'),
                                           phone=request.POST.get('phone_number'))
            client.save()

            cart_ = Cart.objects.create(user=user, pizza=list())
            cart_.save()

            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def cart(request):
    client = Client.objects.filter(user=request.user).first()
    cart_ = Cart.objects.filter(user=client).first()
    pizza_ = cart_.pizza.all()

    context = {"pizza_list": pizza_ }

    return render(request, 'pizzeria/cart.html', context=context)
