from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.carts.models import Cart
from apps.customers.models import Customer, Address
from apps.orders.models import Order, OrderItem


class OrderService:
    """
    سرویس اصلی ثبت سفارش در پروژه ACRON.
    """

    @classmethod
    @transaction.atomic
    def place_order(
        cls,
        user,
        cart_id: str,
        address_id: int,
    ) -> Order:

        # --------------------------------------------------
        # 1. پیدا کردن Customer مربوط به کاربر جاری
        # --------------------------------------------------

        try:
            customer = Customer.objects.get(user=user)
        except Customer.DoesNotExist:
            raise ValidationError(
                "پروفایل مشتری برای این کاربر یافت نشد."
            )

        # --------------------------------------------------
        # 2. دریافت Cart
        # --------------------------------------------------

        try:
            cart = (
                Cart.objects
                .prefetch_related("items__product")
                .get(id=cart_id)
            )
        except Cart.DoesNotExist:
            raise ValidationError(
                "سبد خرید معتبری یافت نشد."
            )

        # --------------------------------------------------
        # 3. بررسی مالکیت Cart
        # --------------------------------------------------

        if cart.customer_id != customer.id:
            raise ValidationError(
                "این سبد خرید متعلق به شما نیست."
            )

        # --------------------------------------------------
        # 4. بررسی خالی نبودن Cart
        # --------------------------------------------------

        cart_items = list(cart.items.all())

        if not cart_items:
            raise ValidationError(
                "سبد خرید شما خالی است و امکان ثبت سفارش وجود ندارد."
            )

        # --------------------------------------------------
        # 5. دریافت Address
        # --------------------------------------------------

        try:
            address = Address.objects.get(
                id=address_id,
                customer=customer,
            )
        except Address.DoesNotExist:
            raise ValidationError(
                "آدرس انتخاب‌شده یافت نشد."
            )

        # --------------------------------------------------
        # 6. ایجاد Order
        # --------------------------------------------------

        order = Order.objects.create(
            customer=customer,
            status=Order.OrderStatus.PENDING,

            # Snapshot آدرس در لحظه ثبت سفارش
            shipping_receiver_name=address.receiver_name,
            shipping_phone_number=address.phone_number,
            shipping_province=address.province,
            shipping_city=address.city,
            shipping_street=address.street,
            shipping_postal_code=address.postal_code,
        )

        # --------------------------------------------------
        # 7. انتقال محصولات به OrderItem
        # --------------------------------------------------

        for item in cart_items:

            product = item.product

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity,
                unit_price=product.price,
            )

        # --------------------------------------------------
        # 8. حذف Cart پس از ایجاد موفق Order
        # --------------------------------------------------

        cart.delete()

        return order