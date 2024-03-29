from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from news.models import Articles
from news.forms import ArticleForm
from member.models import Document
from member.forms import DocumentForm
from contact.models import Contact


class TestSpnaAdminSuperuserViews(TestCase):
    """Tests the main functions on the SPNA Admin page"""

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

    def test_can_send_email_form(self):
        """Tests the send email view"""
        contact = Contact.objects.create(
            name='Email test contact',
            email='contact@email.com',
            message='Test contact message')

        email = {
            'email_to': 'contact@email.com',
            'email_subject': 'Test Subject',
            'email_body': 'Test email body'}
        replied = contact.replied
        self.assertFalse(replied)
        response = self.client.post('/spna_admin/send/', email)
        self.assertRedirects(response, '/spna_admin/')
        updated_contact = Contact.objects.filter(id=contact.id)[0]
        self.assertTrue(updated_contact.replied)

    def test_can_add_article(self):
        existing_articles = Articles.objects.all().count()
        self.assertEqual(existing_articles, 0)
        form = ArticleForm({
            'title':'Test Article',
            'content':'Test article content', })
        self.client.post('/spna_admin/add/article/', form.data)
        total_articles = Articles.objects.all().count()
        self.assertEqual(total_articles, 1)

    def test_article_form_invalid_view(self):
        form = ArticleForm({
            'title':'',
            'content':'Test article content', })
        response = self.client.post('/spna_admin/add/article/', form.data)
        self.assertTemplateUsed('/spna_admin/edit_article.html')
        total_articles = Articles.objects.all().count()
        self.assertEqual(total_articles, 0)
        self.assertEqual(response.status_code, 200)

    def test_can_edit_article(self):
        article = Articles.objects.create(
            title='Test Article', content='Great news about the Django tests', )
        total_articles = Articles.objects.all().count()
        self.assertEqual(total_articles, 1)
        form_data = {
            'title':'Edited Test Article',
            'content':'Edited content',
        }
        response = self.client.post(f'/spna_admin/edit/{article.id}', form_data)
        self.assertRedirects(response, '/news/')
        edited_article = Articles.objects.get(id=article.id)
        self.assertEqual(edited_article.title, 'Edited Test Article')
        self.assertEqual(article.id, edited_article.id)

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
            name='Test Contact Name',
            email='contact@email.com',
            message='Great news about the Django tests', )
        existing_contacts = Contact.objects.filter(id=test_contact.id)
        self.assertEqual(len(existing_contacts), 1)
        response = self.client.get(f'/spna_admin/delete/contact/{test_contact.id}')
        self.assertRedirects(response, '/spna_admin/')
        current_contacts = Articles.objects.filter(id=test_contact.id)
        self.assertEqual(len(current_contacts), 0)

    def test_can_add_document(self):
        existing_doc = Document.objects.all().count()
        self.assertEqual(existing_doc, 0)
        doc = SimpleUploadedFile(
            "test_document.txt",
            b"Document contents for test"
        )
        form = DocumentForm({
            'title':'A Test Document',
            'category':'1',
            'doc':doc,
        })
        self.client.post('/spna_admin/add/document/', form.data)
        self.assertTrue(form.is_valid)
        total_docs = Document.objects.all().count()
        self.assertEqual(total_docs, 1)


class TestNonSuperUserAccess(TestCase):
    """Tests the views to ensure that a non superuser can't access them"""

    def test_spna_admin_view(self):
        response = self.client.get('/spna_admin/')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'spna_admin/spna_admin.html')

    def test_user_cannot_edit_article_view(self):
        test_article = Articles.objects.create(
            title='Test Article', content='Great news about the Django tests', )
        response = self.client.get(f'/spna_admin/edit/{test_article.id}')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'spna_admin/edit_article.html')

    def test_user_cannot_delete_article_view(self):
        test_article = Articles.objects.create(
            title='Test Article', content='Great news about the Django tests', )
        response = self.client.post(f'/spna_admin/delete/article/{test_article.id}')
        self.assertEqual(response.status_code, 302)
        current_articles = Articles.objects.filter(id=test_article.id)
        self.assertEqual(len(current_articles), 1)

    def test_user_cannot_add_article_view(self):
        test_article = {
            'title':'Test Article',
            'content':'A spam article from a user'
        }
        response = self.client.post('/spna_admin/add/article/', test_article)
        self.assertEqual(response.status_code, 302)
        current_articles = Articles.objects.all()
        self.assertEqual(len(current_articles), 0)

    def test_user_cannot_add_document_view(self):
        test_doc = {
            'title':'Test Document',
            'content':'A spam document from a user'
        }
        response = self.client.post('/spna_admin/add/document/', test_doc)
        self.assertEqual(response.status_code, 302)
        current_docs = Document.objects.all()
        self.assertEqual(len(current_docs), 0)


class TestSecureSuperUserAccess(TestCase):
    """Tests to ensure sensitive views are superuser access only"""

    def test_csv_access(self):
        """CSV access only for superusers"""
        response = self.client.get('/spna_admin/csv/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/spna_admin/csv/')

    def test_no_spna_admin_access(self):
        """SPNA_admin access only for superusers"""
        response = self.client.get('/spna_admin/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/spna_admin/')
        self.assertTemplateNotUsed('/spna_admin/spna_admin.html')
