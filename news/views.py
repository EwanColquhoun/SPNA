from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Articles
from .forms import ArticleForm


class ArticleList(generic.ListView):
    """
    A class to paginate the articles
    """
    model = Articles
    queryset = Articles.objects.all().order_by('-created_on')
    template_name = 'news/news.html'
    paginate_by = 6


def news_view(request):
    """A view to return news and articles page"""
    
    articles = Articles.objects.all().order_by('-created_on')
    # form = ArticleForm
    template = 'news/news.html'
    context = {
        'articles': articles,
        # 'form': form,
    }
    return render(request, template, context)


def initiatives_view(request):
    """A view to return initiatives page """
    
    template = 'news/initiatives.html'
    context = {}

    return render(request, template, context)