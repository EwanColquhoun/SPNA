from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import ProfileForm, DocumentForm, EmailForm, CustomSignupForm
from .models import Document

import os


class TestCustomSignupForm(TestCase):
    """Tests the custom sign up form"""

    def test_form_validated(self):
        """Tests the form validates with required fields."""
        form = CustomSignupForm({
            'fullname': 'TestSPNAUser',
            'nursery': 'TestNursery',
            'email': 'testemail@email.com',
            'email2': 'testemail@email.com',
            'subscription': 'Monthly',
            'password1': 'testpassword',
            'password2': 'testpassword',})
        self.assertTrue(form.is_valid())

    def test_username_required(self):
        form = CustomSignupForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_first_name_required(self):
        form = CustomSignupForm({'nursery': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('nursery', form.errors.keys())
        self.assertEqual(form.errors['nursery'][0],
                         'This field is required.')

    def test_last_name_required(self):
        form = CustomSignupForm({'subscription': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subscription', form.errors.keys())
        self.assertEqual(form.errors['subscription'][0],
                         'This field is required.')

    def test_email_required(self):
        form = CustomSignupForm({'fullname': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('fullname', form.errors.keys())
        self.assertEqual(form.errors['fullname'][0],
                         'This field is required.')

    def test_message_required(self):
        form = CustomSignupForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors.keys())
        self.assertEqual(form.errors['password1'][0],
                         'This field is required.')


class TestProfileForm(TestCase):
    """Tests the form exludes the fields from the view."""

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProfileForm()
        self.assertEqual(form.Meta.exclude, (
           'user',
           'subscription', 
           'paid_until',
           'paid',
           'stripe_id',
           'sub_id',
           'has_cancelled'))


class TestEmailForm(TestCase):
    """Ensures there is always an address, subject and body"""

    def test_email_to_is_required(self):
        form = EmailForm({'email_to': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_to', form.errors.keys())
        self.assertEqual(form.errors['email_to'][0], 'This field is required.')

    def test_email_subject_is_required(self):
        form = EmailForm({
            'email_to': 'email@email.com',
            'email_subject': '',
            'email_body': 'Test email body'})
        self.assertFalse(form.is_valid())
        self.assertIn('email_subject', form.errors.keys())
        self.assertEqual(form.errors['email_subject'][0], 'This field is required.')

    def test_email_body_is_required(self):
        form = EmailForm({
            'email_to': 'email@email.com',
            'email_subject': 'Test Email',
            'email_body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email_body', form.errors.keys())
        self.assertEqual(form.errors['email_body'][0], 'This field is required.')


class TestDocumentForm(TestCase):

    def test_document_form_valid(self):
        doc = SimpleUploadedFile(
            "test_document.txt",
            b"Document contents for test"
        )
        other_data = {
            'doc':doc,
        }
        form_data = {
            'title':'A Test Document',
            'category':'1',
        }
        form = DocumentForm(form_data, other_data)
        self.assertTrue(form.is_valid())

    def test_document_form_not_valid(self):
        form = DocumentForm({
            'title':'A Test Document',
            'doc':'',
            'category':'1',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('doc', form.errors.keys())
        self.assertEqual(form.errors['doc'][0], 'This field is required.')
            