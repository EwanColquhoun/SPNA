from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail

from .email import (
    welcome_email_to_member,
)

class TestSpnaEmails(TestCase):
    """Test to see if the emails sent with view calls"""

    def setUp(self):
        """Creates an instance of a Superuser for checking admin functions/views."""
        self.user = User.objects.create_superuser(
            username='UserForTest',
            email='email@emailtest.com',
            password='secret',
        )
        self.user.spnamember.nursery = 'Initial Nursery'
        self.user.spnamember.paid = True
        self.user.save()
        self.client = Client()
        self.client.login(username='UserForTest', password='secret')

    def test_welcome_email(self):
        welcome_email_to_member(self.user)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Welcome to the SPNA')
