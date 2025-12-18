from django.contrib import admin
from django.urls import path
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about_us/', views.about_us, name='about_us'),
    path('our_services/', views.our_services, name='our_services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('register/', views.register, name='register'),
    path('userform/', views.userform, name='userform'),
]
