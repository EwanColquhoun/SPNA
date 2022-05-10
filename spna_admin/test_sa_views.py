from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from news.models import Articles
from contact.models import Contact

class Test_SPNA_Admin_Views(TestCase):

    def setUp(self):
        """Creates an instance of a Superuser for checking admin functions/views."""
        self.user = User.objects.create_superuser(username='testAdminUser',
                                              email='test@email.com',
                                              password='',
                                              )
        self.user.set_password('secret')
        self.user.save()
        self.client = Client()
        self.client.login(username='testAdminUser', password='secret')

    def test_spna_admin_page(self):
        response = self.client.get('/spna_admin/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'spna_admin/spna_admin.html')

    def test_can_delete_article(self):
        test_article = Articles.objects.create(
            title='Test Article', content='Great news about the Django tests', )
        existing_articles = Articles.objects.filter(id=test_article.id)
        self.assertEqual(len(existing_articles), 1)
        response = self.client.get(f'/spna_admin/delete/article/{test_article.id}')
        self.assertRedirects(response, '/news/')
        current_articles = Articles.objects.filter(id=test_article.id)
        self.assertEqual(len(current_articles), 0)

    def test_can_delete_contact(self):
        test_contact = Contact.objects.create(
            name='Test Contact Name', email='contact@email.com', message='Great news about the Django tests', )
        existing_contacts = Contact.objects.filter(id=test_contact.id)
        self.assertEqual(len(existing_contacts), 1)
        response = self.client.get(f'/spna_admin/delete/contact/{test_contact.id}')
        self.assertRedirects(response, '/spna_admin/')
        current_contacts = Articles.objects.filter(id=test_contact.id)
        self.assertEqual(len(current_contacts), 0)