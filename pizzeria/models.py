from django.db import models
from django.utils import timezone

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Size(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'


class Client(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
        message="Phone number must be in the format: '+375 (29) XXX-XX-XX'")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, validators=[phone_regex], default='+375 (29) XXX-XX-XX')
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        ordering = ['phone']


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

    def get_absolute_url(self):
        return reverse('pizza', kwargs={'pizza_id': self.pk})


class Cart(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')

    def __str__(self):
        return f'Order №{self.pk}'

    def get_absolute_url(self):
        return reverse('cart', kwargs={'cart_id': self.pk})


class CartItem(models.Model):
    pizza = models.ForeignKey(PizzaType, on_delete=models.CASCADE)


class Order(models.Model):
    items = models.ManyToManyField(CartItem)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order №{self.pk}'

    def get_absolute_url(self):
        return reverse('order', kwargs={'order_id': self.pk})


class Promo(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="images/")
    code = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    is_archived = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def is_active(self):
        # Проверяем, активен ли промокод, сравнивая текущую дату с expiration_date
        return timezone.now() <= self.expiration_date


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/images/')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
