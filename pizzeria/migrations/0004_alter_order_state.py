# Generated by Django 4.2.4 on 2023-09-12 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0003_alter_order_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='pizzeria.state'),
        ),
    ]
