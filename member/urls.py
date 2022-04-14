from django.urls import path
from .webhooks import webhook
# from .views import CustomSignUpView

from . import views

urlpatterns = [
    path('', views.member_area, name='member_area'),
    path('delete/<document_id>', views.delete_document, name='delete_document'),
    # path('signup/', views.custom_signup_view, name='signup'),
    # path('accounts/signup/', CustomSignUpView.as_view(), name='account_signup'),
    # path('signup/', views.membership, name='membership'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('payment/', views.payment, name='payment'),
    # path('card/', views.card, name='card'),
    path('3dsec/', views.secure, name='3dsec'),
    path('stripe-webhooks/', webhook, name='webhook'),
    path('profile/', views.profile_view, name='profile'),
    path('cancel/', views.cancel_subscription, name='cancel_subscription'),
    # path('payment_failed/', views.payment_failed, name='payment_failed'),
]
