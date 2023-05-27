from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='app'),
    path("about", views.services, name='about'),
]  