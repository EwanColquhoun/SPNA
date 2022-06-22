from datetime import date, timedelta

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


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

    def test_spnamember_has_paid(self):
        self.assertFalse(
            self.user.spnamember.has_paid(),
            "Initial user should have empty paid_until attr"
        )

    def test_different_date_values(self):
        current_date = date.today()
        _30days = timedelta(days=30)
        self.user.spnamember.set_paid_until(current_date + _30days)

        self.assertTrue(
            self.user.spnamember.has_paid(
                current_date=current_date
            )
        )

    def test_date_in_the_past(self):
        current_date = date.today()
        _30days = timedelta(days=30)

        self.user.spnamember.set_paid_until(current_date - _30days)

        self.assertFalse(
            self.user.spnamember.has_paid(
                current_date=current_date
            )
        )
