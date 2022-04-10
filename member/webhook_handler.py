from django.http import HttpResponse

class StripeWH_Handler:
    """
    Handle the webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic/unknown webhook
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle succeeded webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle succeeded webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

