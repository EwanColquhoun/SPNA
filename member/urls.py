from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_area, name='member_area'),
]
