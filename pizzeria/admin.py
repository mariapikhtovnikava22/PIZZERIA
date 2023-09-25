from django.contrib import admin
from .models import PizzaType, Order, Client, Courier, Size, State, Cart, Promo, Review, FAQ, Article


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['state', 'client', 'courier', 'created']
    list_filter = ['state']


@admin.register(PizzaType)
class PizzaTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'slug')
    list_filter = ['size', 'name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address']


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_archived', 'expiration_date', 'code']


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
    list_display = ['user']


@admin.register(Review)
class RewievAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'date']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'date_added']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
