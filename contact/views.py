from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


# Create your views here.
def post_contact(request):
    """A view to manage contact requests"""
    
    contactform = ContactForm()
    contactform = ContactForm(request.POST)
    if contactform.is_valid():
        contactform.save()
        messages.success(request, "Contact form submitted!")
    else:
        messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    
    return redirect(reverse('home'))

            # cant get the toast to display. It seems to disoplay only when the modal is visible.