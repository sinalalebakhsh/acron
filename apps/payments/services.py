# why this file?
# The services.py file is used to define service classes,
# that encapsulate business logic and operations related
# to payments in the application. It provides a layer of abstraction
# between the views and the models, allowing for better organization
# and separation of concerns in the codebase. By using service classes,
# we can keep the views clean and focused on handling HTTP requests,
# while the service classes handle the actual business logic and interactions
# with the models and external services. This makes the code more maintainable,
# testable, and easier to understand.


from django.db import transaction

from rest_framework.exceptions import ValidationError

from apps.orders.models import Order

from apps.orders.services import OrderService

from .models import Payment

class PaymentService:
    
    @staticmethod
    @transaction.atomic
    def initiate_payment(order_id, user):
        """
        درخواست پرداخت: فاکتور را چک می‌کند و لینک درگاه را می‌سازد.
        """
        # ۱. بررسی امنیتی و زمانی فاکتور (همان متدی که قبلا نوشتیم)
        order = OrderService.validate_order_for_payment(order_id)
        
        # ۲. بررسی اینکه فاکتور متعلق به همین شخص باشد
        if order.customer.user != user:
            raise ValidationError("شما اجازه دسترسی به این فاکتور را ندارید.")

        # ۳. محاسبه جمع کل فاکتور
        total_amount = sum(item.quantity * item.unit_price for item in order.items.all())

        # ۴. ساخت یا به‌روزرسانی رکورد پرداخت در دیتابیس
        payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={'amount': total_amount}
        )

        # اگر از قبل پرداختی موفق داشته، ارور بده
        if not created and payment.status == Payment.PaymentStatus.SUCCESS:
            raise ValidationError("این سفارش قبلاً با موفقیت پرداخت شده است.")

        # ۵. ساخت لینک درگاه شبیه‌ساز (Mock Gateway)
        # در پروژه‌های دیگر که از هسته شما استفاده می‌کنند، در این خط به API زرین‌پال متصل می‌شوند
        mock_gateway_url = f"http://127.0.0.1:8000/api/payments/mock-bank/?transaction_id={payment.transaction_id}"
        
        return mock_gateway_url, payment.transaction_id

    @staticmethod
    @transaction.atomic
    def verify_mock_payment(transaction_id, is_successful):
        """
        شبیه‌سازی بازگشت از بانک (Callback): تایید یا رد تراکنش.
        """
        try:
            payment = Payment.objects.select_related('order').get(transaction_id=transaction_id)
        except Payment.DoesNotExist:
            raise ValidationError("تراکنش در سیستم یافت نشد.")

        if payment.status != Payment.PaymentStatus.PENDING:
            raise ValidationError("وضعیت این تراکنش قبلاً مشخص شده است.")

        # اگر درگاه شبیه‌ساز پیام موفقیت فرستاد:
        if is_successful:
            # تغییر وضعیت پرداخت به موفق
            payment.status = Payment.PaymentStatus.SUCCESS
            
            # تغییر وضعیت فاکتور اصلی به "تکمیل شده"
            payment.order.status = Order.OrderStatus.COMPLETED
            payment.order.save()
        else:
            # تغییر وضعیت پرداخت به ناموفق
            # دقت کنید: فاکتور را لغو نمی‌کنیم تا کاربر بتواند در فرصت ۱۵ دقیقه‌ای دوباره تلاش کند
            payment.status = Payment.PaymentStatus.FAILED
            
        payment.save()
        return payment



