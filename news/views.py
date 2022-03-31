from django.shortcuts import render
from django.contrib import messages
from .models import Articles
from .forms import ArticleForm


def news_view(request):
    """A view to return news and articles page"""
    
    articles = Articles.objects.all()
    form = ArticleForm
    template = 'news/news.html'
    context = {
        'articles': articles,
        'form': form,
    }
    return render(request, template, context)


def initiatives_view(request):
    """A view to return initiatives page """
    
    template = 'news/initiatives.html'
    context = {}

    return render(request, template, context)