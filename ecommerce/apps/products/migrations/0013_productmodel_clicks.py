# Generated by Django 3.1.14 on 2022-07-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_is_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='clicks',
            field=models.IntegerField(default=0, verbose_name='상품 모델 클릭수'),
        ),
    ]
