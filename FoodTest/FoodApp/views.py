from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, authentication, permissions, viewsets, mixins, status
import django_expiring_token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from FoodApp import serializers
from FoodApp.models import Food, Chef, Menu, Order, User

class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    authentication_classes = (django_expiring_token.authentication.ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class CheckEmailView(viewsets.ModelViewSet):
    serializer_class = serializers.CheckEmailSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        email = self.request.query_params.get('email',None)
        return self.queryset.filter(email=email)


class FoodViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    authentication_classes = (django_expiring_token.authentication.ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Food.objects.all()
    serializer_class = serializers.FoodSerializer

    def get_queryset(self):
        return self.queryset

    def perform_create(self,serializer):
        serializer.save()


class ChefViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin):
    authentication_classes = (django_expiring_token.authentication.ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Chef.objects.all()
    serializer_class = serializers.ChefSerializer

    def get_queryset(self):
        return self.queryset

    def perform_create(self,serializer):
        serializer.save()


class UsersOrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = (django_expiring_token.authentication.ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.OrderDetailsSerializer
        return self.serializer_class

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    authentication_classes = (django_expiring_token.authentication.ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(chef=None)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.OrderDetailsSerializer
        return self.serializer_class


class OrderSetChefVeiwSet(generics.UpdateAPIView):
    serializer_class = serializers.OrderSetChefSerializer
    queryset = Order.objects.all()
    authentication_classes = (django_expiring_token.authentication.ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class MenuViewSet(viewsets.ModelViewSet)   :
    serializer_class = serializers.MenuSerializer
    queryset = Menu.objects.all()
    authentication_classes = (django_expiring_token.authentication.ExpiringTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
