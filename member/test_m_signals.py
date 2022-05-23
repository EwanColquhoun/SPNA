from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from .models import SPNAMember


class TestSPNAModelMethods(TestCase):
    """Tests the superuser access"""

    def setUp(self):
        """Creates an instance of a Superuser for checking admin functions/views."""
        self.user = User.objects.create(
            username='UserForTest',
            email='email@emailtest.com',
            password='secret',
        )
        self.user.save()
        self.client = Client()
        self.client.login(username='UserForTest', password='secret')

    def test_signals_called(self):
        self.user.spnamember.nursery = 'Test Nursery'
        self.user.save()
        self.assertIsInstance(self.user, User)
        instance = SPNAMember.objects.filter(nursery = 'Test Nursery')[0]
        self.assertEqual(instance.nursery, 'Test Nursery')
