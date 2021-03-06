# Generated by Django 3.1.14 on 2022-07-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20220713_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordergroup',
            name='is_agreement',
        ),
        migrations.RemoveField(
            model_name='ordergroup',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='order',
            name='is_agreement',
            field=models.BooleanField(default=True, verbose_name='주문 동의'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('CARD', '카드'), ('ACCOUNT', '계좌 이체'), ('KAKAO', '카카오 페이')], default='CARD', max_length=100, verbose_name='결제 방법'),
            preserve_default=False,
        ),
    ]
