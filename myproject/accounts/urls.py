from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('create_profile/', views.profile_create_view, name='create_profile'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.documents, name='documents'),
]