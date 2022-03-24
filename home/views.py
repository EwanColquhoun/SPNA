from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def index(request):
    """A view to return index page."""
    # message eg:
    # if request.GET:
    #     messages.success(request, 'Well done on the message')
    # else:
    #     messages.info(request, 'This is an error message')

    return render(request, 'home/index.html')


def about(request):
    """A view to return the About page."""
    return render(request, 'home/about.html')