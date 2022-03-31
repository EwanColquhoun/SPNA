from django.urls import path
from . import views

urlpatterns = [
    path('', views.spna_admin, name='spna_admin'),
    path('delete/<article_id>', views.delete_article, name='delete_article'),
]
