from django.contrib import admin
from .models import PizzaType, Order, Client, Courier, Size, State


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['state', 'client', 'courier', 'slug', 'created']
    list_filter = ['state']


@admin.register(PizzaType)
class PizzaTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'size', 'slug']
    list_filter = ['size', 'name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address']


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'diameter']


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
