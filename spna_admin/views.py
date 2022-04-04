from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from news.forms import ArticleForm
from news.models import Articles
from contact.models import Contact
from member.models import Document
from member.forms import DocumentForm


@login_required
def spna_admin(request):
    """A view for the admin page. """

    if not request.user.is_superuser:
        messages.error(request, "Sorry only SPNA Admin can access this page.")
        return redirect(reverse('home'))

    docForm = DocumentForm()
    form = ArticleForm()
    users = User.objects.all()
    contacts = Contact.objects.all()

    context = {
        'docForm': docForm,
        'form': form,
        'users': users,
        'contacts': contacts,
    }

    return render(request, 'spna_admin/spna_admin.html', context)


@login_required
@staff_member_required
def delete_article(request, article_id):
    """
    Deletes the article when called.
    """
    article = get_object_or_404(Articles, id=article_id)
    article.delete()
    messages.success(request, 'Article deleted successfully!')
    return HttpResponseRedirect(reverse('spna_admin'))


@login_required
@staff_member_required
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
        form = ArticleForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully added {article.title}.')
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
@staff_member_required
def add_article(request):
    """
    A view to add articles from the spna_admin page.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry only Admin can access this page.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article successfully added!')
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


@login_required
@staff_member_required
def add_document(request):
    """
    A view to add documents from the spna_admin page.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry only Admin can access this page.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document successfully added!')
            return redirect(reverse('spna_admin'))
        else:
            messages.error(request, 'Failed to add document. Please ensure the form is valid.')
    else:
        form = DocumentForm()

    users = User.objects.all()

    template = 'spna_admin/spna_admin.html'
    context = {
        'form': form,
        'users': users,
    }

    return render(request, template, context)
