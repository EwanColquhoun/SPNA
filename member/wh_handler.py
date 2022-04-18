import stripe
import datetime
from django.contrib.auth.models import User

from django.contrib import messages
from django.conf import settings
from .models import SPNAMember


def set_paid_until(request, charge):
    """
    Updates the spnamember model with a new paid until value.
    """
    # print('setpaid until')

    stripe.api_key = settings.STRIPE_SECRET_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    # print(pi.customer, 'picustomer')
    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email
        # print(customer, 'customer')
        if customer:
            sub = stripe.Subscription.list(limit=1, customer=customer.id)
            # subscr = stripe.Subscription.retrieve(
            #      customer['subscription'].data[0].id
            # )
            # print(subscr, 'subcr')
            current_period_end = sub.data[0]['current_period_end']
            # print(current_period_end, 'sub')

        try:
            user = User.objects.get(email=email)
            # print(user, 'user')
        except Exception as e:
          
            messages.error(request, f'No User with name {user.spnamember.fullname}. Error:{e}. Please contact Admin.')
            return False

        user.spnamember.set_paid_until(current_period_end)
        user.spnamember.has_paid(current_date=datetime.date.today())
   
    else:
        messages.error(request, 'No customer with this payment intent exists. Please contact Admin.')
