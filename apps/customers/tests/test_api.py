from rest_framework.test import APITestCase
from rest_framework import status

from apps.accounts.models import CustomUser


class CustomerMeApiTest(APITestCase):

    def setUp(self):

        self.user = CustomUser.objects.create_user(
            username='api_user',
            email='api@test.com',
            password='12345678'
        )

    def test_authentication_required(self):

        response = self.client.get(
            '/api/customers/me/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_get_customer_profile(self):

        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.get(
            '/api/customers/me/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['user']['username'],
            self.user.username
        )

    def test_patch_customer_profile(self):

        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.patch(
            '/api/customers/me/',
            {
                'phone_number': '09121234567'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['phone_number'],
            '09121234567'
        )
    
    