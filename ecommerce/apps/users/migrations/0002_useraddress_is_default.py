# Generated by Django 3.1.14 on 2022-07-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='is_default',
            field=models.BooleanField(default=True, verbose_name='기본 배송지'),
        ),
    ]