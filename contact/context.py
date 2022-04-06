from news.models import Articles
from member.models import Document, SPNAMember
from .forms import ContactForm


def contact_modal(request):
    """
    A context processor for the modals
    """

    article = Articles.objects.all()
    doc = Document.objects.all()
    members = SPNAMember.objects.all()
    
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
        'article': article,
        'doc': doc,
        'members':members,
    }

    return context

