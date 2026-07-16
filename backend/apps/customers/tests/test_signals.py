from django.test import TestCase

from apps.accounts.models import CustomUser
from apps.customers.models import Customer


class CustomerSignalTest(TestCase):

    def test_signal_creates_customer(self):

        user = CustomUser.objects.create_user(
            username='signal_user',
            email='signal@test.com',
            password='12345678'
        )

        self.assertTrue(
            Customer.objects.filter(
                user=user
            ).exists()
        )

    def test_only_one_customer_created(self):

        user = CustomUser.objects.create_user(
            username='signal_user2',
            email='signal2@test.com',
            password='12345678'
        )

        self.assertEqual(
            Customer.objects.filter(
                user=user
            ).count(),
            1
        )

    
