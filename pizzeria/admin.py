from django.contrib import admin
from .models import PizzaType, Order, Client, Courier, Size, State, Cart


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['state', 'client', 'courier', 'slug', 'created']
    list_filter = ['state']

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(PizzaType)
class PizzaTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'slug')
    list_filter = ['size', 'name']
    prepopulated_fields = {'slug': ('name',)}


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


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [ 'user']
