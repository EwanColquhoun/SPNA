from django.shortcuts import redirect, reverse
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def post_contact(request):
    """A view to manage contact requests"""
    
    contactform = ContactForm()
    contactform = ContactForm(request.POST)
    if contactform.is_valid():
        contactform.save()
        messages.success(request, "Contact form submitted!")
        print('valid')
    else:
        messages.error(request, 'Failed to update product. Please ensure the form is valid.')
        print('notvalid')
    return redirect(reverse('home'))

            # cant get the toast to display. It seems to disoplay only when the modal is visible.