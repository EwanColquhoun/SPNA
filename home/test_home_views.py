from django.test import TestCase


class TestHomeViews(TestCase):
    """Ensure the views use the correct template"""

    def test_home_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')