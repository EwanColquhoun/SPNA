from django.shortcuts import render
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