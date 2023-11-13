from datetime import date, timedelta

import requests
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReviewForm, CustomUserChangeForm
from .models import *
from django import forms
from django.http import HttpResponseRedirect
from django.db import transaction

from plotly.graph_objs import Figure, Layout, Bar

menu = [{'title': 'Pizza', 'url_name': 'pizza'},
        {'title': 'News', 'url_name': 'news_list'},
        {'title': "Reviews", "url_name": "reviews"},
        {'title': 'Promo codes and promotions', 'url_name': 'Promocode'},
        {'title': "Cart", "url_name": "order"},
        ]


def test(request):
    return render(request, 'pizzeria/test.html')

def main(request):
    if request.method == 'GET':

        pizzas = PizzaType.objects.all()
        pizzas_names = {pizza.name for pizza in pizzas}
        p = [pizzas.filter(name=pname) for pname in pizzas_names]
        size = Size.objects.all()
        promo_list = Promo.objects.all()

        count = 0
        if request.user.is_authenticated and Client.objects.filter(user=request.user).exists():
            client = Client.objects.filter(user=request.user).first()
            cart_ = Cart.objects.filter(user=client).first()
            if not cart_.items:
                count = 0
            else:
                count = cart_.items.count()

        context = {"pizzas": pizzas,
                   'pizzass': p,
                   'menu': menu,
                   'size': size,
                   'count': count,
                   'promo': promo_list}

        return render(request, 'pizzeria/main.html', context=context)

    if request.method == 'POST':
        form = request.POST

        client = Client.objects.filter(user=request.user).first()
        cart_ = Cart.objects.filter(user=client).first()
        pizza_ = PizzaType.objects.filter(name=form['pizza_name'], price=float(form['size'].replace(',', '.'))).first()
        cart_item = CartItem.objects.create(pizza=pizza_)
        cart_.items.add(cart_item)
        cart_.save()

        return HttpResponseRedirect(request.path_info)


def faq(request):
    return render(request, 'pizzeria/faq.html')


def info(request):
    # static_info
    pizza_count = PizzaType.objects.all().count()
    orders_count = Order.objects.all().count()
    couriers_count = Courier.objects.all().count()

    orders = list(Order.objects.all())
    pizza = dict()
    for order in orders:
        for item in list(order.items.all()):
            if item.pizza in pizza:
                pizza[item.pizza] += 1
            else:
                pizza[item.pizza] = 1
    popular_pizza = max(pizza, key=pizza.get)
    pizza_counts = list(pizza.values())
    pizza_types = [str(pizza_) for pizza_ in pizza.keys()]
    data = Bar(x=pizza_types, y=pizza_counts)
    layout = Layout(title='Popular pizza',
                    xaxis=dict(title='pizza types'),
                    yaxis=dict(title='pizza counts'))
    fig = Figure(data=data, layout=layout)
    plot_div = fig.to_html(full_html=False)

    context = {
        'pizza_count': pizza_count,
        'orders_count': orders_count,
        'couriers_count': couriers_count,
        'popular_pizza': popular_pizza,
        'plot_div': plot_div
    }
    return render(request, 'pizzeria/info.html', context=context)


def add_review(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('reviews')
        else:
            return redirect('login')
    else:
        form = ReviewForm()
    if len(reviews):
        context = {
            'form': form,
            'reviews': reviews,
        }
    else:
        context = {
            'form': form,
        }
    return render(request, 'pizzeria/reviews.html', context=context)


def news_list(request):
    articles = Article.objects.all()
    return render(request, 'pizzeria/news_list.html', {'articles': articles})


def news_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'pizzeria/news_detail.html', {'article': article})


def cart(request):
    if request.method == 'GET':
        client = Client.objects.filter(user=request.user).first()
        cart_ = Cart.objects.filter(user=client).first()
        pizza_ = cart_.items.all()

        context = {"pizza_list": pizza_}

        return render(request, 'pizzeria/cart.html', context=context)

    if request.method == 'POST':
        form = request.POST
        if form.get('order'):
            with transaction.atomic():
                client = Client.objects.filter(user=request.user).first()
                cart_ = Cart.objects.filter(user=client).first()
                items = cart_.items.all()
                state = State.objects.filter(name='accepted').first()

                courier = Courier.objects.all()
                count = {}
                for c in courier:
                    count[c.id] = len(c.order_set.all())

                min_courier = min(count.items(), key=lambda item: item[1])[0]

                order = Order.objects.create(client=client, state=state, courier_id=min_courier)
                for p in items:
                    order.items.add(p.id)
                cart_.items.clear()
                return redirect('home')
        else:
            client = Client.objects.filter(user=request.user).first()
            cart_ = Cart.objects.filter(user=client).first()
            item_ = CartItem.objects.filter(id=form['item_id']).first()
            cart_.items.remove(item_)
            cart_.save()

            return HttpResponseRedirect(request.path_info)


def personal_account(request):

    if request.method == 'GET':
        user = CustomUserChangeForm(instance=request.user)
        order_ = Order.objects.all()
        total_price = 0

        for order in order_:
            pizza_ids = order.items.values_list('pizza', flat=True)

            pizzas_in_order = PizzaType.objects.filter(id__in=pizza_ids)

            order_price = sum(pizza.price for pizza in pizzas_in_order)

            total_price += order_price

        context = {"order_list": order_, "total_price": total_price, 'form': user}

        return render(request, 'pizzeria/personal.html', context=context)

    if request.method == 'POST':
        form = request.POST
        if form.get('save'):
            user_form = CustomUserChangeForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user = user_form.save()
                client, created = Client.objects.get_or_create(user=user)
                client.address = request.POST.get('address')
                client.phone = request.POST.get('phone')
                client.save()

                try:
                    cart_ = Cart.objects.get(user=client)
                except Cart.DoesNotExist:
                    cart_ = Cart.objects.create(user=client)
                cart_.save()

                login(request, user)
                update_session_auth_hash(request, user)

            return redirect('home')
        else:
            print(form.get)
            print('j')
            item_id = form.get('item_id')
            client = get_object_or_404(Client, user=request.user)
            order = get_object_or_404(Order, id=item_id, client=client)
            order.delete()

            return HttpResponseRedirect(request.path_info)


def pizza(request, pizza_id):
    pizzas = PizzaType.objects.filter(size__name='small')
    size = Size.objects.all()

    context = {"pizzas": pizzas,
               'menu': menu,
               'size': size}

    return render(request, 'pizzeria/main.html', context=context)


def about(request):
    return render(request, 'pizzeria/about.html')


def news(request):
    return HttpResponse('News')


def contacts(request):
    return HttpResponse("Contacts")


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

            cart_ = Cart.objects.create(user=client)
            cart_.save()

            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})
