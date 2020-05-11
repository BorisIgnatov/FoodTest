from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from FoodApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('FoodApp.urls')),
    path('api/food/', views.FoodViewSet.as_view({'post':'create','get':'list'}), name='food'),
    path('api/chef/', views.ChefViewSet.as_view({'post':'create','get':'list'}), name='chef'),
    path('api/order/user', views.UsersOrderViewSet.as_view({'post':'create','get':'list'}), name='order'),
    path('api/order/birzha', views.OrderViewSet.as_view({'get':'list'}), name='order'),
    url(r'^api/order/setchef/(?P<pk>\d+)/$', views.OrderSetChefVeiwSet.as_view()),
    path('api/token/', include('django_expiring_token.urls')),
    path('api/menu/', views.MenuViewSet.as_view({'post':'create','get':'list'}),name='menu'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
