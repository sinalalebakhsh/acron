from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from rest_framework.exceptions import ValidationError

from apps.carts.models import Cart

from apps.orders.models import Order, OrderItem


class OrderService:
    """
    This service takes a shopping cart and converts it into a finalized invoice (order).
    """  
    @staticmethod
    @transaction.atomic
    def create_order_from_cart(cart_id, customer):
        """
        این سرویس یک سبد خرید را می‌گیرد و آن را به یک فاکتور قطعی تبدیل می‌کند.
        """
        # ۱. پیدا کردن سبد خرید به همراه آیتم‌ها و محصولاتش (برای جلوگیری از N+1)
        try:
            cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
        except Cart.DoesNotExist:
            raise ValidationError("سبد خرید یافت نشد یا قبلاً پرداخت شده است.")

        # ۲. اگر سبد خرید خالی بود، اجازه ساخت فاکتور نده!
        if cart.items.count() == 0:
            raise ValidationError("سبد خرید شما خالی است.")

        # ۳. ساخت فاکتور اولیه (Header)
        order = Order.objects.create(customer=customer)

        # ۴. تبدیل تک‌تک آیتم‌های سبد به آیتم‌های فاکتور
        order_items_to_create = []
        for cart_item in cart.items.all():
            product = cart_item.product
            
            # بررسی موجودی انبار در لحظه آخر
            if product.inventory < cart_item.quantity:
                raise ValidationError(f"موجودی محصول '{product.name}' کافی نیست.")

            # کسر از موجودی انبار
            product.inventory -= cart_item.quantity
            product.save()

            # آماده‌سازی آیتم فاکتور (دقت کنید قیمت همین الان فریز می‌شود)
            order_items_to_create.append(
                OrderItem(
                    order=order,
                    product=product,
                    quantity=cart_item.quantity,
                    unit_price=product.price  # فریز کردن قیمت!
                )
            )

        # ۵. ذخیره یکجای تمام آیتم‌ها در دیتابیس (بسیار بهینه‌تر از ذخیره تک‌تک)
        OrderItem.objects.bulk_create(order_items_to_create)

        # ۶. حذف سبد خرید (چون تبدیل به فاکتور شد)
        cart.delete()

        return order

    @staticmethod
    @transaction.atomic
    def cancel_expired_order(order):
        """
        این متد فاکتور را لغو کرده و موجودی کالاها را به انبار برمی‌گرداند.
        """
        # اگر وضعیت فاکتور چیزی غیر از "در انتظار پرداخت" است، کاری نکن
        if order.status != Order.OrderStatus.PENDING:
            return False

        # حلقه روی تمام آیتم‌های فاکتور برای بازگرداندن موجودی
        # استفاده از select_related برای جلوگیری از مشکل N+1 در ارتباط با جدول Product
        for item in order.items.select_related('product'):
            product = item.product
            product.inventory += item.quantity
            product.save()

        # تغییر وضعیت فاکتور به لغو شده
        order.status = Order.OrderStatus.CANCELED
        order.save()
        return True

    @staticmethod
    def validate_order_for_payment(order_id):
        """
        این متد قبل از ارسال کاربر به درگاه بانکی فراخوانی می‌شود
        تا بررسی کند آیا هنوز برای پرداخت فرصت دارد یا خیر.
        """
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise ValidationError("سفارش یافت نشد.")

        if order.status == Order.OrderStatus.COMPLETED:
            raise ValidationError("این سفارش قبلاً پرداخت شده است.")
            
        if order.status == Order.OrderStatus.CANCELED:
            raise ValidationError("این سفارش لغو شده است.")

        # محاسبه زمان انقضا (زمان ثبت فاکتور + ۱۵ دقیقه)
        expiration_time = order.created_at + timedelta(minutes=15)
        
        # مقایسه با زمان حال
        if timezone.now() > expiration_time:
            # فراخوانی متد بازگرداندن موجودی به انبار
            OrderService.cancel_expired_order(order)
            raise ValidationError("زمان ۱۵ دقیقه‌ای پرداخت به پایان رسیده و سفارش به دلیل اتمام مهلت لغو شد.")
        
        return order




