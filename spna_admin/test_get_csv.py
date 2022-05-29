from django.test import TestCase
from spna_admin.get_csv import fields_list

class TestGetCsvVariables(TestCase):
    """Tests to ensure the variables are correct"""

    def test_fields_are_correct(self):
        """Checks the fields printed aren't altered."""
        fields = fields_list
        text = [
            'user',
            'user__email',
            'user__first_name',
            'user__last_name',
            'user__date_joined',
            'nursery',
            'fullname',
            'street_address1',
            'town_or_city',
            'postcode',
            'country',
            'phone',
            'subscription',
            'paid_until',
        ]
        self.assertEqual(fields, text)
