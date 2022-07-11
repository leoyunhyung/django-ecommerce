# Generated by Django 3.1.14 on 2022-07-11 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ecommerce.bases.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='활성화 여부')),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
                ('description', models.CharField(max_length=100, verbose_name='설명')),
                ('discount_price', models.IntegerField(blank=True, null=True, verbose_name='할인 금액')),
                ('discount_rate', models.IntegerField(blank=True, null=True, verbose_name='할인율')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to=settings.AUTH_USER_MODEL, verbose_name='유저')),
            ],
            options={
                'verbose_name': '쿠폰',
                'verbose_name_plural': '쿠폰',
            },
            bases=(ecommerce.bases.models.UpdateMixin, models.Model),
        ),
    ]
