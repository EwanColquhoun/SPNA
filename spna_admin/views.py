from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from news.forms import ArticleForm
from news.models import Articles


@login_required
def spna_admin(request):
    """A view for the admin page. """

    form = ArticleForm()
    users = User.objects.all()

    context = {
        'form': form,
        'users': users
    }

    return render(request, 'spna_admin/spna_admin.html', context)


@login_required
def delete_article(request, article_id):
    """
    Deletes the article when called.
    """
    article = get_object_or_404(Articles, id=article_id)
    article.delete()
    messages.success(request, 'Article deleted successfully!')
    return HttpResponseRedirect(reverse('spna_admin'))


@login_required
def edit_article(request, article_id):
    """
    A view to edit the article on the spna_admin page.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry only SPNA Admin can access this page.")
        return redirect(reverse('home'))
    
    article = get_object_or_404(Articles, id=article_id)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        
        # print(request.POST)
        # slug = slugify(request.POST.get('title'))
        form = ArticleForm(request.POST, request.FILES,)
        # form.instance.slug = slug
        # form.save(commit=False)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('spna_admin'))
        else:
            messages.error(request, 'Failed to add article. Please ensure the form is valid.')
    else:
        form = ArticleForm(instance=article)
        messages.info(request, f'You are editing {article.title}')


    users = User.objects.all()
    template = 'spna_admin/edit_article.html'
    context = {
        'users': users,
        'article': article,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_article(request):
    """
    A view to add articles from the spna_admin page.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry only store owners can access this page.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('spna_admin'))
        else:
            messages.error(request, 'Failed to add article. Please ensure the form is valid.')
    else:
        form = ArticleForm()

    users = User.objects.all()

    template = 'spna_admin/spna_admin.html'
    context = {
        'form': form,
        'users': users,
    }

    return render(request, template, context)
