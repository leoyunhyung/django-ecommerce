# Generated by Django 3.1.14 on 2022-07-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_productmodel_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='clicks',
            field=models.IntegerField(default=0, verbose_name='์กฐํ์'),
        ),
    ]
