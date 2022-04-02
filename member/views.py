from django.shortcuts import render
from .models import Document

# Create your views here.
def member_area(request):
    """ 
    A view to return the members area
    """
    docs = Document.objects.all()

    context = {
        'docs': docs,
    }
    return render(request, 'member/member-area.html', context)