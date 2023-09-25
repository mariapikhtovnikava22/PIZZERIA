from django import forms
from .models import Review
from django.core import validators


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    text = forms.Textarea()

    class Meta:
        model = Review
        fields = ['rating', 'text']
