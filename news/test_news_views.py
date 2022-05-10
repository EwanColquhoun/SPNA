from django.test import TestCase


class TestInitiativesView(TestCase):
    """Test the correct view is called"""

    def test_initiatives_view(self):
        response = self.client.get('/news/initiatives/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/initiatives.html')


class TestNewsView(TestCase):
    """Test the correct view is called"""

    def test_news_view(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news.html')
