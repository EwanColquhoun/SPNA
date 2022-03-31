from django import forms
from .models import Articles
from .widgets import CustomClearableFileInput


class ArticleForm(forms.ModelForm):
    """Article form management."""

    class Meta:
        """
        Article form for spna_admin
        """
        model = Articles
        fields = ('title', 'content', 'image_url', 'image', 'campaign')
        image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['title'].label = 'Article Title'
        self.fields['content'].label = 'Article Content'
        self.fields['campaign'].label = 'Campaign'
        # self.fields['slug'].disabled = True