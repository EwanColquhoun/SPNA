from django import forms
from django_summernote.widgets import SummernoteWidget

from allauth.account.forms import SignupForm
from .models import Document, SPNAMember


class CustomSignupForm(SignupForm):
    """
    Takes the default AllAuth user form, adds and modifies as below.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password again'
        self.fields['fullname'].label = 'Full Name'

    class Meta:
        model = SPNAMember
        fields = '__all__'

    fullname = forms.CharField(max_length=40, required=False)
    nursery = forms.CharField(max_length=40, required=False,
                            help_text='Please enter the name of the Nursery you are affiliated with.')
    street_address1 = forms.CharField(max_length=40, required=False)
    street_address2 = forms.CharField(max_length=40, required=False)
    town_or_city = forms.CharField(max_length=40, required=False)
    county = forms.CharField(max_length=40, required=False)
    postcode = forms.CharField(max_length=40, required=False)  
    country = forms.CharField(max_length=40, required=False)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a user object.
        
        user = super().save(request)
        user.spnamember.fullname = self.cleaned_data['fullname']
        user.spnamember.nursery = self.cleaned_data['nursery']
        user.spnamember.street_address1 = self.cleaned_data['street_address1']
        user.spnamember.street_address2 = self.cleaned_data['street_address2']
        user.spnamember.town_or_city = self.cleaned_data['town_or_city']
        user.spnamember.county = self.cleaned_data['county']
        user.spnamember.postcode = self.cleaned_data['postcode']
        user.spnamember.country = self.cleaned_data['country']
        return user


class DocumentForm(forms.ModelForm):
    """Article form management."""

    class Meta:
        """
        Document form for spna_admin
        """
        model = Document
        fields = ('title', 'category', 'doc',)
        # widgets = {
        #     'content': SummernoteWidget(),
        #     'image': CustomClearableFileInput()
        # }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Document Title'
        self.fields['doc'].label = 'Document Upload'
        self.fields['category'].label = 'Document Category'


class EmailForm(forms.Form):
    """A form to send emails"""

    email_to = forms.CharField()
    email_subject = forms.CharField()
    email_body = forms.CharField(widget=SummernoteWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email_to'].label = 'To:'
        self.fields['email_subject'].label = 'Subject:'
        self.fields['email_body'].label = 'Body:'

    def save(self):
        """
        Creates a save method
        """
        data = self.cleaned_data
        self.email_to = data['email_to']
        self.email_subject = data['email_subject']
        self.email_body = data['email_body']
        return self
