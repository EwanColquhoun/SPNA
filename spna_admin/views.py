from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from news.forms import ArticleForm
from news.models import Articles
from contact.models import Contact
from member.models import Document, SPNAMember
from member.forms import DocumentForm, EmailForm
from spna.email import send_admin_email
from .get_csv import export_qs_to_csv


@login_required
def spna_admin(request):
    """A view for the admin page. """

    if not request.user.is_superuser:
        messages.error(request, "Sorry only SPNA Admin can access this page.")
        return redirect(reverse('home'))

    emailForm = EmailForm()
    docForm = DocumentForm()
    form = ArticleForm()
    users = User.objects.all()
    contacts = Contact.objects.all()

    context = {
        'emailForm': emailForm,
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
    return HttpResponseRedirect(reverse('news'))


@login_required
@staff_member_required
def delete_contact(request, contact_id):
    """
    Deletes the contact when called.
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry only SPNA Admin can access this page.")
        return redirect(reverse('home'))
        
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
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

    if request.method == 'POST':
        # form = ArticleForm(instance=article)
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully changed {article.title}.')
            return redirect(reverse('news'))
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


@login_required
@staff_member_required
def get_csv_of_users(request):
    """
    Gets a csv of the spnamember model
    """

    return export_qs_to_csv(model_class = SPNAMember)


@login_required
@staff_member_required
def send_admin_email_view(request):
    """
    A method to handle the sending of admin emails.
    """
    contacts = Contact.objects.all()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
        #  call to send email
            send_admin_email(form)
            messages.success(request, 'Email successfully sent!')

            if Contact.objects.filter(email=form.data['email_to']).exists():
                for contact in contacts:
                    if contact.email == form.data['email_to']:
                        contact.replied = True
                        contact.created = contact.created
                        contact.save()
                 
            return redirect(reverse('spna_admin'))
        else:
            messages.error(request, 'Failed to send email. Please ensure the form is valid.')
    else:
        form = EmailForm()

    users = User.objects.all()

    template = 'spna_admin/spna_admin.html'
    context = {
        'form': form,
        'users': users,
    }

    return render(request, template, context)
    
