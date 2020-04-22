from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from FoodApp.models import Food, Menu, Order, Chef

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email','password','name','location','card_number','phone_number','is_chef','current_money')
        extra_wkargs = {'password':{'write_only':True, 'min_length':5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        user = super().update(instance,validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

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
        fields = ('id','name','price','portion','products','time_of_cooking')
        read_only_fields = ('id',)


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ('user','rating','total_money')
        

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

