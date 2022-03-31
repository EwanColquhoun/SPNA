from django.urls import path
from . import views

urlpatterns = [
    path('', views.spna_admin, name='spna_admin'),
    path('delete/<article_id>', views.delete_article, name='delete_article'),
    path('edit/<article_id>', views.edit_article, name='edit_article'),
    path('add/', views.add_article, name='add_article'),
]
