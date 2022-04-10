from django.urls import path
from .webhooks import webhook
# from .views import CustomSignUpView

from . import views

urlpatterns = [
    path('', views.member_area, name='member_area'),
    path('delete/<document_id>', views.delete_document, name='delete_document'),
    # path('signup/', views.custom_signup_view, name='signup'),
    # path('accounts/signup/', CustomSignUpView.as_view(), name='account_signup'),
    path('signup/', views.membership, name='membership'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('card/', views.card, name='card'),
    path('stripe-webhooks/', webhook, name='webhook'),
]
