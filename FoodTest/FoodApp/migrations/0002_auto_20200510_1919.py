# Generated by Django 3.0.4 on 2020-05-10 13:19

import FoodApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rating', models.FloatField(blank=True, default=0)),
                ('total_money', models.FloatField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('portion', models.CharField(max_length=255)),
                ('products', models.CharField(max_length=255)),
                ('time_of_cooking', models.TimeField()),
                ('image', models.ImageField(null=True, upload_to=FoodApp.models.food_image_path_file)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_first',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=255)),
                ('total_price', models.FloatField(default=1000.0)),
                ('time', models.TimeField(default='01:00')),
                ('chef', models.ManyToManyField(to='FoodApp.Chef')),
                ('foods', models.ManyToManyField(to='FoodApp.Food')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foods', models.ManyToManyField(to='FoodApp.Food')),
            ],
        ),
        migrations.AddField(
            model_name='chef',
            name='menu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FoodApp.Menu'),
        ),
    ]
