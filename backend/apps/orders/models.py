import uuid
from django.db import models
from apps.customers.models import Customer, Address
from apps.products.models import Product

class Order(models.Model):

    class OrderStatus(models.TextChoices):
        PENDING = 'P', 'در انتظار پرداخت'
        COMPLETED = 'C', 'پرداخت موفق'
        CANCELED = 'X', 'لغو شده'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='orders'
    )

    status = models.CharField(
        max_length=1,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )

    shipping_receiver_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    shipping_phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )

    shipping_province = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    shipping_city = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    shipping_street = models.TextField(
        null=True,
        blank=True
    )

    shipping_postal_code = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order {self.id} - {self.customer.user.username}"
# class Order(models.Model):
#     # ۱. تعریف وضعیت‌های مختلف یک سفارش با استفاده از TextChoices
#     class OrderStatus(models.TextChoices):
#         PENDING = 'P', 'در انتظار پرداخت'
#         COMPLETED = 'C', 'پرداخت موفق'
#         CANCELED = 'X', 'لغو شده'
#     # ۲. شناسه یکتا و غیرقابل حدس برای پیگیری سفارش
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     # ۳. ارتباط با مشتری (سفارش برخلاف سبد خرید، حتماً صاحب دارد)
#     customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders') 
#     # ۴. وضعیت فعلی سفارش
#     status = models.CharField(
#         max_length=1, 
#         choices=OrderStatus.choices, 
#         default=OrderStatus.PENDING
#     )
#     # ۵. زمان ثبت سفارش
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"Order {self.id} - {self.customer.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    # 6. The most important field of this phase: Freezing the price!
    # ۶. مهم‌ترین فیلد این فاز: فریز کردن قیمت!
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"








