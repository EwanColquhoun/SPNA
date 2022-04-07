from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from allauth.account.views import SignupView
from allauth.account.utils import complete_signup
from allauth.exceptions import ImmediateHttpResponse

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


class CustomSignUpView(SignupView):
    """
    Overides the default (AllAuth) signup methods.
    """
    success_url = 'home'

    def form_valid(self, form):
        # User initiated here to gain access

        user = form.save(self.request)
        user.refresh_from_db()
        user.spnamember.fullname = form.cleaned_data['fullname']
        user.spnamember.nursery = form.cleaned_data['nursery']
        user.spnamember.street_address1 = form.cleaned_data['street_address1']
        user.spnamember.town_or_city = form.cleaned_data['town_or_city']
        user.spnamember.postcode = form.cleaned_data['postcode']
        user.spnamember.country = form.cleaned_data['country']
        user.spnamember.subscription = self.request.POST['subscription']
        user.spnamember.save()
        print(user.spnamember.nursery, 'spna')
        print(user.spnamember.fullname, 'fullname')
        self.user = user
        try:
            # register_email(form.instance)
            messages.success(self.request, 'Registration successful!')
            return complete_signup(
                self.request,
                self.user,
                settings.EMAIL_VERIFICATION,
                self.success_url,
            )
        except ImmediateHttpResponse as error:
            return error.response