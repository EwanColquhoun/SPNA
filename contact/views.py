from django.shortcuts import redirect, reverse, get_list_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST

from spna.email import contact_email

from .models import Contact
from .forms import ContactForm
from spna.helpers import strip_tags


@require_POST
def post_contact(request):
    """A view to manage contact requests"""
    contactform = ContactForm()
    contactform = ContactForm(request.POST)
        
    if contactform.is_valid():
        email = request.POST.get('email')
        contactform.save()
        try:
            user = User.objects.get(email=email)
            contacts = get_list_or_404(Contact, email=email)
            if user:
                for contact in contacts:
                    contact.member = True
                    contact.save()
            messages.success(request, "Contact form submitted, we will be intouch shortly. Thank you.")
            contact_email(contactform.instance)
            return redirect(reverse('home'))
        except Exception:
            messages.success(request, "Contact form submitted, we will be intouch shortly. Thank you.")
            contact_email(contactform.instance)
            return redirect(reverse('home'))

    else:
        messages.error(request, 'Failed to send. Please try again.')
    return redirect(reverse('home'))
