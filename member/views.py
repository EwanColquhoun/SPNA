from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .models import Document


@login_required
def member_area(request):
    """ 
    A view to return the members area
    """
    docs = Document.objects.all()

    context = {
        'docs': docs,
    }
    return render(request, 'member/member-area.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_document(request, document_id):
    """
    Deletes the document when called.
    """
    doc = get_object_or_404(Document, id=document_id)
    doc.delete()
    messages.success(request, 'Document deleted successfully!')
    return HttpResponseRedirect(reverse('member_area'))
