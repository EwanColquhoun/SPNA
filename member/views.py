import stripe

from django.shortcuts import (
    render,
    reverse,
    get_object_or_404,
    redirect,
    HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

from allauth.account.forms import LoginForm
from allauth.account.utils import perform_login

from spna.email import (
    register_email,
    cancel_email,
    cancel_email_to_member,
    payment_error_admin,
    welcome_email_to_member,
    upgrade_email_to_member,
    update_card_details_to_member,
    renewal_email)

from .models import Document, SPNAMember, Plan
from .forms import CustomSignupForm, ProfileForm, UpgradeForm

stripe_secret_key = settings.STRIPE_SECRET_KEY
stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY


@login_required
def member_area(request):
    """
    A view to return the members area
    """
    if not request.user.spnamember.paid:
        messages.error(request, "Sorry only SPNA Members can \
                       access this page.")
        return redirect(reverse('home'))

    docs_1 = Document.objects.filter(category='1')
    docs_2 = Document.objects.filter(category='2')
    docs_3 = Document.objects.filter(category='3')

    context = {
        'docs_1': docs_1,
        'docs_2': docs_2,
        'docs_3': docs_3,
    }
    return render(request, 'member/member-area.html', context)


@login_required
def profile_view(request):
    """
    A view to show the user profile.
    """
    if not request.user.spnamember.paid:
        messages.error(request, "Sorry only SPNA Members can \
                       access this page.")
        return redirect(reverse('home'))

    member = get_object_or_404(SPNAMember, user=request.user)
    default_pm = ''

    if not request.user.is_superuser:
        cus = request.user.spnamember.stripe_id
        stripe.api_key = stripe_secret_key
        if cus:
            p_method = stripe.Customer.list_payment_methods(cus, type="card",)
            default_pm = p_method.data[0].card
        else:
            default_pm = False

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

        member = get_object_or_404(SPNAMember, user=request.user)
        form = ProfileForm(instance=member)
        upgrade_form = UpgradeForm()
        template = 'member/profile.html'
        context = {
            'upgrade_form': upgrade_form,
            'form': form,
            'member': member,
            'STRIPE_PUBLIC_KEY': stripe_public_key,
            'pm': default_pm,
        }

        return render(request, template, context)

    else:
        upgrade_form = UpgradeForm()
        form = ProfileForm(instance=member)
        template = 'member/profile.html'
        context = {
                'upgrade_form': upgrade_form,
                'form': form,
                'member': member,
                'STRIPE_PUBLIC_KEY': stripe_public_key,
                'pm': default_pm,
            }
        return render(request, template, context)


@login_required
@require_POST
def upgrade_subscription(request):
    """
    A view to change the logged in user's subscription.
    """
    plan = request.POST.get('name')

    if plan == 'Monthly':
        spi = settings.STRIPE_PLAN_MONTHLY_ID
        spna_plan = Plan.objects.get(pk=1)
    elif plan == 'Six Monthly':
        spi = settings.STRIPE_PLAN_SIXMONTHLY_ID
        spna_plan = Plan.objects.get(pk=2)
    else:
        spi = settings.STRIPE_PLAN_YEARLY_ID
        spna_plan = Plan.objects.get(pk=3)

    if request.user.spnamember:
        sub = request.user.spnamember.sub_id
        try:
            stripe.api_key = stripe_secret_key
            subscription = stripe.Subscription.retrieve(sub)
            stripe.Subscription.modify(
                subscription.id,
                payment_behavior='pending_if_incomplete',
                proration_behavior='always_invoice',
                items=[{
                    'id': subscription['items']['data'][0].id,
                    'price': spi,
                }]
            )
            member = get_object_or_404(SPNAMember, user=request.user)
            member.subscription = spna_plan.name
            member.save()
            member.refresh_from_db()
            upgrade_email_to_member(member)
            messages.success(request,
                             'Your subscription has been changed. \
                             Please reload the page for updated details.')
        except AttributeError as err:
            messages.error(request,
                           f'There has been an error. Please contact the SPNA. \
                            Error={err}.')
            trans = 'Upgrade'
            payment_error_admin(request, err, trans)
    else:
        messages.info(request,
                      'Your details are missing from the database, \
                        please contact SPNA admin.')

    return redirect('profile_page')


@login_required
def renew_subscription(request):
    """
    A view to renew the logged in user's subscription,
    providing the are still in a billing period.
    """
    try:
        stripe.api_key = stripe_secret_key
        sub = request.user.spnamember.sub_id
        stripe.Subscription.modify(
            sub,
            cancel_at_period_end=False)
        member = get_object_or_404(SPNAMember, user=request.user)
        member.has_cancelled = False
        member.save()
        renewal_email(member)
        messages.success(request,
                         f'Your subscription will continue as \
                            normal from {request.user.spnamember.paid_until}.')
    except AttributeError as err:
        messages.error(request,
                       f'There has been an error. \
                        Please contact the SPNA. Error={err}.')
        trans = 'Renew'
        payment_error_admin(request, err, trans)

    return redirect(reverse('profile_page'))


@login_required
def cancel_subscription(request):
    """
    A view to cancel the logged in user's subscription.
    """
    try:
        stripe.api_key = stripe_secret_key
        sub = request.user.spnamember.sub_id
        stripe.Subscription.modify(
            sub,
            cancel_at_period_end=True)
        cancel_email(request.user)
        cancel_email_to_member(request.user)
        member = get_object_or_404(SPNAMember, user=request.user)
        member.has_cancelled = True
        member.save()
        messages.success(request,
                         f'Your subscription will end at the end of \
                         the next billing period:\
                         {request.user.spnamember.paid_until}.')
        return redirect('profile_page')
    except AttributeError as err:
        messages.error(request,
                       f'There has been an error. \
                        Please contact the SPNA. Error={err}.')
        trans = 'Cancel'
        payment_error_admin(request, err, trans)

    return render(request, 'home/index.html')


@require_POST
def update_payment_method(request):
    """
    A view to update the logged in users default payment method.
    """
    try:
        new_pm = request.POST['payment_method_id']
        cus = request.user.spnamember.stripe_id
        sub = request.user.spnamember.sub_id

        stripe.api_key = stripe_secret_key
        stripe.PaymentMethod.attach(new_pm, customer=cus,)
        stripe.Customer.modify(
            cus,
            invoice_settings={"default_payment_method": new_pm},)
        stripe.Subscription.modify(sub, default_payment_method=new_pm)

        update_card_details_to_member(request)
        messages.success(request,
                         'Your card details have been updated for the \
                            next payment.')
        return redirect(reverse('profile_page'))

    except AttributeError as err:
        messages.error(request,
                       f'Card declined. Please check the details and \
                        try again. {err}')
        trans = 'Update payment'
        payment_error_admin(request, err, trans)
        return redirect(reverse('profile_page'))


def subscribe(request):
    """
    This view is activated from the 'Sign Up' button. 
    Creates the payment intent.
    """
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            # creates and saves user attributes into the session
            request.session['fullname'] = form.cleaned_data['fullname']
            request.session['email'] = form.cleaned_data['email']
            request.session['nursery'] = form.cleaned_data['nursery']
            request.session['phone'] = form.cleaned_data['phone']
            request.session['postcode'] = form.cleaned_data['postcode']
            request.session['street_address1'] = form.cleaned_data['street_address1']
            request.session['subscription'] = form.cleaned_data['subscription']
            request.session['town_or_city'] = form.cleaned_data['town_or_city']
            request.session['country'] = form.cleaned_data['country']
            request.session['password'] = form.cleaned_data['password1']

            plan = request.POST.get('subscription')
            # gets the plan selected from the request
            if plan == 'Monthly':
                spi = settings.STRIPE_PLAN_MONTHLY_ID
                spna_plan = Plan.objects.get(pk=1)
                amount = spna_plan.amount
            elif plan == 'Six Monthly':
                spi = settings.STRIPE_PLAN_SIXMONTHLY_ID
                spna_plan = Plan.objects.get(pk=2)
                amount = spna_plan.amount
            else:
                spi = settings.STRIPE_PLAN_YEARLY_ID
                spna_plan = Plan.objects.get(pk=3)
                amount = spna_plan.amount

            automatic = True

            # creates the intent
            stripe.api_key = stripe_secret_key
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                setup_future_usage='on_session',
                currency='GBP',
            )

            context = {
                'customer_email': request.POST.get('email'),
                'fullname': request.POST.get('fullname'),
                'STRIPE_PUBLIC_KEY': stripe_public_key,
                'secret_key': payment_intent.client_secret,
                'payment_intent_id': payment_intent.id,
                'automatic': automatic,
                'stripe_plan_id': spi,
                'spna_plan': spna_plan,
            }

            return render(request, 'member/payment.html', context)

        else:
            messages.error(request, 'There was an error in the form. \
                           Please ensure the form has been correctly\
                             filled in.')
            return redirect(reverse('subscribe'))
    else:
        form = CustomSignupForm()
        context = {
            'form': form,
            }
        return render(request, 'member/subscribe.html', context)


def payment(request):
    """
    A view to pay the SPNA, create a customer and an associated subscription.
    """
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    customer_email = request.POST['customer_email']
    stripe.api_key = stripe_secret_key
    log_form = LoginForm()

    if request.method == 'POST':
        try:
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
                ],
            )
        except stripe.error.CardError as err:
            messages.error(request,
                           f"There was a problem with the card details. \
                            Please try again. {err}")
            return redirect('subscribe')

        except stripe.error.StripeError as err:
            messages.error(request,
                           f"Sorry we have encountered a problem. \
                            Please try again later. {err}")
            return redirect('subscribe')

        latest_invoice = stripe.Invoice.retrieve(sub.latest_invoice)
        # Generates an instance of the SPNA member once invoice is paid.
        if latest_invoice.paid:
            full_name = request.session['fullname']
            user = User.objects.create_user(
                username=request.session['email'],
                password=request.session['password'],
            )
            user.refresh_from_db()
            user.email = request.session['email']
            user.first_name = user.spnamember.get_fname(full_name)
            user.last_name = user.spnamember.get_sname(full_name)
            user.spnamember.sub_id = sub.id
            user.spnamember.stripe_id = customer.id
            user.spnamember.subscription = request.session['subscription']
            user.spnamember.fullname = request.session['fullname']
            user.spnamember.phone = request.session['phone']
            user.spnamember.country = request.session['country']
            user.spnamember.postcode = request.session['postcode']
            user.spnamember.town_or_city = request.session['town_or_city']
            user.spnamember.street_address1 = request.session['street_address1']
            user.spnamember.nursery = request.session['nursery']
            user.save()

            perform_login(request,
                          user,
                          settings.ACCOUNT_EMAIL_VERIFICATION,
                          signup=False)
            user.refresh_from_db()
            welcome_email_to_member(user)
            messages.success(request,
                             f'Successfully created SPNA\
                                 Member {user.spnamember.fullname}.')

            return HttpResponseRedirect('/')

        else:
            try:
                ret = stripe.PaymentIntent.confirm(
                    latest_invoice.payment_intent,
                    return_url="https://scottishpna.herokuapp.com/",
                )
                # 3D Secure
                if ret.status == 'requires_action':
                    intent = stripe.PaymentIntent.retrieve(
                        latest_invoice.payment_intent
                    )
                    user = User.objects.create_user(
                        username=request.session['email'],
                        password=request.session['password'],
                    )
                    user.email = request.session['email']
                    full_name = request.session['fullname']
                    user.first_name = user.spnamember.get_fname(full_name)
                    user.last_name = user.spnamember.get_sname(full_name)
                    user.spnamember.sub_id = sub.id
                    user.spnamember.stripe_id = customer.id
                    user.spnamember.subscription = request.session['subscription']
                    user.spnamember.fullname = request.session['fullname']
                    user.spnamember.phone = request.session['phone']
                    user.spnamember.country = request.session['country']
                    user.spnamember.postcode = request.session['postcode']
                    user.spnamember.town_or_city = request.session['town_or_city']
                    user.spnamember.street_address1 = request.session['street_address1']
                    user.spnamember.nursery = request.session['nursery']
                    user.save()
                    user.refresh_from_db()

                    context = {
                        'payment_intent_secret': intent.client_secret,
                        'STRIPE_PUBLISHABLE_KEY': stripe_public_key,
                    }
                    return render(request, 'member/3dsec.html', context)
            except stripe.error.StripeError as err:
                messages.warning(request,
                                 f'The card was declined. \
                                    Please try again. {err}')
                return redirect('subscribe')

        context = {
            'form': log_form,
        }

        return render(request, 'account/login.html', context)

    else:
        form = CustomSignupForm()
        context = {
            'form': form,
            }
        return render(request, 'member/subscribe.html', context)


def secure(request):
    """
    A view to show on 3d secure payment
    """
    return render(request, 'member/3dsec.html')


def member_login(request):
    """
    A view to log in the user after 3d auth passes
    """
    try:
        user = get_object_or_404(User, email=request.session['email'])
        welcome_email_to_member(user)
        register_email(user)
        perform_login(request,
                      user,
                      settings.ACCOUNT_EMAIL_VERIFICATION,
                      signup=False)
        return redirect('/')
    except ValueError as err:
        messages.error(request,
                       f'There has been an error logging you in. \
                        Please try again from the home page. Error: {err}')

    return render(request, 'member/member-login.html')
