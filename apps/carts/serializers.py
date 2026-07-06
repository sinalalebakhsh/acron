from rest_framework import serializers
from .models import Cart, CartItem
from apps.products.models import Product

# ۱. ساخت یک سریالایزر سبک و بهینه برای محصول داخل سبد خرید
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # ما در سبد خرید به توضیحات طولانی یا برند نیازی نداریم، فقط اطلاعات حیاتی!
        fields = ['id', 'name', 'price', 'main_image']


# ۲. سریالایزر آیتم‌های داخل سبد (CartItem)
class CartItemSerializer(serializers.ModelSerializer):
    # نمایش اطلاعات محصول به صورت تو در تو، اما با سریالایزر سبک
    product = SimpleProductSerializer(read_only=True)
    
    # تعریف یک فیلد محاسباتی که در دیتابیس وجود ندارد
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    # متد متصل به فیلد محاسباتی بالا
    def get_total_price(self, cart_item: CartItem):
        # قیمت محصول × تعداد آن
        return cart_item.quantity * cart_item.product.price


# ۳. سریالایزر اصلی سبد خرید (Cart)
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    # اتصال آیتم‌ها به سبد خرید (توجه: کلمه items همان related_name در مدل است)
    items = CartItemSerializer(many=True, read_only=True)
    
    # فیلد محاسباتی برای جمع کل مبلغ کل سبد خرید
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'grand_total']

    # متد متصل به فیلد محاسباتی مبلغ کل
    def get_grand_total(self, cart: Cart):
        # یک حلقه پایتونی برای جمع زدن قیمت کل تک‌تک آیتم‌های این سبد
        return sum([item.quantity * item.product.price for item in cart.items.all()])
    

