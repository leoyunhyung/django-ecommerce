# Generated by Django 3.1.14 on 2022-07-13 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0001_initial'),
        ('orders', '0007_auto_20220713_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_agreement',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='ordergroup',
            name='delivery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_groups', to='deliveries.delivery', verbose_name='배송 정보'),
        ),
        migrations.AddField(
            model_name='ordergroup',
            name='is_agreement',
            field=models.BooleanField(default=True, verbose_name='주문 동의'),
        ),
        migrations.AddField(
            model_name='ordergroup',
            name='payment_type',
            field=models.CharField(choices=[('CARD', '카드'), ('ACCOUNT', '계좌 이체'), ('KAKAO', '카카오 페이')], default='CARD', max_length=100, verbose_name='결제 방법'),
            preserve_default=False,
        ),
    ]