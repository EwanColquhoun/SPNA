import stripe
from django.contrib.auth.models import User

from django.contrib import messages
from django.conf import settings
from .models import SPNAMember


def set_paid_until(request, charge):
    """
    Updates the spnamember model with a new paid until value.
    """
    print('setpaid until')

    messages.info(request, f"set_paid_until with {charge}")

    stripe.api_key = settings.STRIPE_SECRET_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    print(pi.customer, 'picustomer')
    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email
        print(customer, 'customer')
        if customer:
            sub = stripe.Subscription.list(limit=1, customer=customer.id)
            # subscr = stripe.Subscription.retrieve(
            #      customer['subscription'].data[0].id
            # )
            # print(subscr, 'subcr')
            current_period_end = sub.data[0]['current_period_end']
            print(current_period_end, 'sub')

        try:
            user = User.objects.get(email=email)
            print(user, 'user')
        except Exception as e:
          
            print('except no user')
            return False

        user.spnamember.set_paid_until(current_period_end)
        messages.info(
            request,
            f"Profile with {current_period_end} saved for user {email}"
        )
    else:
        pass
