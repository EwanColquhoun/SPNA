from django.shortcuts import render
from django.contrib.auth.models import User
from news.forms import ArticleForm


def spna_admin(request):
    """A view for the admin page. """

    form = ArticleForm()
    users = User.objects.all()

    context = {
        'form': form,
        'users': users
    }

    return render(request, 'spna_admin/spna_admin.html', context)