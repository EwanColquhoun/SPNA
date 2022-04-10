from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse

import stripe

from .webhook_handler import StripeWH_Handler

@require_POST
@csrf_exempt
def webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WEBHOOK_SIGNING_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
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

    print('Success!')
    return HttpResponse(status=200)