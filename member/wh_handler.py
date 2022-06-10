import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

from spna.email import cancel_email, cancel_email_to_member

import stripe


def wh_set_paid_until(request, charge):
    """
    Updates the spnamember model with a new paid until value.
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email
        if customer:
            sub = stripe.Subscription.list(limit=1, customer=customer.id)
            current_period_end = sub.data[0]['current_period_end']

        try:
            user = User.objects.get(email=email)
        except RuntimeError as err:
          
            messages.error(request, f'No User with name {user.spnamember.fullname}. Error:{err}. Please contact Admin.')
            return False

        user.spnamember.set_paid_until(current_period_end)
        user.spnamember.has_paid(current_date=datetime.date.today())
   
    else:
        messages.error(request, 'No customer with this payment intent exists. Please contact Admin.')


def update_paid_until(request, event):
    """Updates the paid until date when the subscription is changed."""
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    sub = stripe.Subscription.retrieve(event.id)
    cust = sub.customer
    expiry = sub.current_period_end

    if cust:
        customer = stripe.Customer.retrieve(cust)
        email = customer.email
        if customer:
            try:
                user = User.objects.get(email=email)
                user.spnamember.set_paid_until(expiry)
            except RuntimeError as err:
            
                messages.error(request, f'No User with name {user.spnamember.fullname}. Error:{err}. Please contact Admin.')
                return False
    else:
        messages.error(request, 'No customer with this subscription exists. Please contact Admin.')

def sub_cancelled(request, charge):
    """Changes the 'paid' option of the SPNA member when subscription is deleted."""

    stripe.api_key = settings.STRIPE_SECRET_KEY
    cust = stripe.PaymentIntent.retrieve(charge.customer)

    if cust:
        customer = stripe.Customer.retrieve(cust)
        email = customer.email
        if customer:
            try:
                user = User.objects.get(email=email)
            except RuntimeError as err:
            
                messages.error(request, f'No User with name {user.spnamember.fullname}. Error:{err}. Please contact Admin.')
                return False

        user.spnamember.paid=False
        cancel_email(request.user)
        cancel_email_to_member(request.user)

    else:
        messages.error(request, 'No customer with this subscription exists. Please contact Admin.')
