# Generated by Django 3.0.4 on 2020-04-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_chef_food_menu_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='rating',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='chef',
            name='total_money',
            field=models.FloatField(blank=True),
        ),
    ]
