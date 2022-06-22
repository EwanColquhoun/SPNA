from django.shortcuts import render

def page_not_found(request, Exception):
    return render(request, 'not-found.html')

def server_not_found(request):
    return render(request, 'server-not-found.html')