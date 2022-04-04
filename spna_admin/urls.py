from django.urls import path
from . import views

urlpatterns = [
    path('', views.spna_admin, name='spna_admin'),
    path('delete/<article_id>', views.delete_article, name='delete_article'),
    path('edit/<article_id>', views.edit_article, name='edit_article'),
    path('add/article/', views.add_article, name='add_article'),
    path('add/document/', views.add_document, name='add_document'),
    path('send/', views.send_admin_email_view, name='send_email'),
]
