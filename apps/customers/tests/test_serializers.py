from django.test import TestCase

from apps.accounts.models import CustomUser
from apps.customers.serializers import CustomerSerializer


class CustomerSerializerTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='serializer_user',
            email='serializer@test.com',
            password='12345678'
        )

        self.customer = self.user.customer

    def test_serializer_contains_expected_fields(self):

        serializer = CustomerSerializer(
            self.customer
        )

        data = serializer.data

        self.assertIn('id', data)
        self.assertIn('uuid', data)
        self.assertIn('phone_number', data)
        self.assertIn('birth_date', data)
        self.assertIn('user', data)

    def test_nested_user_serializer(self):

        serializer = CustomerSerializer(
            self.customer
        )

        user_data = serializer.data['user']

        self.assertEqual(
            user_data['username'],
            self.user.username
        )

        self.assertEqual(
            user_data['email'],
            self.user.email
        )

