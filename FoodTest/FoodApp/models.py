import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


def food_image_path_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/food/',filename)


class UserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('no email address')
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255,null=True)
    card_number = models.CharField(max_length=19,null=True)
    phone_number = models.CharField(max_length=12,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)
    is_first = models.BooleanField(default=True)
    code = models.CharField(max_length=4,null=True)
    current_money = models.FloatField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    portion = models.CharField(max_length=255)
    products = models.CharField(max_length=255)
    time_of_cooking = models.TimeField()
    image = models.ImageField(null=True, upload_to=food_image_path_file)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    status = models.CharField(max_length=255,blank=True)
    total_price = models.FloatField(default=1000.)
    time = models.TimeField(default='01:00')
    foods = models.ManyToManyField('Food')
    chef = models.ManyToManyField('Chef')


class Chef(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    rating = models.FloatField(blank=True, default=0)
    total_money = models.FloatField(blank=True,default=0)
    menu= models.OneToOneField('Menu', on_delete=models.CASCADE,null=True,blank=True)


class Menu(models.Model):
    foods = models.ManyToManyField('Food')
    #chef = models.OneToOneField('Chef', on_delete=models.CASCADE,primary_key=True, blank=True)

