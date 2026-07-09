from rest_framework import serializers
from .models import Order, OrderItem
from apps.carts.models import Cart
from .services import OrderService

# ۱. سریالایزر نمایش آیتم‌های فاکتور
# 1. Serializer to display invoice items
class OrderItemSerializer(serializers.ModelSerializer):
    # برای نمایش نام محصول به جای فقط آی‌دی آن
    # To display the product name instead of just its ID
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'quantity', 'unit_price']


# ۲. سریالایزر نمایش کل فاکتور
#2. Serializer to display the entire invoice
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'status', 'created_at', 'items']


# ۳. سریالایزر عملیاتی: فقط برای دریافت آی‌دی سبد خرید و ساخت فاکتور
# 3. Operational Serializer: Only for getting the shopping cart ID and creating the invoice
class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        # بررسی اینکه آیا این سبد خرید اصلاً وجود دارد؟
        # Check if this shopping cart even exists?
        if not Cart.objects.filter(id=cart_id).exists():
            raise serializers.ValidationError("سبد خرید نامعتبر است یا قبلا پرداخت شده است.")
        return cart_id

    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        
        # استخراج مشتری از ریکوئست (کاربر باید لاگین باشد)
        # ما request را از طریق context از سمت View به اینجا پاس می‌دهیم
        # Extract the customer from the request (user must be logged in)
        # We pass the request here via context from the View side
        customer = self.context['request'].user.customer
        
        # فراخوانی لایه سرویس که در مرحله قبل ساختیم!
        # Call the service layer we created in the previous step!
        order = OrderService.create_order_from_cart(cart_id=cart_id, customer=customer)
        
        return order
    


