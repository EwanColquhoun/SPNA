from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from .models import SPNAMember

from .forms import ProfileForm, DocumentForm, EmailForm, CustomSignupForm


class TestNonSuperUserAccess(TestCase):
    """Tests the views to ensure that a non superuser can't access them"""

    def test_member_area_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'member/member-area.html')
        # self.assertRedirects(response, '/accounts/login/?next=/member/')

    def test_profile_view(self):
        response = self.client.get('/member/profile/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/member/profile/')
        self.assertTemplateNotUsed(response, 'member/profile.html')


class TestSuperUserAccess(TestCase):
    """Tests the superuser access"""

    def setUp(self):
        """Creates an instance of a Superuser for checking admin functions/views."""
        self.user = User.objects.create_superuser(
            username='UserForTest',
            email='email@emailtest.com',
            password='secret',
        )
        self.user.spnamember.paid = True
        self.user.save()
        self.client = Client()
        self.client.login(username='UserForTest', password='secret')

    def test_member_area_view(self):
        response = self.client.get('/member/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'member/member-area.html')
        self.assertTemplateNotUsed(response, 'home/index.html')

    def test_profile_view(self):
        response = self.client.get('/member/profile/')
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, 'home')
        self.assertTemplateUsed(response, 'member/profile.html')
        # self.assertTemplateNotUsed(response, 'member/profile.html')