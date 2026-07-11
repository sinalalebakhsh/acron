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


# why transaction.atomic?
# The @transaction.atomic decorator is used to ensure that the operations
from django.db import transaction

# why ValidationError?
# The ValidationError exception is used to indicate that there was a validation
from rest_framework.exceptions import ValidationError

# why select_related?
# The select_related method is used to optimize database queries by performing
from apps.orders.models import Order

# The OrderService is used to handle business logic related to orders.
from apps.orders.services import OrderService

# The Payment model is used to represent payment records in the database.
from .models import Payment


# What is the PaymentService class?
# The PaymentService class is a service class that encapsulates the business logic
# and operations related to payments in the application. It provides methods
# for initiating payments and verifying mock payments, handling the necessary  
# validations, database operations, and interactions with external services (like payment gateways).
class PaymentService:
    # The initiate_payment method is responsible for initiating a payment request for a given order.
    # It performs security checks, calculates the total amount, creates or updates a payment record,
    # and generates a mock gateway URL for the payment process.
    # ---------------------------
    # The @transaction.atomic decorator is used to ensure 
    # that the operations within the initiate_payment method are executed within a single database transaction. This means that if any part of the method fails (e.g., due to a validation error), 
    # all changes made to the database will be rolled back, ensuring data integrity and consistency.
    # ---------------------------
    # The initiate_payment method takes two parameters: order_id and user.
    # - order_id: The ID of the order for which the payment is being initiated.
    # - user: The user who is initiating the payment.
    @staticmethod
    @transaction.atomic
    def initiate_payment(order_id, user):
        """
        This method initiates a payment request for a given order. 
        It performs security checks, calculates the total amount, 
        creates or updates a payment record, and generates a mock gateway URL for the payment process.
        درخواست پرداخت: فاکتور را چک می‌کند و لینک درگاه را می‌سازد.
        """

        # diagnostic: invoked by user: {user.username}, order_id: {order_id}
        # ۱. بررسی امنیتی و زمانی فاکتور (همان متدی که قبلا نوشتیم)
        order = OrderService.validate_order_for_payment(order_id)
        
        #  diagnostic: order validated
        # ۲. بررسی اینکه فاکتور متعلق به همین شخص باشد
        if order.customer.user != user:
            raise ValidationError("شما اجازه دسترسی به این فاکتور را ندارید.")

        #  diagnostic: user is authorized to access the order
        # ۳. محاسبه جمع کل فاکتور
        total_amount = sum(item.quantity * item.unit_price for item in order.items.all())

        #  diagnostic: total_amount calculated: {total_amount}
        # ۴. ساخت یا به‌روزرسانی رکورد پرداخت در دیتابیس
        payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={'amount': total_amount}
        )

        # if the payment record already exists, update the amount in case it has changed
        # اگر از قبل پرداختی موفق داشته، ارور بده
        if not created and payment.status == Payment.PaymentStatus.SUCCESS:
            raise ValidationError("این سفارش قبلاً با موفقیت پرداخت شده است.")

        #  diagnostic: payment record created or updated
        # ۵. ساخت لینک درگاه شبیه‌ساز (Mock Gateway)
        # در پروژه‌های دیگر که از هسته شما استفاده می‌کنند، در این خط به API زرین‌پال متصل می‌شوند
        mock_gateway_url = f"http://127.0.0.1:8000/api/payments/mock-bank/?transaction_id={payment.transaction_id}"
        
        return mock_gateway_url, payment.transaction_id

    # The verify_mock_payment method is responsible for simulating,
    # the callback from the bank (payment gateway) to confirm or reject a transaction. 
    # It takes two parameters: transaction_id and is_successful.
    # - transaction_id: The unique identifier of the payment transaction to be verified.
    # - is_successful: A boolean indicating whether the transaction was successful.
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





