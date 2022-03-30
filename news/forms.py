from django import forms
from .models import Articles


class ArticleForm(forms.ModelForm):
    """Article form management."""

    class Meta:
        model = Articles
        fields = ('title', 'content', 'image', 'campaign')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['title'].label = 'Article Title'
        self.fields['content'].label = 'Article Content'
        self.fields['image'].label = 'Image'
        self.fields['campaign'].label = 'Campaign'
