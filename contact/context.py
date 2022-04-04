from news.models import Articles
from member.models import Document
from .forms import ContactForm


def contact_modal(request):
    """
    A context processor for the modals
    """

    article = Articles.objects.all()
    doc = Document.objects.all()
    
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
        'article': article,
        'doc': doc,
    }

    return context

