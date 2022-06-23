import json
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse

import stripe

from .wh_handler import (
    wh_set_paid_until,
    sub_cancelled,
    update_paid_until,
    failed_payment)

stripe_secret_key = settings.STRIPE_SECRET_KEY
stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
endpoint_secret = settings.STRIPE_WEBHOOK_SIGNING_KEY


# Modified from stripe.com
@require_POST
@csrf_exempt
def webhook(request):
    """
    Handles returning webhook response
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.headers.get('stripe-signature')
    event = None
    request_data = json.loads(request.body)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as err:
        # Invalid payload
        return HttpResponse(content=err, status=400)
    except stripe.error.SignatureVerificationError as err:
        # Invalid signature
        return HttpResponse(content=err, status=400)
    except Exception as err:
        # General Exception
        return HttpResponse(content=err, status=400)

    event_type = request_data['type']

    if event_type == 'invoice.paid':
        # Code to action when payment 
        # is all good (user login, update user paid until etc)
        if event.data.object.payment_intent:
            wh_set_paid_until(request, event.data.object)

    if event_type == 'customer.subscription.updated':
        # Code to action when subscription is updated
        # and paid (user login, update user paid until etc)
        update_paid_until(request, event.data.object)

    if event_type == 'invoice.payment_failed':
        # If the payment fails or the customer does not
        # have a valid payment method,
        # an invoice.payment_failed event is sent, 
        # the subscription becomes past_due.
        # Use this webhook to notify your user that their payment has
        # failed and to retrieve new card details.
        failed_payment(request, event.data.object)

    if event_type == 'customer.subscription.deleted':
        # handle subscription canceled automatically based
        # upon your subscription settings. Or if the user cancels it.
        sub_cancelled(request, event.data.object)

    return HttpResponse(status=200)
