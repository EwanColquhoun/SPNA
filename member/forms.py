from django import forms
from django_countries import countries
from django_summernote.widgets import SummernoteWidget

from allauth.account.forms import SignupForm
from .models import Document, SPNAMember, Plan


class CustomSignupForm(SignupForm):
    """
    Takes the default AllAuth user form, adds and modifies as below.
    """
    M = 'Monthly'
    M6 = 'Six Monthly'
    Y = 'Yearly'

    PLAN = (
        (M, '£10 monthly'),
        (M6, '£55 six monthly'),
        (Y, '£100 yearly'),
    )

    COUNTRY_CHOICES = tuple(countries)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password again'
        self.fields['fullname'].label = 'Full Name'
        self.fields['country'].initial = 'GB'

    class Meta:
        model = SPNAMember
        fields = '__all__'

    fullname = forms.CharField(max_length=40, required=True)
    nursery = forms.CharField(max_length=40, required=True,
                            help_text='Please enter the name of the '
                            'Nursery you are affiliated with.')
    street_address1 = forms.CharField(max_length=40, required=False)
    town_or_city = forms.CharField(max_length=40, required=False)
    postcode = forms.CharField(max_length=40, required=False)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)
    phone = forms.CharField(max_length=15, required=False)
    subscription = forms.ChoiceField(choices=PLAN, required=True,
                                    help_text='For access to member'
                                    ' documents and SPNA Membership')


    field_order = [
        'fullname',
        'nursery',
        'email',
        'email2',
        'street_address1',
        'town_or_city',
        'postcode',
        'country',
        'phone',
        'subscription',
        'password1',
        'password2',
    ]

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a user object.

        user = super().save(request)
        user.spnamember.fullname = self.cleaned_data['fullname']
        user.spnamember.nursery = self.cleaned_data['nursery']
        user.spnamember.street_address1 = self.cleaned_data['street_address1']
        user.spnamember.town_or_city = self.cleaned_data['town_or_city']
        user.spnamember.postcode = self.cleaned_data['postcode']
        user.spnamember.country = self.cleaned_data['country']
        user.spnamember.phone = self.cleaned_data['phone']
        user.spnamember.subscription = request.POST['subscription']
        return user


class ProfileForm(forms.ModelForm):
    """Profile update form"""

    class Meta:
        model = SPNAMember
        exclude = (
            'user',
            'subscription',
            'paid_until',
            'paid',
            'stripe_id',
            'sub_id',
            'has_cancelled'
            )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['street_address1'].label = 'Street Address'


class DocumentForm(forms.ModelForm):
    """Article form management."""

    class Meta:
        """
        Document form for spna_admin
        """
        model = Document
        fields = ('title', 'category', 'doc',)

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


class UpgradeForm(forms.Form):
    """A form to update the subscription"""

    # C = 'Current'
    M = 'Monthly'
    M6 = 'Six Monthly'
    Y = 'Yearly'

    PLAN = (
        # (C, 'No Change'),
        (M, '£10 monthly'),
        (M6, '£55 six monthly'),
        (Y, '£100 yearly'),
    )

    name = forms.ChoiceField(choices=PLAN, required=True)

    class Meta:
        model = Plan
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Chosen Subscription'
        # self.fields['name'].default = request.user.spnamember.subscription.                                
   
