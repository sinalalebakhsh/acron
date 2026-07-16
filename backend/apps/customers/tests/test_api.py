import datetime

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
    
    def test_patch_invalid_phone_number(self):
        # ۱. احراز هویت کاربر
        self.client.force_authenticate(user=self.user)
        
        # ۲. ارسال درخواست ویرایش با شماره تلفن غلط (کمتر از 10 کاراکتر)
        response = self.client.patch(
            '/api/customers/me/',
            {
                'phone_number': '123' 
            },
            format='json'
        )

        # ۳. بررسی اینکه آیا سیستم خطای 400 داده است؟
        # (Bad Request)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # ۴. بررسی اینکه آیا خطا دقیقاً مربوط به فیلد 
        # phone_number
        #  است؟
        self.assertIn('phone_number', response.data)


    def test_patch_future_birth_date(self):
        self.client.force_authenticate(user=self.user)
        
        # ۱. ساخت یک تاریخ در آینده (مثلاً 10 روز بعد از امروز)
        future_date = (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        
        # ۲. ارسال تاریخ آینده به سرور
        response = self.client.patch(
            '/api/customers/me/',
            {
                'birth_date': future_date
            },
            format='json'
        )

        # ۳. بررسی اینکه آیا سیستم خطای 400 داده است؟
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        
        # ۴. بررسی اینکه آیا خطا مربوط به فیلد 
        # birth_date
        #  است؟
        self.assertIn('birth_date', response.data)




