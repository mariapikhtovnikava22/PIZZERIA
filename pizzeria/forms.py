from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Review
from django.core import validators


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    text = forms.Textarea()

    class Meta:
        model = Review
        fields = ['rating', 'text']


class CustomUserChangeForm(UserChangeForm):
    phone = forms.CharField(max_length=20, required=True,
                            widget=forms.TextInput(attrs={'placeholder': '+375 (29) XXX-XX-XX'}))
    address = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address']
