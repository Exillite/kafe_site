# Generated by Django 3.2.14 on 2022-07-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafe', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sales',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]
