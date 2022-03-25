from django.shortcuts import render
from .models import Articles


def news_view(request):
    """A view to return news and articles page"""
    
    articles = Articles.objects.all()
    template = 'news/news.html'
    context = {
        'articles': articles
    }
    return render(request, template, context)