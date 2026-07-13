from datetime import date

from rest_framework import serializers

from .models import Customer

from apps.accounts import models as accounts_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = accounts_models.CustomUser

        fields = [
            'id',
            'username',
            'email',
        ]




class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Customer

        fields = [
            'id',
            'uuid',
            'phone_number',
            'birth_date',
            'user',
        ]
        read_only_fields = [
            'id',
            'uuid',
            'user',
        ]

    def validate_phone_number(self, value):
        if value and len(value)<10:
                raise serializers.ValidationError(
                "Phone number is too short."
                    )
        
        return value

    def validate_birth_date(self, value):

        if value and value > date.today():
            raise serializers.ValidationError(
                "Birth date cannot be in future."
            )

        return value



from rest_framework import serializers
from .models import Customer, Address
from django.contrib.auth import get_user_model

User = get_user_model()

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'province', 'city', 'street', 'postal_code']

class CustomerProfileSerializer(serializers.ModelSerializer):
    # دریافت نام و ایمیل از جدول User (به صورت فقط‌خواندنی)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    
    # نمایش لیست آدرس‌های کاربر
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'addresses']

        
