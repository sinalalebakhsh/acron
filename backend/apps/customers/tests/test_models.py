# apps/customers/tests/test_models.py
from django.test import TestCase

from apps.accounts.models import CustomUser
from apps.customers.models import Customer


class CustomerModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='sina',
            email='sina@test.com',
            password='12345678'
        )

    def test_customer_created_by_signal(self):
        self.assertTrue(
            Customer.objects.filter(
                user=self.user
            ).exists()
        )

    def test_customer_has_uuid(self):
        customer = self.user.customer

        self.assertIsNotNone(
            customer.uuid
        )

    def test_customer_str(self):
        customer = self.user.customer

        self.assertEqual(
            str(customer),
            self.user.username
        )
    
