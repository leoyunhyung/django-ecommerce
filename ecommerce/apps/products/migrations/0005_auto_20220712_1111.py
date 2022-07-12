# Generated by Django 3.1.14 on 2022-07-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220711_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='options',
            field=models.IntegerField(blank=True, null=True, verbose_name='옵션'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='수량'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='discount_rate',
            field=models.IntegerField(blank=True, null=True, verbose_name='할인율'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='low_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='최저가'),
        ),
    ]
