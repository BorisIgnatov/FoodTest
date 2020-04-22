# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path, include
from FoodApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('FoodApp.urls')),
    path('api/food/', views.FoodViewSet.as_view({'post':'create','get':'list'}), name='food'),
    path('api/chef/', views.ChefViewSet.as_view({'post':'create','get':'list'}), name='chef'),
    path('api/order/', views.OrderViewSet.as_view({'post':'create','get':'list'}), name='order'),
]
