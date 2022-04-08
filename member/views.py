from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse

import stripe

from .models import Document
from .forms import CustomSignupForm
from .signals import save_spnamember


@login_required
def member_area(request):
    """ 
    A view to return the members area
    """
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


def subscribe(request):
    # This view creates a payment intent..! Next is to set up stripe card element properly. Also might be helpful to add the user once payment has been made and not before.
    """
    This view is activated from the 'Sign Up' button. Needs to instanciate the User.
    """
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        print('post')
        if form.is_valid():
            print('valid')

# creates and saves user (maybe once payment approved?)
            user = form.save(request)
            user.refresh_from_db()
            save_spnamember(user, form)
            user.save()

            messages.success(request, f'Successfully created User {user.spnamember.fullname}.')
            plan =form.cleaned_data['subscription']

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
                currency = 'GBP',
            )
            context = {
                'customer_email': form.cleaned_data['email'],
                'plan': form.cleaned_data['subscription'],
                'STRIPE_PUBLIC_KEY': stripe_public_key,
                'secret_key': payment_intent.client_secret,
                'payment_intent_id': payment_intent.id,
                'automatic': automatic,
                'stripe_plan_id': spi,
            }
            return render(request, 'member/payment.html', context)
        else:
            messages.error(request, 'Failed to add User. Please ensure the form is valid.')
    else:
        form = CustomSignupForm()

    context = {
        'form': form,
    }
    return render(request, 'member/subscribe.html', context)


def payment(request):
    # need to get the previous intent and invoice, pay it and set uop a subscription. Then save the user?
    """
    This view creates the payment intent and sends it to stripe.
    """
    # try:
    #     stripe.api_key = settings.STRIPE_SECRET_KEY
    #     plan = request.POST.get['subscription']
    #     if plan == 'Monthly':
    #         spi = settings.STRIPE_PLAN_MONTHLY_ID
    #     elif plan == 'Six Monthly':
    #         spi = settings.STRIPE_PLAN_SIXMONTHLY_ID
    #     else:
    #         spi = settings.STRIPE_PLAN_YEARLY_ID

    #     automatic = True

    #     payment_intent = stripe.PaymentIntent.create(
    #         amount=plan,
    #         currency = settings.STRIPE_CURRENCY,
    #         payment_method = 'card',
    #     )
    #     context = {
    #         'secret_key': payment_intent.client_secret,
    #         'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    #         'customer_email': request.user.email,
    #         'payment_intent_id': payment_intent.id,
    #         'automatic': automatic,
    #         'stripe_plan_id': spi,
    #     }

    #     return render(request, 'accounts/email_confirm.html', context)

    # except Exception as e:
    #     messages.error(request, 'Sorry, your payment cannot be \
    #         processed right now. Please try again later.')
    #     return HttpResponse(content=e, status=400)


    return render(request, 'member/payment.html')
