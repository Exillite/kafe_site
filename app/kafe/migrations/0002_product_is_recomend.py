# Generated by Django 3.2.14 on 2022-08-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_recomend',
            field=models.BooleanField(default=False, verbose_name='Рекомендовать в корзине'),
        ),
    ]
