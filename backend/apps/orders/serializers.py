# apps/orders/serializers.py

from rest_framework import serializers
from .models import Order, OrderItem

class OrderCreateInputSerializer(serializers.Serializer):
    """
    سریالایزر اختصاصی برای ولیدیشن و دریافت اطلاعات اولیه ثبت سفارش از سمت فرانت‌اند.
    این سریالایزر فاقد متد create یا update داخلی است، زیرا این وظایف به لایه سرویس منتقل شده‌اند.
    """
    cart_id = serializers.UUIDField(required=True, error_messages={'required': 'ارسال شناسه سبد خرید الزامی است.'})
    shipping_address = serializers.CharField(required=True, min_length=10, error_messages={'required': 'آدرس ارسال نمی‌تواند خالی باشد.'})


class OrderItemSerializer(serializers.ModelSerializer):
    """
    سریالایزر نمایش جزییات هر قلم کالا در فاکتور نهایی سفارش.
    """
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'quantity',]


class OrderSerializer(serializers.ModelSerializer):
    """
    سریالایزر اصلی برای خروجی دادن جزییات کامل یک سفارش به همراه اقلام تو در توی آن.
    """
    items = OrderItemSerializer(many=True, read_only=True) # نمایش اقلام سفارش به صورت Nested

    class Meta:
        model = Order
        fields = ['id',  'status', 'items', 'created_at']
    
