from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),

    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),

    # Profile
    path('profile/', views.profile, name='profile'),

    # Middleware test
    path('request-time/', views.request_time, name='request_time'),
]
