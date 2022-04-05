from django.shortcuts import redirect, reverse
from django.contrib import messages

from spna.email import contact_email

from .forms import ContactForm


# Create your views here.
def post_contact(request):
    """A view to manage contact requests"""
    contactform = ContactForm()
    contactform = ContactForm(request.POST)
    if contactform.is_valid():
        contactform.save()
        messages.success(request, "Contact form submitted, we will be intouch shortly. Thank you.")
        contact_email(contactform.instance)
    else:
        messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    return redirect(reverse('home'))
