from django.db import models

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class Size(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.DecimalField(max_digits=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Courier:
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Client:
    phone_regex = RegexValidator(
        regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
        message="Phone number must be in the format: '+375 (29) XXX-XX-XX'")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, validators=[phone_regex], default='+375 (29) XXX-XX-XX')
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class PizzaType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Order:
    pizza = models.ForeignKey(PizzaType, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order #{self.pk}'
