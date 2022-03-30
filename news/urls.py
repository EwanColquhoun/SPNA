from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_view, name='news'),
    path('initiatives/', views.initiatives_view, name='initiatives'),
]
