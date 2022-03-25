from django.shortcuts import render


def news_view(request):
    """A view to return news and articles page"""
    return render(request, 'news/news.html')