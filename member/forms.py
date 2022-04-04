from django import forms
from .models import Document


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
    email_body = forms.CharField()

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
