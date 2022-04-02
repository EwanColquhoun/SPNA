from django.shortcuts import render

# Create your views here.
def member_area(request):
    """ 
    A view to return the members area
    """

    return render(request, 'member/member-area.html')