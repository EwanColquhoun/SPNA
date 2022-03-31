from django import forms
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from spna_admin.widgets import CustomClearableFileInput
from .models import Articles


class ArticleForm(forms.ModelForm):
    """Article form management."""

    class Meta:
        """
        Article form for spna_admin
        """
        model = Articles
        fields = ('title', 'content', 'image', 'campaign')
        widgets = {
            'content': SummernoteWidget(),
        }
        image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Article Title'
        self.fields['content'].label = 'Article Content'
        self.fields['campaign'].label = 'Campaign'
