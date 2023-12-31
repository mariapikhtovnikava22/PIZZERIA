# Generated by Django 4.2.4 on 2023-09-24 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0006_alter_order_client_alter_order_courier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.ManyToManyField(to='pizzeria.pizzatype')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pizzeria.client')),
            ],
        ),
    ]
