from django.test import TestCase
from django.test.client import Client

from .forms import ProfileForm, DocumentForm, EmailForm, CustomSignupForm


class TestCustomSignupForm(TestCase):
    """Tests the custom sign up form"""

