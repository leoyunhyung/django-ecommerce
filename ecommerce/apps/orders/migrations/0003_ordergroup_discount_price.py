# Generated by Django 3.1.14 on 2022-07-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergroup',
            name='discount_price',
            field=models.IntegerField(default=0, verbose_name='할인 금액'),
        ),
    ]