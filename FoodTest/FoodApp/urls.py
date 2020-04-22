from django.urls import path
from FoodApp import views

app_name = 'FoodApp'

urlpatterns = [
    path('create/',views.CreateUserView.as_view(), name='create'),
    path('token/',views.CreateTokenView.as_view(), name='token'),
    path('me/',views.ManageUserView.as_view(), name='me'),
]
