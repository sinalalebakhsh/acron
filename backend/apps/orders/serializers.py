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
        fields = [
            'id',
            'customer',
            'status',
            'created_at',
            'items',
            'total_price',
            'shipping_receiver_name',
            'shipping_phone_number',
            'shipping_province',
            'shipping_city',
            'shipping_street',
            'shipping_postal_code',
        ]
    def get_total_price(self, obj):
        # محاسبه مجموع قیمت فاکتور بر اساس اقلام
        return sum(item.quantity * item.unit_price for item in obj.items.all())

class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    address_id = serializers.IntegerField()


    