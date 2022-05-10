from django.test import TestCase
from django.test.client import Client

from .forms import ContactForm


class TestContactForm(TestCase):

    def test_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_email_is_required(self):
        form = ContactForm({
            'name': 'John',
            'phone_number': '12345678910',
            'email': '',
            'message': 'Test message'})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_message_is_required(self):
        form = ContactForm({
            'name': 'John',
            'phone_number': '12345678910',
            'email': 'john@john.com',
            'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, (
            'name',
            'phone_number',
            'email',
            'message'))

