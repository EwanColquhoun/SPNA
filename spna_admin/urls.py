from django.urls import path
from . import views

urlpatterns = [
    path('', views.spna_admin, name='spna_admin'),
    path('delete/article/<article_id>', views.delete_article, name='delete_article'),
    path('delete/contact/<contact_id>', views.delete_contact, name='delete_contact'),
    path('delete/document/<doc_id>', views.delete_document, name='delete_document'),
    path('edit/<article_id>', views.edit_article, name='edit_article'),
    path('add/article/', views.add_article, name='add_article'),
    path('add/document/', views.add_document, name='add_document'),
    path('send/', views.send_admin_email_view, name='send_email'),
    path('csv/', views.get_csv_of_users, name='get_csv'),
]
