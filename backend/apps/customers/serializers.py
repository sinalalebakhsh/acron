from rest_framework import serializers
from .models import Customer, Address

class AddressSerializer(serializers.ModelSerializer):
    """
    سریالایزر برای تبدیل مدل آدرس به JSON و برعکس
    """
    class Meta:
        model = Address
        fields = [
            'id', 
            'title', 
            'receiver_name', 
            'phone_number', 
            'province', 
            'city', 
            'street', 
            'postal_code', 
            'is_default'
        ]
        read_only_fields = ['id']

class CustomerSerializer(serializers.ModelSerializer):
    """
    سریالایزر ساده برای اطلاعات کلی مشتری
    """
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'phone_number']

class CustomerProfileSerializer(serializers.ModelSerializer):
    """
    سریالایزر کامل برای صفحه پروفایل (شامل اطلاعات کاربری و لیست آدرس‌ها)
    """
    # خواندن فیلدهای مرتبط از مدل User از طریق رابطه OneToOne
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    customer_phone = serializers.CharField(source='phone_number', read_only=True)
    # دریافت آدرس‌های مرتبط با این مشتری (سریالایزر چندتایی)
    addresses = AddressSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'customer_phone', 
            'addresses'
        ]


        