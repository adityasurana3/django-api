"""
URL configuration for drfproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductListAPIView.as_view()),
    path('products/info/', views.product_info),
    path('orders/', views.OrderListAPIView.as_view()),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-orders'),
    path('products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_list'),
]
