from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from FoodApp.models import Food, Menu, Order, Chef
from django.core.mail import send_mail
import random


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','name','location','card_number','phone_number','is_chef','is_first','current_money')

    def create(self, validated_data):
        code = random.randint(10000,99999)
        send_mail(
            'Hello from FoodLink',
            'To sign in your account use this code:\n'+str(code),
            'boris.ignatov.99@gmail.com',
            [validated_data['email']],
            fail_silently=False,)
        validated_data['password'] = code
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        user = super().update(instance,validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class CheckEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email',)


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )   

    def validate(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentionals')
            raise serializers.ValidationError(msg,code='authentication')
        
        attrs['user'] = user
        return attrs


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id','name','price','portion','products','time_of_cooking','image')
        read_only_fields = ('id',)


class ChefSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(many=False,queryset=Menu.objects.all())
    class Meta:
        model = Chef
        fields = ('user','rating','total_money','menu')
        

class OrderSerializer(serializers.ModelSerializer):
    foods = serializers.PrimaryKeyRelatedField(many=True,queryset=Food.objects.all())
    chef = serializers.PrimaryKeyRelatedField(many=True,queryset=Chef.objects.all())

    class Meta:
        model = Order
        fields = ('id','status','time','foods','chef')
        read_only_fields = ('id',)


class OrderDetailsSerializer(OrderSerializer):
    foods = FoodSerializer(many=True,read_only=True)
    chef = ChefSerializer(many=True,read_only=True)


class OrderSetChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','chef')
        read_only_fields = ('id',)

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id','foods')

class MenuDetailSerializer(MenuSerializer):
    foods = FoodSerializer(many=True,read_only=False)


