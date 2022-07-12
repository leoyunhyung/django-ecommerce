# Generated by Django 3.1.14 on 2022-07-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220711_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='discount_rate',
            field=models.IntegerField(default=0, verbose_name='할인율'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='low_price',
            field=models.IntegerField(default=0, verbose_name='최저가'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='release_price',
            field=models.IntegerField(verbose_name='출시가'),
        ),
    ]
