import stripe

from django.contrib import messages
from django.conf import settings
from .models import SPNAMember


def set_paid_until(request, charge):
    messages.info(request, f"set_paid_until with {charge}")

    stripe.api_key = settings.STRIPE_SECRET_KEY
    pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

    if pi.customer:
        customer = stripe.Customer.retrieve(pi.customer)
        email = customer.email

        if customer:
            subscr = stripe.Subscription.retrieve(
                customer['subscriptions'].data[0].id
            )
            current_period_end = subscr['current_period_end']

        try:
            user = SPNAMember.objects.get(email=email)
        except SPNAMember.DoesNotExist:
            messages.warning(
                request,
                f"User with email {email} not found"
            )
            return False

        user.set_paid_until(current_period_end)
        messages.info(
            request,
            f"Profile with {current_period_end} saved for user {email}"
        )
    else:
        pass
        # charge.amount  1990 | 19995
        # this was one time payment, update
        # paid_until (e.g. paid_until = current_date + 31 days) using
        # charge.paid + charge.amount attrs
