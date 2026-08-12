from django.db import transaction
from .models import Customer, Address

class AddressService:
    @staticmethod
    @transaction.atomic
    def set_default_address(user, address_id):
        """
        تنظیم آدرس پیش‌فرض برای کاربر و غیرفعال کردن بقیه آدرس‌ها
        """
        customer = Customer.objects.get(user=user)
        # تمام آدرس‌های فعلی کاربر از حالت پیش‌فرض خارج می‌شوند
        Address.objects.filter(customer=customer, is_default=True).update(is_default=False)
        # آدرس انتخابی پیش‌فرض می‌شود
        address = Address.objects.get(id=address_id, customer=customer)
        address.is_default = True
        address.save()
        return address


