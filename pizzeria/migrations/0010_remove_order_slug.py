# Generated by Django 4.2.4 on 2023-09-24 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0009_alter_cartitem_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
    ]
