# apps/orders/services.py

from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.carts.models import Cart
from apps.orders.models import Order, OrderItem
from apps.products.models import Product

class OrderService:
    """
    سرویس ارشد مدیریت و پردازش فرآیند ثبت سفارش در پروژه ACRON.
    این کلاس کاملاً مستقل از ویو کار می‌کند و منطق تجاری را ایزوله نگه می‌دارد.
    """

    @classmethod
    def place_order(cls, user, cart_id: str, shipping_address: str) -> Order:
        """
        متد اصلی ثبت سفارش. 
        این متد ورودی‌های لازم را گرفته و تمام مراحل را در قالب یک تراکنش اتمیک پیش می‌برد.
        """
        
        # استفاده از context manager برای ایجاد یک Transaction اتمیک در دیتابیس.
        # چرا؟ اگر هرکدام از خطوط داخل این بلوک با خطا مواجه شوند، دیتابیس به حالت اولیه
        # برگشت می‌خورد (Rollback) و هیچ داده‌ی ناقصی ذخیره نمی‌شود.
        with transaction.atomic():
            
            # ۱. واکشی سبد خرید به همراه اقلام آن به صورت بهینه برای جلوگیری از مشکل N+1 Query
            # از select_related استفاده نمی‌کنیم چون رابطه با اقلام سبد خرید (CartItem) از نوع reverse foreign key است،
            # پس از prefetch_related استفاده می‌کنیم تا اقلام را یکبار برای همیشه لود کنیم.
            try:
                cart = Cart.objects.prefetch_related('items__product').get(id=cart_id, is_active=True)
            except Cart.DoesNotExist:
                raise ValidationError("سبد خرید معتبری یافت نشد یا این سبد خرید قبلاً منقضی شده است.")

            # ۲. بررسی اینکه آیا سبد خرید اصلاً قلم کالا دارد یا خیر
            cart_items = cart.items.all()
            if not cart_items:
                raise ValidationError("سبد خرید شما خالی است و امکان ثبت سفارش وجود ندارد.")

            # ۳. محاسبه کل مبلغ سفارش و بررسی موجودی انبار به صورت یکجا
            total_price = 0
            for item in cart_items:
                product = item.product
                
                # بررسی موجودی انبار: آیا موجودی محصول کمتر از تعداد درخواستی کاربر است؟
                if product.stock < item.quantity:
                    raise ValidationError(
                        f"موجودی کالا '{product.name}' کافی نیست. موجودی فعلی: {product.stock}"
                    )
                
                # محاسبه قیمت: تعداد ضربدر قیمت فعلی محصول
                total_price += product.price * item.quantity

            # ۴. ایجاد رکورد اصلی سفارش در دیتابیس
            # در این مرحله سفارش در حالت 'PENDING' (در انتظار پرداخت) ایجاد می‌شود.
            order = Order.objects.create(
                user=user,
                total_price=total_price,
                shipping_address=shipping_address,
                status='PENDING' # مقدار پیش‌فرض که نشان می‌دهد فرآیند پرداخت هنوز تکمیل نشده
            )

            # ۵. انتقال اقلام از سبد خرید به اقلام سفارش + فریز کردن قیمت‌ها + کسر از انبار
            for item in cart_items:
                product = item.product
                
                # فریز کردن قیمت: قیمت فعلی محصول را مستقیماً در جدول OrderItem ذخیره می‌کنیم.
                # چرا؟ اگر فردا قیمت محصول تغییر کرد، فاکتور کاربر نباید دستخوش تغییر شود.
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item.quantity,
                    price=product.price # قیمت فریز شده کالا در لحظه خرید
                )

                # کسر از انبار: موجودی محصول را به تعداد خریداری شده کاهش می‌دهیم
                product.stock -= item.quantity
                
                # ذخیره تغییرات محصول در دیتابیس (فقط فیلد stock را آپدیت می‌کنیم تا پرفورمنس بالاتر برود)
                product.save(update_fields=['stock'])

            # ۶. غیرفعال کردن سبد خرید (کاربر کارش با این سبد خرید تمام شده است)
            cart.is_active = False
            cart.save(update_fields=['is_active'])

            # خروجی متد: شیء سفارشِ ساخته شده را برمی‌گردانیم تا لایه‌های بالاتر از آن استفاده کنند
            return order


