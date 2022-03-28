from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/send', views.post_contact, name='post_contact'),
]
