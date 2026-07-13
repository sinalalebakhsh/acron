from django.db import models
from apps.orders.models import Order

class ShipmentStatus(models.TextChoices):
    PREPARING = 'PRE', 'در حال آماده‌سازی و بسته‌بندی'
    SHIPPED = 'SHI', 'تحویل شرکت حمل و نقل شده'
    DELIVERED = 'DEL', 'تحویل مشتری شده'
    CANCELED = 'CAN', 'لغو شده'

class CarrierChoices(models.TextChoices):
    POST = 'POST', 'شرکت ملی پست'
    TIPAX = 'TIPX', 'تیپاکس'
    PEYK = 'PEYK', 'پیک اختصاصی'

class Shipment(models.Model):
    order = models.OneToOneField(
        Order, 
        on_delete=models.PROTECT, 
        related_name='shipment',
        verbose_name="سفارش مربوطه"
    )
    status = models.CharField(
        max_length=3, 
        choices=ShipmentStatus.choices, 
        default=ShipmentStatus.PREPARING,
        verbose_name="وضعیت ارسال"
    )
    carrier = models.CharField(
        max_length=4,
        choices=CarrierChoices.choices,
        default=CarrierChoices.POST,
        verbose_name="شرکت حمل و نقل"
    )
    tracking_number = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="کد رهگیری مرسوله"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد مرسوله")
    shipped_at = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ خروج از انبار")
    delivered_at = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ تحویل به مشتری")

    class Meta:
        verbose_name = "مرسوله"
        verbose_name_plural = "مرسولات"
        ordering = ['-created_at']

    def get_tracking_url(self):
        """
        تولید خودکار لینک رهگیری بر اساس شرکت حمل و نقل برای فرانت‌اند یا دستیار هوشمند
        """
        if not self.tracking_number:
            return None
        if self.carrier == 'POST':
            return f"https://tracking.post.ir/?id={self.tracking_number}"
        elif self.carrier == 'TIPX':
            return f"https://tipaxco.com/tracking?id={self.tracking_number}"
        return None

    def __str__(self):
        return f"Shipment for Order {self.order.id} - Status: {self.get_status_display()}"



