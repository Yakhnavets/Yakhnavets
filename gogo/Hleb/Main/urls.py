from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index),
    path('about', views.about),
    path ('galery', views.galery),
    path ('contacts', views.contacts),
    path ('login', views.login),
    
    ]