from django.urls import path
from .webhooks import webhook
# from .views import CustomSignUpView

from . import views

urlpatterns = [
    path('', views.member_area, name='member_area_page'),

    path('subscribe/', views.subscribe, name='subscribe'),
    path('payment/', views.payment, name='payment'),

    path('3dsec/', views.secure, name='3dsec'),
    path('stripe-webhooks/', webhook, name='webhook'),
    path('profile/', views.profile_view, name='profile_page'),
    path('cancel/', views.cancel_subscription, name='cancel_subscription'),
    path('renew/', views.renew_subscription, name='renew'),
    path('upgrade/', views.upgrade_subscription, name='upgrade'),
    path('update_payment_method/', views.update_payment_method, name='update_payment_method'),
    path('login/', views.member_login, name='member_login'),
]
