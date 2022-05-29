from django.shortcuts import render
from django.views import generic

from contact.forms import ContactForm
from .models import Articles


class ArticleList(generic.ListView):
    """
    A class to paginate the articles
    """
    model = Articles
    queryset = Articles.objects.all().order_by('-created_on')
    template_name = 'news/news.html'
    paginate_by = 6


def initiatives_view(request):
    """A view to return initiatives page """

    form = ContactForm()
    template = 'news/initiatives.html'
    context = {
        'contact_form':form
    }

    return render(request, template, context)
