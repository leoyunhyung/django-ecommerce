# Generated by Django 3.1.14 on 2022-07-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20220712_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='사이즈'),
        ),
    ]
