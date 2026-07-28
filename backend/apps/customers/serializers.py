from datetime import date
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Customer, Address
from apps.accounts import models as accounts_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = accounts_models.CustomUser
        fields = ['id','username','email',]




class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Customer

        fields = ['id','uuid','phone_number','birth_date','user',]
        read_only_fields = ['id','uuid','user',]

    def validate_phone_number(self, value):
        if value and len(value)<10:
                raise serializers.ValidationError("Phone number is too short.")
        
        return value

    def validate_birth_date(self, value):

        if value and value > date.today():
            raise serializers.ValidationError("Birth date cannot be in future.")

        return value




User = get_user_model()




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id', 'title', 'receiver_name', 'phone_number',
            'province', 'city', 'street', 'postal_code',
            'is_default', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class CustomerProfileSerializer(serializers.ModelSerializer):
    addresses = serializers.SerializerMethodField()
    customer_phone = serializers.CharField(source='customer.phone_number', read_only=True)
    birth_date = serializers.DateField(source='customer.birth_date', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 
            'last_name', 'customer_phone', 'birth_date', 'addresses'
        ]

    def get_addresses(self, obj):
        # دریافت لیست آدرس‌ها از طریق رابطه Customer
        if hasattr(obj, 'customer'):
            addresses = obj.customer.addresses.all()
            return AddressSerializer(addresses, many=True).data
        return []   




