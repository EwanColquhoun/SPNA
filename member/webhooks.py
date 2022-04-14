from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from .wh_handler import set_paid_until
# from member.views import payment_failed

import stripe
import json


endpoint_secret = settings.STRIPE_WEBHOOK_SIGNING_KEY

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
        print("Event constructed correctly")
    except ValueError as er:
        # Invalid payload
        # payment_failed(request, er)
        print("Invalid Payload")
        return HttpResponse(content=er, status=400)
    except stripe.error.SignatureVerificationError as er:
        # Invalid signature
        # payment_failed(request, e)
        print("Invalid signature")
        return HttpResponse(content=er, status=400)
    except Exception as er:
        # payment_failed(request, er)
        print('last error')
        return HttpResponse(content=er, status=400)

    data = request_data['data']
    event_type = request_data['type']
    print(event_type, 'TYPE')

    # data_object = data['object']

    if event_type =='invoice.paid':
        # Code to action when payment is all good (user login, update user paid until etc)
        print('Success!', data)
        set_paid_until(request, event.data.object)

    if event_type == 'invoice.payment_failed':
        # If the payment fails or the customer does not have a valid payment method,
        # an invoice.payment_failed event is sent, the subscription becomes past_due.
        # Use this webhook to notify your user that their payment has
        # failed and to retrieve new card details.
        print(data, 'failed')

    if event_type == 'customer.subscription.deleted':
        # handle subscription canceled automatically based
        # upon your subscription settings. Or if the user cancels it.
        print(data, 'cust_deleted')
    
    return HttpResponse(status=200)