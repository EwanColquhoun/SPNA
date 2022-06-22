from django.test import TestCase
from django.core import mail

from .forms import ContactForm


class TestContactView(TestCase):
    """Checks the contact view actions correctly"""

    def test_contact_form_posts(self):
        """If contact is valid and posted an email is sent to admin."""
        data = ({
            'name':'Test Contact',
            'phone':'0123456789',
            'email':'contact@email.com',
            'message':'Test contact message'
        })
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/contact/contact/send', data)
        self.assertRedirects(response, '/')
        self.assertEqual(len(mail.outbox), 1)

    def test_contact_does_not_post(self):
        """If form is not valid it should redirect to home"""
        form = ContactForm({
            'name': '',
            'phone_number': '12345678910',
            'email': '',
            'message': 'Test contact message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(mail.outbox), 0)
        response = self.client.post('/contact/contact/send', form.data)
        self.assertEqual(len(mail.outbox), 0)
        self.assertRedirects(response, '/')


