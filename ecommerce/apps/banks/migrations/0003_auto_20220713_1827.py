# Generated by Django 3.1.14 on 2022-07-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_auto_20220713_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account',
            field=models.CharField(max_length=100, verbose_name='계좌'),
        ),
    ]
