# apps/orders/serializers.py

from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'created_at', 'items', 'total_price']
    def get_total_price(self, obj):
        # محاسبه مجموع قیمت فاکتور بر اساس اقلام
        return sum(item.quantity * item.unit_price for item in obj.items.all())

class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    shipping_address = serializers.CharField(min_length=10)


    