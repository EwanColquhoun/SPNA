from .forms import ContactForm


def contact_modal(request):

    contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }

    return context