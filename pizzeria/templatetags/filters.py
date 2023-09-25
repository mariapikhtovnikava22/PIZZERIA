from django import template
from ..models import Client, PizzaType

register = template.Library()


@register.filter(name='is_client')
def is_client(user):
    if not user.is_authenticated:
        return False
    return Client.objects.filter(user=user).exists()


@register.filter
def total_price(pizza_list):
    total = sum(item.pizza.price for item in pizza_list)
    return total


@register.filter
def calculate_total_price(order_list):
    total_price = 0
    for order in order_list:
        pizza_ids = order.items.values_list('pizza', flat=True)
        pizzas_in_order = PizzaType.objects.filter(id__in=pizza_ids)
        order_price = sum(pizza.price for pizza in pizzas_in_order)
        total_price += order_price
    return total_price


@register.filter
def actual_promo(promo_list):
    promo = []
    for i in promo_list:
        if i.is_active():
            promo.append(i)
    return promo
