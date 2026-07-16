from django.utils import timezone

from .models import Shipment, ShipmentStatus


class ShipmentService:
    
    @staticmethod
    def create_shipment(order) -> Shipment:
        """
        صدا زدن اتوماتیک انبار برای آماده‌سازی کالا پس از پرداخت موفق
        """
        # جلوگیری از ایجاد مرسوله تکراری در صورت دبل‌کلیک یا خطای زیرساختی
        shipment, created = Shipment.objects.get_or_create(order=order)
        return shipment

    @staticmethod
    def update_tracking_info(shipment_id: int, carrier: str, tracking_number: str) -> Shipment:
        """
        متدی مخصوص پنل انباردار برای ثبت کد مرسوله پستی
        """
        shipment = Shipment.objects.get(id=shipment_id)
        shipment.carrier = carrier
        shipment.tracking_number = tracking_number
        shipment.status = ShipmentStatus.SHIPPED
        shipment.shipped_at = timezone.now()
        shipment.save()
        
        # خلاقیت جدید: در این نقطه می‌توان وب‌هوک پیامک یا ایمیل اطلاع‌رسانی به کاربر را شلیک کرد.
        return shipment




