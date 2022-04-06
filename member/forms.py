from django import forms
from django_summernote.widgets import SummernoteWidget
from allauth.account.forms import SignupForm
from .models import Document, Member


class CustomSignupForm(SignupForm):
    """
    Takes the default AllAuth user form, adds and modifies as below.
    """
    class Meta:
        model = Member
        fields = fields = '__all__'
        # fields = ('username', 'first_name', 'last_name',
        #           'email', 'password1', 'password2', 'nursery', 'street_address1')

        username = forms.CharField(max_length=30,
                               required=True,
                               help_text='Required. 150 characters or fewer. \
                                    Letters, digits and @/./+/-/_ only.')
        first_name = forms.CharField(max_length=30,
                                    required=True,
                                    help_text='Required')
        last_name = forms.CharField(max_length=30,
                                    required=True,
                                    help_text='Required')
        email = forms.CharField(max_length=100,
                                widget=forms.EmailInput
                            (attrs={'placeholder': 'youremail@mail.com'}))
        nursery = forms.CharField(max_length=40,
                               required=False,
                               help_text='Please enter the name of the Nursery you are affiliated with.')
  

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.message = self.cleaned_data['message']
        user.message = self.cleaned_data['message']
        user.message = self.cleaned_data['message']
        user.message = self.cleaned_data['message']
        user.message = self.cleaned_data['message']
        user.save()
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
