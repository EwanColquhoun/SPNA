from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_area, name='member_area'),
    path('delete/<document_id>', views.delete_document, name='delete_document'),

]
