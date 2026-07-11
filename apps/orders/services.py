# import the necessary modules and classes
from django.db import transaction
# import the ValidationError exception from the Django REST framework,
# which will be used to raise validation errors during the order creation process.
from rest_framework.exceptions import ValidationError
# import the Cart model from the carts app, which represents a shopping cart in the system.
from apps.carts.models import Cart
# import the Order and OrderItem models from the orders app, which represent an order and its items in the system.
from apps.orders.models import Order, OrderItem

# import the Product model from the products app, which represents a product in the system.
# This import is necessary because the order creation process involves checking product inventory and freezing product prices.
# why we need it?
# because when we create an order from a cart, 
# we need to check the inventory of each product in the cart 
# and freeze its price at the time of order creation. 
# Therefore, we need to import the Product model to access its inventory and price fields.
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


