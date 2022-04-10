from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.views.decorators.http import require_POST
# from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.conf import settings
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse

import stripe

from .models import Document
from .forms import CustomSignupForm
from .signals import save_spnamember
from .stripe import set_paid_until

stripe_secret_key = settings.STRIPE_SECRET_KEY
stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY


@login_required
def member_area(request):
    """ 
    A view to return the members area
    """
    if not request.user.is_authenticated:
        messages.error(request, "Sorry only SPNA Members can access this page.")
        return redirect(reverse('home'))

    docs = Document.objects.all()

    context = {
        'docs': docs,
    }
    return render(request, 'member/member-area.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_document(request, document_id):
    """
    Deletes the document when called.
    """
    doc = get_object_or_404(Document, id=document_id)
    doc.delete()
    messages.success(request, 'Document deleted successfully!')
    return HttpResponseRedirect(reverse('member_area'))


# class CustomSignUpView(SignupView):
#     """
#     Overides the default (AllAuth) signup methods.
#     """
#     success_url = 'home'

# # Use the below to gain access to variables with def post and get then use the form_valid function perhaps?

#     # def post(self,request):
#     #     print('post')
#     #     return render(request, 'accounts/login.html')

#     def form_valid(self, form):
#         # User initiated here to gain access

#         user = form.save(self.request)
#         user.refresh_from_db()
#         save_spnamember(user, form)
#         user.save()
#         self.user = user
        
#         try:
#             # register_email(form.instance)
#             messages.success(self.request, 'Registration successful!')
#             return complete_signup(
#                 self.request,
#                 self.user,
#                 settings.EMAIL_VERIFICATION,
#                 self.success_url,
#             )
#         except ImmediateHttpResponse as error:
#             return error.response

  
# A trial to get it to work with stripe payments below.
def membership(request):
    """
    a signup form view
    """
    form = CustomSignupForm()

    context = {
        'form': form,
    }
    return render(request, 'member/subscribe.html', context)

# payment methods
def subscribe(request):
    # This view creates a payment intent..! Next is to set up stripe card element properly. Also might be helpful to add the user once payment has been made and not before.
    """
    This view is activated from the 'Sign Up' button. Needs to instanciate the User.
    """

    # if request.method == 'POST':
    form = CustomSignupForm(request.POST)
    print('post')
        # if form.is_valid():
    print('valid')

# creates and saves user (maybe once payment approved?)
    # user = form.save(request)
    # user.refresh_from_db()
    # save_spnamember(user, form)
    # user.save()

    # messages.success(request, f'Successfully created User {user.spnamember.fullname}.')
    plan =request.POST.get('subscription')

    if plan == 'Monthly':
        spi = settings.STRIPE_PLAN_MONTHLY_ID
        amount = '1000'
    elif plan == 'Six Monthly':
        spi = settings.STRIPE_PLAN_SIXMONTHLY_ID
        amount = '5500'
    else:
        spi = settings.STRIPE_PLAN_YEARLY_ID
        amount = '10000'

    automatic = True

# creates the intent
    stripe.api_key = stripe_secret_key
    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        payment_method_types=['card'],
        currency='GBP',
    )
    context = {
        'customer_email': request.POST.get('email'),
        'plan': plan,
        'STRIPE_PUBLIC_KEY': stripe_public_key,
        'secret_key': payment_intent.client_secret,
        'payment_intent_id': payment_intent.id,
        'automatic': automatic,
        'stripe_plan_id': spi,
        'form': form,
    }
    return render(request, 'member/payment.html', context)
    #     else:
    #         messages.error(request, 'Failed to add User. Please ensure the form is valid.')
    # else:
    #     form = CustomSignupForm()

    # context = {
    #     'form': form,
    # }
    # return render(request, 'member/membership.html', context)

def card(request):
    """
    Processes payment from card view.
    """

    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    automatic = request.POST['automatic']
    customer_email = request.POST['customer_email']
    stripe.api_key = stripe_secret_key

    if automatic:
        customer = stripe.Customer.create(
            email=customer_email,
            payment_method=payment_method_id,
            invoice_settings={
                'default_payment_method': payment_method_id
            }
        )
        sub = stripe.Subscription.create(
            customer=customer.id,
            items=[
                {
                    'plan': stripe_plan_id
                },
            ]
        )
        latest_invoice = stripe.Invoice.retrieve(sub.latest_invoice)
        stripe.PaymentIntent.modify(
            latest_invoice.payment_intent,
            payment_method=payment_method_id,
        )
        ret = stripe.PaymentIntent.confirm(
            latest_invoice.payment_intent  
        )

        if ret.status == 'requires_action':
            intent = stripe.PaymentIntent.retrieve(
                latest_invoice.payment_intent
            )
            context = {
                'payment_intent_secret': intent.client_secret,
                'STRIPE_PUBLISHABLE_KEY': stripe_public_key,
            }

            return render(request, 'member/3dsec.html', context)

    else:
        stripe.PaymentIntent.modify(
            payment_intent_id,
            payment_method=payment_method_id,
        )
    
    return render(request, 'home/index.html')


# def card(request):
#     # need to get the previous intent and invoice, pay it and set uop a subscription. Then save the user?
#     """
#     This view creates the payment intent and sends it to stripe.
#     """
#     payment_intent_id = request.POST['payment_intent_id']
#     payment_method_id = request.POST['payment_method_id']
#     email = request.POST['customer_email']
#     stripe_plan_id = request.POST['stripe_plan_id']
#     stripe.api_key = stripe_secret_key

#     customer = stripe.Customer.create(
#         email=email,
#         payment_method=payment_method_id,
#         invoice_settings={
#             'default_payment_method': 'card'
#         }
#     )
#     s = stripe.Subscription.create(
#         customer=customer.id,
#         items=[
#             {
#                 'plan': stripe_plan_id
#             },
#         ]
#     )
#     latest_invoice = stripe.Invoice.retrieve(s.latest_invoice)

#     ret = stripe.PaymentIntent.confirm(
#         latest_invoice.payment_intent
#     )

#     if ret.status == 'requires_action':
#         intent = stripe.PaymentIntent.retrieve(
#             latest_invoice.payment_intent
#         )
#         context = {
#             'payment_intent_secret': intent.client_secret,
#             'STRIPE_PUBLISHABLE_KEY': stripe_public_key,
#         }

#         return render(request, 'member/3dsec.html', context)

#     else:
#         print(ret.status, 'not 3d secure!')
#         stripe.PaymentIntent.modify(
#             payment_intent_id,
#             payment_method=payment_method_id,
#         )
#         return render(request, 'member/member-area.html')


# stripe webhooks from https://github.com/Django-Lessons/video-store-proj
# @require_POST
# @csrf_exempt
# def stripe_webhooks(request):

#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None

#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, settings.STRIPE_WEBHOOK_SIGNING_KEY
#         )
#         print("Event constructed correctly")
#     except ValueError:
#         # Invalid payload
#         print("Invalid Payload")
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError:
#         # Invalid signature
#         print("Invalid signature")
#         return HttpResponse(status=400)

#     # Handle the event
#     if event.type == 'charge.succeeded':
#         # object has  payment_intent attr
#         messages.success(request, 'payment recieved, thank you')
#         set_paid_until(request, event.data.object)

#     return HttpResponse(status=200)

