# Generated by Django 4.2.4 on 2023-09-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0011_remove_order_pizza_order_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('code', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('is_archived', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
