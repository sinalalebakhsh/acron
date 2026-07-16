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
    

# این کلاس فقط برای زمانی است که کلاینت می‌خواهد محصولی را به سبد اضافه کند (POST)
class AddCartItemSerializer(serializers.ModelSerializer):
    # کلاینت فقط این دو شناسه را برای ما می‌فرستد
    product_id = serializers.IntegerField()
    cart_id = serializers.UUIDField()

    class Meta:
        model = CartItem
        fields = ['id', 'cart_id', 'product_id', 'quantity']

    # اعتبارسنجی: آیا این محصول اصلاً در فروشگاه وجود دارد؟
    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("محصولی با این شناسه یافت نشد.")
        return value

    # اعتبارسنجی: آیا این سبد خرید اصلاً وجود دارد؟
    def validate_cart_id(self, value):
        if not Cart.objects.filter(id=value).exists():
            raise serializers.ValidationError("سبد خریدی با این شناسه یافت نشد.")
        return value

    # قلب تپنده این بخش: تغییر رفتار ذخیره‌سازی برای دور زدن خطای دیتابیس
    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            # سناریو ۱: آیا این محصول از قبل در این سبد خرید وجود دارد؟
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            
            # بله وجود دارد! پس فقط تعداد جدید را با تعداد قبلی جمع کن
            cart_item.quantity += quantity
            cart_item.save()
            
            self.instance = cart_item
            
        except CartItem.DoesNotExist:
            # سناریو ۲: محصول در سبد نیست. پس یک ردیف جدید در دیتابیس بساز
            self.instance = CartItem.objects.create(
                cart_id=cart_id, 
                product_id=product_id, 
                quantity=quantity
            )

        return self.instance


# این کلاس فقط برای زمانی است که کلاینت می‌خواهد تعداد را تغییر دهد (PATCH)
# مثلاً کاربر در سبد خرید دکمه + یا - را می‌زند
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']








