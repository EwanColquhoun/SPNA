import stripe

from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

from allauth.account.views import SignupView
from allauth.account.forms import LoginForm
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse

from .models import Document, SPNAMember
from .forms import CustomSignupForm, ProfileForm
from .signals import get_fname, get_sname


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


@login_required
def profile_view(request):
    """
    A view to show the user profile.
    """
    member = get_object_or_404(SPNAMember, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = ProfileForm(instance=member)

    template = 'member/profile.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)



@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_document(request, document_id):
    """
    Deletes the document when called.
    """
    doc = get_object_or_404(Document, id=document_id)
    doc.delete()
    messages.success(request, 'Document deleted successfully!')
    return HttpResponseRedirect(reverse('member_area'))


# A trial to get it to work with stripe payments below.
@csrf_protect
def membership(request):
    """
    a signup form view
    """
    form = CustomSignupForm()

    context = {
        'form': form,
    }

    return render(request, 'member/subscribe.html', context)


def secure(request):
    """ 
    A view to show on 3d secure payment
    """
    
    # messages.success(request, f'Welcome {user.fullname} to the SPNA.')
    return render(request, 'member/3dsec.html')


def subscribe(request):
    # This view creates a payment intent..!
    """
    This view is activated from the 'Sign Up' button.
    """

    form = CustomSignupForm(request.POST)
    print('post')
    if request.method == 'POST':
        if form.is_valid():

        # creates and saves user attributes into the session
            user = form.save(request)
            user.first_name=get_fname(form)
            user.last_name=get_sname(form)
            user.save()
            request.session['fullname'] = form.cleaned_data['fullname']
            request.session['email'] = form.cleaned_data['email']
            request.session['nursery'] = form.cleaned_data['nursery']
            request.session['phone'] = form.cleaned_data['phone']
            request.session['postcode'] = form.cleaned_data['postcode']
            request.session['street_address1'] = form.cleaned_data['street_address1']
            request.session['subscription'] = form.cleaned_data['subscription']
            request.session['town_or_city'] = form.cleaned_data['town_or_city']
            request.session['country'] = form.cleaned_data['country']

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
                'fullname': request.POST.get('fullname'),
                'plan': plan,
                'STRIPE_PUBLIC_KEY': stripe_public_key,
                'secret_key': payment_intent.client_secret,
                'payment_intent_id': payment_intent.id,
                'automatic': automatic,
                'stripe_plan_id': spi,
            }
            return render(request, 'member/payment.html', context)
        else:
            form = CustomSignupForm(data=request.POST)
            print(form.data)
            messages.error(request, 'Please ensure the form has been correctly filled in.')
            
            return redirect('membership')


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
    log_form = LoginForm()

    # Automatic renewal for potential future development.
    if automatic:
        customer = stripe.Customer.create(
            email=customer_email,
            name=request.session['fullname'],
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
        # Generates an instance of the SPNA member once invoice is paid.
        if latest_invoice.paid:
            user = User.objects.get(email=request.session['email'])
            user.refresh_from_db()
            user.spnamember.subscription=request.session['subscription']
            user.spnamember.fullname=request.session['fullname']
            user.spnamember.phone=request.session['phone']
            user.spnamember.country=request.session['country']
            user.spnamember.postcode=request.session['postcode']
            user.spnamember.town_or_city=request.session['town_or_city']
            user.spnamember.street_address1=request.session['street_address1']
            user.spnamember.nursery=request.session['nursery']
            user.save()
            messages.success(request, f'Successfully created user {user.spnamember.fullname}.')
    
            context = {
                'form':log_form,
            }

            return render(request, 'account/login.html', context)
        else:
            ret = stripe.PaymentIntent.confirm(
                latest_invoice.payment_intent,
            )
            # 3D Secure
            if ret.status == 'requires_action':
                intent = stripe.PaymentIntent.retrieve(
                    latest_invoice.payment_intent
                )
                user = User.objects.get(email=request.session['email'])
                user.refresh_from_db()
                user.spnamember.subscription=request.session['subscription']
                user.spnamember.fullname=request.session['fullname']
                user.spnamember.phone=request.session['phone']
                user.spnamember.country=request.session['country']
                user.spnamember.postcode=request.session['postcode']
                user.spnamember.town_or_city=request.session['town_or_city']
                user.spnamember.street_address1=request.session['street_address1']
                user.spnamember.nursery=request.session['nursery']
                user.save()
                # messages.success(request, f'Successfully created User {user.spnamember.fullname}.')
                
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
        messages.success(request, f'Successfully created User {user.spnamember.fullname}.')
    
    context = {
        'form': log_form,
    }

    return render(request, 'account/login.html', context)


def payment_failed(request, e):

    form = CustomSignupForm()

    messages.error(request, f'There was a problem with your payment. Please try again. Error: {e}')

    context = {
        'form':form,
    }

    return render(request, 'member/subscribe.html', context)