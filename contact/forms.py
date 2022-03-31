from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Contact



class ContactForm(forms.ModelForm):
    """
    Contact form set up.
    """
    class Meta:
        model = Contact
        fields = ('name', 'phone_number', 'email', 'message')
        widgets = {
            'message': SummernoteWidget(),
            'email': forms.EmailInput(
                attrs={'placeholder': 'you@youremail.com'}),
            'phone_number': forms.TextInput(
                attrs={'placeholder': '+44 1234567890',
                       'rows': 1, 'cols': 15})
        }
