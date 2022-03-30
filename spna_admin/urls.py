from django.urls import path
from . import views

urlpatterns = [
    path('', views.spna_admin, name='spna_admin'),
]
