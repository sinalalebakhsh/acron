#  import models from django.db for defining the Payment model
from django.db import models

# import uuid for generating unique transaction IDs
import uuid

#  import the Order model from the orders app to establish a relationship with the Payment model
from apps.orders.models import Order

# Define the Payment model to represent payment transactions associated with orders
class Payment(models.Model):
    """
    Model representing a payment transaction for an order.
    Each order can have only one active payment record.
    """
    class PaymentStatus(models.TextChoices):
        PENDING = 'P', 'در انتظار پرداخت'
        SUCCESS = 'S', 'موفق'
        FAILED = 'F', 'ناموفق'

    # هر فاکتور فقط یک رکورد پرداخت فعال دارد
    # var order is a one-to-one relationship with the Order model, 
    # ensuring that each order can have only one associated payment record.
    # The on_delete=models.PROTECT option prevents deletion of the order if a payment exists,
    # and related_name='payment' allows reverse access from the Order model to its associated Payment.
    order = models.OneToOneField(Order, on_delete=models.PROTECT, related_name='payment')

    # The amount field represents the transaction amount for the payment.
    amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="مبلغ تراکنش")
    

    # کد رهگیری یکتای سیستم ما (به جای کد مرچنت بانک)
    # The transaction_id field is 
    # a UUIDField that generates a unique identifier for each payment transaction.
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # status field represents the current status of the payment,
    # using the PaymentStatus choices defined above. The default status is set to PENDING.
    status = models.CharField(max_length=1, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    

    # ثبت زمان‌های دقیق برای پیگیری‌های مالی
    # The created_at and updated_at fields are DateTimeFields 
    # that automatically record the timestamp of when the payment record is 
    # created and last updated, respectively.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # The __str__ method provides a human-readable representation of the Payment instance,
    # displaying the transaction ID and current status 
    # for easy identification in the admin interface or logs.
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.status}"



