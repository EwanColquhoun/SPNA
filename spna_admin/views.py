from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from news.forms import ArticleForm
from news.models import Articles


def spna_admin(request):
    """A view for the admin page. """

    form = ArticleForm()
    users = User.objects.all()

    context = {
        'form': form,
        'users': users
    }

    return render(request, 'spna_admin/spna_admin.html', context)


def delete_article(request, article_id):
    """
    Deletes the article when called.
    """
    article = get_object_or_404(Articles, id=article_id)
    article.delete()
    messages.success(request, 'Article deleted successfully!')
    return HttpResponseRedirect(reverse('spna_admin'))


def edit_article(request, article_id):
    """
    A view to edit the article on the spna_admin page.
    """
    article = get_object_or_404(Articles, id=article_id)
    form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'spna_admin/spna_admin.html', context)