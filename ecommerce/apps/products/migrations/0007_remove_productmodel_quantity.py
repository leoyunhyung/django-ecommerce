# Generated by Django 3.1.14 on 2022-07-12 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220712_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='quantity',
        ),
    ]
