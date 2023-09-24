from django import template
from ..models import Client


register = template.Library()


@register.filter(name='is_client')
def is_client(user):
    if not user.is_authenticated:
        return False
    return Client.objects.filter(user=user).exists()
