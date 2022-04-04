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
    email_date = forms.DateTimeField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email_to'].label = 'To:'
        self.fields['email_subject'].label = 'Subject:'
        self.fields['email_body'].label = 'Body:'
