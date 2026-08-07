from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.carts.models import Cart
from apps.orders.models import Order, OrderItem
from apps.customers.models import Customer

class OrderService:
    """
    سرویس ارشد مدیریت و پردازش فرآیند ثبت سفارش در پروژه ACRON.
    """
    @classmethod
    def place_order(cls, user, cart_id: str, shipping_address: str) -> Order:
        """
        متد ثبت سفارش با رعایت کامل ساختار مدل‌های Order و OrderItem.
        """
        with transaction.atomic(): 
            # ۱. یافتن پروفایل مشتری (Customer) متصل به کاربر جاری
            try:
                customer = Customer.objects.get(user=user)
            except Customer.DoesNotExist:
                raise ValidationError("پروفایل مشتری برای این کاربر یافت نشد.")

            # ۲. واکشی سبد خرید به همراه اقلام آن
            try:
                cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
            except Cart.DoesNotExist:
                raise ValidationError("سبد خرید معتبری یافت نشد.")

            # ۳. بررسی خالی نبودن سبد خرید
            cart_items = cart.items.all()
            if not cart_items:
                raise ValidationError("سبد خرید شما خالی است و امکان ثبت سفارش وجود ندارد.")

            # ۴. ایجاد رکورد اصلی سفارش در دیتابیس (مطابق با مدل Order)
            order = Order.objects.create(
                customer=customer,
                status=Order.OrderStatus.PENDING  # مقدار 'P'
            )

            # ۵. انتقال اقلام به سفارش و فریز کردن قیمت در فیلد unit_price
            for item in cart_items:
                product = item.product
                
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item.quantity,
                    unit_price=product.price  # ذخیره قیمت فریز شده کالا
                )

            # ۶. پاکسازی سبد خرید پس از ثبت موفق سفارش
            cart.delete()

            return order