from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from .wh_handler import set_paid_until

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

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
        print("Event constructed correctly")
    except ValueError as e:
        # Invalid payload
        print("Invalid Payload")
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        print("Invalid signature")
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    if event.type =='charge.succeeded':
        # Code to action when payment is all good (user login, update user paid until etc)
        print('Success!')
        set_paid_until(request, event.data.object)

    if event.type =='source.chargeable':
        print('3d secure over')
    
    return HttpResponse(status=200)