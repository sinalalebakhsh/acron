from django.db import transaction

from rest_framework.exceptions import ValidationError

from apps.carts.models import Cart

from apps.orders.models import Order, OrderItem

class OrderService:
    
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


