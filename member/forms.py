from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    """Article form management."""

    class Meta:
        """
        Document form for spna_admin
        """
        model = Document
        fields = ('title', 'doc',)
        # widgets = {
        #     'content': SummernoteWidget(),
        #     'image': CustomClearableFileInput()
        # }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Document Title'
        self.fields['doc'].label = 'Document Upload'
