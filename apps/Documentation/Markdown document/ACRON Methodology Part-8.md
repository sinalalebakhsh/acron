# ACRON Methodology Part-8

<aside>
📢

در Part-7 ، فاز 6 تمام شد تعداد قدم ها 14 قدم

</aside>

# فاز 7: Payment Domain

---

<aside>
📢

ما لایه‌ی پرداخت را طوری طراحی می‌کنیم که هسته‌ی سیستم اصلاً نداند پول چگونه جابجا می‌شود! هسته فقط یک پیام می‌فرستد: *"من X تومان پول می‌خواهم"*. 

امروز یک **درگاه شبیه‌ساز (Mock Gateway)** جواب این پیام را می‌دهد، و فردا توسعه‌دهندگان دیگر می‌توانند بدون دست زدن به کدهای شما، ماژول‌های زرین‌پال، استرایپ (Stripe) یا پی‌پال را به آن متصل کنند.

</aside>

<aside>
📢

قدم اول: ایجاد موجودیت تراکنش (دیتابیس)

</aside>

> 1- ابتدا باید اپلیکیشن جدیدی برای پرداخت‌ها داشته باشیم. (مطمئن شوید که `apps.payments` را به `INSTALLED_APPS` در فایل تنظیمات اضافه کنید).
> 
> 
> ```python
> # Application definition
> 
> INSTALLED_APPS = [
> 		....
>     # CREATE by me
> 		....
>     'apps.payments',
> 		....
> ]
> 
> ```
> 

> 2- در مسیر `apps/payments/` فایل `models.py` را بسازید:
> 
> 
> ```python
> from django.db import models
> import uuid
> from apps.orders.models import Order
> 
> class Payment(models.Model):
>     class PaymentStatus(models.TextChoices):
>         PENDING = 'P', 'در انتظار پرداخت'
>         SUCCESS = 'S', 'موفق'
>         FAILED = 'F', 'ناموفق'
> 
>     # هر فاکتور فقط یک رکورد پرداخت فعال دارد
>     order = models.OneToOneField(Order, on_delete=models.PROTECT, related_name='payment')
>     amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="مبلغ تراکنش")
>     
>     # کد رهگیری یکتای سیستم ما (به جای کد مرچنت بانک)
>     transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
>     
>     status = models.CharField(max_length=1, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
>     
>     # ثبت زمان‌های دقیق برای پیگیری‌های مالی
>     created_at = models.DateTimeField(auto_now_add=True)
>     updated_at = models.DateTimeField(auto_now=True)
> 
>     def __str__(self):
>         return f"Payment {self.transaction_id} - {self.status}"
> ```
> 

> 3- *(پس از این کار، اجرای `makemigrations` و `migrate` فراموش نشود).*
> 
> 
> ```python
> $ python manage.py makemigrations payments
> Migrations for 'payments':
>   apps\payments\migrations\0001_initial.py
>     + Create model Payment
> 
> $ python manage.py migrate payments
> Operations to perform:
>   Apply all migrations: payments
> Running migrations:
>   Applying payments.0001_initial... OK
> 
> ```
> 

<aside>
📢

قدم دوم: لایه سرویس (هسته‌ی مرکزی و درگاه شبیه‌ساز)

</aside>

این فایل جذاب‌ترین بخش کار است. ما دو عملیات اصلی داریم: ساخت لینک پرداخت، و تایید پرداخت. اینجا دقیقاً همان منطقِ انقضای ۱۵ دقیقه‌ای که قبلاً نوشتیم را به کار می‌گیریم.

> 4- در مسیر `apps/payments/` فایل `services.py` را بسازید و کدهای زیر را داخل آن کپی کنید:
> 
> 
> ```python
> from django.db import transaction
> from rest_framework.exceptions import ValidationError
> from apps.orders.models import Order
> from apps.orders.services import OrderService
> from .models import Payment
> 
> class PaymentService:
>     
>     @staticmethod
>     @transaction.atomic
>     def initiate_payment(order_id, user):
>         """
>         درخواست پرداخت: فاکتور را چک می‌کند و لینک درگاه را می‌سازد.
>         """
>         # ۱. بررسی امنیتی و زمانی فاکتور (همان متدی که قبلا نوشتیم)
>         order = OrderService.validate_order_for_payment(order_id)
>         
>         # ۲. بررسی اینکه فاکتور متعلق به همین شخص باشد
>         if order.customer.user != user:
>             raise ValidationError("شما اجازه دسترسی به این فاکتور را ندارید.")
> 
>         # ۳. محاسبه جمع کل فاکتور
>         total_amount = sum(item.quantity * item.unit_price for item in order.items.all())
> 
>         # ۴. ساخت یا به‌روزرسانی رکورد پرداخت در دیتابیس
>         payment, created = Payment.objects.get_or_create(
>             order=order,
>             defaults={'amount': total_amount}
>         )
> 
>         # اگر از قبل پرداختی موفق داشته، ارور بده
>         if not created and payment.status == Payment.PaymentStatus.SUCCESS:
>             raise ValidationError("این سفارش قبلاً با موفقیت پرداخت شده است.")
> 
>         # ۵. ساخت لینک درگاه شبیه‌ساز (Mock Gateway)
>         # در پروژه‌های دیگر که از هسته شما استفاده می‌کنند، در این خط به API زرین‌پال متصل می‌شوند
>         mock_gateway_url = f"http://127.0.0.1:8000/api/payments/mock-bank/?transaction_id={payment.transaction_id}"
>         
>         return mock_gateway_url, payment.transaction_id
> 
>     @staticmethod
>     @transaction.atomic
>     def verify_mock_payment(transaction_id, is_successful):
>         """
>         شبیه‌سازی بازگشت از بانک (Callback): تایید یا رد تراکنش.
>         """
>         try:
>             payment = Payment.objects.select_related('order').get(transaction_id=transaction_id)
>         except Payment.DoesNotExist:
>             raise ValidationError("تراکنش در سیستم یافت نشد.")
> 
>         if payment.status != Payment.PaymentStatus.PENDING:
>             raise ValidationError("وضعیت این تراکنش قبلاً مشخص شده است.")
> 
>         # اگر درگاه شبیه‌ساز پیام موفقیت فرستاد:
>         if is_successful:
>             # تغییر وضعیت پرداخت به موفق
>             payment.status = Payment.PaymentStatus.SUCCESS
>             
>             # تغییر وضعیت فاکتور اصلی به "تکمیل شده"
>             payment.order.status = Order.OrderStatus.COMPLETED
>             payment.order.save()
>         else:
>             # تغییر وضعیت پرداخت به ناموفق
>             # دقت کنید: فاکتور را لغو نمی‌کنیم تا کاربر بتواند در فرصت ۱۵ دقیقه‌ای دوباره تلاش کند
>             payment.status = Payment.PaymentStatus.FAILED
>             
>         payment.save()
>         return payment
> ```
> 

<aside>
📢

قدم سوم: ساخت API دروازه‌ها (Views & Serializers)

</aside>

حالا باید این هسته را از طریق اینترنت در دسترس قرار دهیم.

> 5-  در مسیر `apps/payments/` فایل `serializers.py` را بسازید ، و فایل زیر را داخلش کپی کنید:
> 
> 
> ```python
> from rest_framework import serializers
> 
> class InitiatePaymentSerializer(serializers.Serializer):
>     # این خط اصلاح شد تا با دیتابیس سفارشات هماهنگ شود
>     order_id = serializers.UUIDField()
> 
> class MockBankCallbackSerializer(serializers.Serializer):
>     transaction_id = serializers.UUIDField()
>     is_successful = serializers.BooleanField(default=True, help_text="تیک بزنید تا پرداخت موفق شبیه‌سازی شود")
> ```
> 

### کالبدشکافی فایل `serializers.py` (دروازه‌بانان داده)

در پروژه ACRON، سریالایزرها فقط وظیفه تبدیل اطلاعات دیتابیس به JSON را ندارند؛ آن‌ها **قراردادهای API (API Contracts)** هستند که مشخص می‌کنند کلاینت دقیقاً چه چیزی باید بفرستد.

- **چرا `Serializer` و نه `ModelSerializer`؟ (خلاقیت معماری):**
یک خطای مرسوم بین جنگوکاران این است که برای هر کاری از ModelSerializer استفاده می‌کنند! ما اینجا قرار نیست مستقیماً رکوردی در جدول Payment بسازیم یا ویرایش کنیم. ما فقط می‌خواهیم کاربر **شماره فاکتور (`order_id`)** را بفرستد تا آن را به لایه سرویس بسپاریم. استفاده از Serializer  ساده یعنی  **جداسازی کامل لایه API از ساختار دیتابیس**. فردا اگر نام فیلد در دیتابیس تغییر کند، قرارداد ما با فرانت‌اند یا موبایل دست‌نخورده  باقی می‌ماند!
- **چرا `UUIDField`؟** تضمین می‌کند که کلاینت حتماً یک کد ۳۶ کاراکتری استاندارد UUID بفرستد. اگر کسی رشته‌ای مثل `"123"` بفرستد، سریالایزر قبل از اینکه درخواست حتی به لایه سرویس یا دیتابیس برسد، آن را با ارور ۴۰۰ بلاک می‌کند (حفاظت از منابع سرور).
- **خلاقیت در `help_text` و `default=True`:** وقتی از ابزاری مثل Swagger (داکیومنت‌ساز API) استفاده می‌کنیم، این فیلد `help_text` مستقیماً تبدیل به یک راهنما در پنل تسترها می‌شود! برنامه‌نویس فرانت‌اند بدون اینکه از شما سوال بپرسد، متوجه می‌شود که با تیک زدن این گزینه می‌تواند سناریوی پرداخت موفق یا ناموفق را شبیه‌سازی کند.

> 6- در مسیر `apps/payments/` فایل `views.py` را بسازید:
> 
> 
> ```python
> from rest_framework.viewsets import GenericViewSet
> from rest_framework.response import Response
> from rest_framework.decorators import action
> from rest_framework.permissions import IsAuthenticated, AllowAny
> from drf_spectacular.utils import extend_schema
> from .serializers import InitiatePaymentSerializer, MockBankCallbackSerializer
> from .services import PaymentService
> 
> class PaymentViewSet(GenericViewSet):
>     
>     @extend_schema(request=InitiatePaymentSerializer, summary="درخواست تولید لینک پرداخت", tags=['Payments'])
>     @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
>     def initiate(self, request):
>         serializer = InitiatePaymentSerializer(data=request.data)
>         serializer.is_valid(raise_exception=True)
>         
>         order_id = serializer.validated_data['order_id']
>         
>         # ارسال به هسته مرکزی پرداخت
>         url, trx_id = PaymentService.initiate_payment(order_id, request.user)
>         
>         return Response({
>             "message": "لینک پرداخت با موفقیت تولید شد.",
>             "gateway_url": url,
>             "transaction_id": trx_id
>         })
> 
>     @extend_schema(request=MockBankCallbackSerializer, summary="شبیه‌ساز درگاه بانک (تست)", tags=['Payments'])
>     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
>     def mock_verify(self, request):
>         """
>         این ویو نقش بانک را بازی می‌کند. 
>         در دنیای واقعی، بانک پس از پرداخت کاربر، اطلاعات را به یک URL مشابه این می‌فرستد.
>         """
>         serializer = MockBankCallbackSerializer(data=request.data)
>         serializer.is_valid(raise_exception=True)
>         
>         trx_id = serializer.validated_data['transaction_id']
>         is_successful = serializer.validated_data['is_successful']
>         
>         payment = PaymentService.verify_mock_payment(trx_id, is_successful)
>         
>         return Response({
>             "payment_status": payment.get_status_display(),
>             "order_status": payment.order.get_status_display()
>         })
> ```
> 

### کالبدشکافی فایل `views.py` (کنترلرها و هدایت‌کنندگان جریان)

این فایل نشان‌دهنده هنر **«لاغر نگه داشتن ویوها» (Thin Views & Fat Services)** است. ویو هیچ منطق تجاری یا مالی‌ای ندارد و فقط ترافیک HTTP را مدیریت می‌کند.

- **چرا؟** وارد کردن ابزارهای مورد نیاز. توجه کنید که ما لاگین بودن (`IsAuthenticated`) و آزاد بودن (`AllowAny`) را همزمان ایمپورت کردیم، چون در پرداخت اینترنتی به هر دو نیاز داریم!
- **خلاقیت بزرگ معماری (چرا `GenericViewSet`؟):**
چرا از `ModelViewSet` که کار را راحت می‌کند استفاده نکردیم؟ چون `ModelViewSet` به صورت خودکار مسیرهای ساخت (CREATE)، حذف (DELETE) و ویرایش (UPDATE) را باز می‌کند! **شما هرگز نباید به کاربر اجازه دهید با یک درخواست PUT یا DELETE ساده، تاریخچه تراکنش‌های مالی را تغییر دهد یا حذف کند!**
ارث‌بری از `GenericViewSet` یک بوم کاملاً خالی به ما می‌دهد که فقط با اکشن‌هایی که خودمان تعریف می‌کنیم (مثل `initiate` و `mock_verify`) کار می‌کند. این یعنی **حداکثر امنیت مالی**.
- **`@extend_schema`:** به موتور Swagger می‌گوید که این مسیر چه شکلی است تا داکیومنت شیک و خودکار بسازد.
- **`@action(detail=False, ...)`:** در DRF، وقتی `detail=False` است، یعنی این متد روی کل مجموعه کار می‌کند و به آی‌دی در URL نیاز ندارد (مسیر می‌شود: `/api/payments/initiate/`).
- **`permission_classes=[IsAuthenticated]`:** **قفل اول:** فقط کاربری که توکن معتبر (لاگین) دارد می‌تواند درخواست پرداخت بدهد.
- **چرا `raise_exception=True`؟** یک الگوی تمیز (Clean Code). به جای اینکه بنویسیم `if serializer.is_valid():` و بعد ارورها را دستی برگردانیم، این پارامتر به DRF می‌گوید: *"اگر داده‌ها معتبر نبودند، خودت در همین خط کار را متوقف کن و یک ارور ۴۰۰ با جزئیات به کلاینت بفرست"*.
- **چرا `validated_data`؟** ما هرگز از `request.data['order_id']` مستقیم استفاده نمی‌کنیم! داده‌ها حتماً باید از فیلتر امنیتی سریالایزر عبور کنند تا مطمئن شویم یک عدد واقعی هستند، نه کدهای مخرب یا SQL Injection.

```python
        url, trx_id = PaymentService.initiate_payment(order_id, request.user)
```

- **پاس دادن کار به مغز متفکر:** ویو اصلاً نمی‌داند پرداخت چطور کار می‌کند! فقط آی‌دی فاکتور و کاربر فعلی (`request.user`) را به لایه سرویس می‌دهد و یک لینک درگاه (`url`) و کد پیگیری (`trx_id`) تحویل می‌گیرد.

```python
return Response({
            "message": "لینک پرداخت با موفقیت تولید شد.",
            "gateway_url": url,
            "transaction_id": trx_id
        })
```

- **چرا خروجی به این شکل است؟** برنامه‌نویس فرانت‌اند با دریافت این خروجی، کاربر را به `gateway_url` ریدایرکت (Redirect) می‌کند و `transaction_id` را هم در حافظه مرورگر نگه می‌دارد تا وضعیتش را پیگیری کند.

```python
@extend_schema(request=MockBankCallbackSerializer, summary="شبیه‌ساز درگاه بانک (تست)", tags=['Payments'])
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def mock_verify(self, request):
```

- **چرا `permission_classes=[AllowAny]`؟ (یک نکته حیاتی و بسیار مهم در سیستم‌های واقعی):**
این اکشن نقش بازگشت از بانک (**Callback یا Webhook**) را بازی می‌کند. در دنیای واقعی، وقتی کاربر در سایت زرین‌پال یا بانک ملت پول را پرداخت می‌کند، **سرورِ بانک** به این آدرس یک درخواست می‌فرستد تا بگوید پرداخت انجام شد.
سرور بانک که در سایت شما لاگین نیست! بانک توکن JWT کاربر شما را ندارد! اگر اینجا از `IsAuthenticated` استفاده کنید، سرور بانک با خطای "401 Unauthorized" مواجه می‌شود، پرداخت تایید نمی‌شود و پول به حساب مشتری برمی‌گردد! به همین دلیل، مسیرهای Callback بانک همیشه باید Public (`AllowAny`) باشند و امنیت آن‌ها از طریق چک کردن امضای دیجیتال یا همان `transaction_id` یکتا در دیتابیس تامین می‌شود.

```python
serializer = MockBankCallbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trx_id = serializer.validated_data['transaction_id']
        is_successful = serializer.validated_data['is_successful']
        
        payment = PaymentService.verify_mock_payment(trx_id, is_successful)
```

- **چرا؟** دریافت کد پیگیری و وضعیت پرداخت از شبیه‌ساز بانک، اعتبارسنجی آن، و ارسال به لایه سرویس برای تغییر وضعیت فاکتور.

```python
return Response({
            "payment_status": payment.get_status_display(),
            "order_status": payment.order.get_status_display()
        })
```

- **خلاقیت در استفاده از `get_status_display()`:** در دیتابیس، وضعیت‌ها به صورت حروف تک‌کاراکتری مثل `'S'` (برای Success) یا `'C'` (برای Completed) ذخیره می‌شوند تا سرعت دیتابیس بالا باشد. اما اگر `'S'` را به فرانت‌اند بفرستیم، خوانا نیست. متد جادویی `get_status_display()` در جنگو، معادل انسانی و فارسی آن (مثلاً "موفق" یا "تکمیل شده") که در تاپل `TextChoices` مدل تعریف کرده بودیم را برمی‌گرداند. این یعنی احترام به توسعه‌دهندگانی که از API ما استفاده می‌کنند.

> 7-  **تنظیم URLها:** فایل `apps/payments/urls.py` را ایجاد کنید و سپس آن را در `api/urls.py` مرکزی ثبت کنید:
> 
> 
> ```python
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import PaymentViewSet
> 
> router = DefaultRouter()
> router.register('payments', PaymentViewSet, basename='payments')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

کالبدشکافی فایل `urls.py` (مسیریابی سیستم)

- **چرا `basename='payments'` اجباری است؟ (نکته فنی):**
وقتی شما از `ModelViewSet` استفاده می‌کنید، DRF به متد `queryset = Payment.objects.all()` در بالای کلاس نگاه می‌کند و اسم مسیرها را به صورت خودکار حدس می‌زند. اما چون ما از `GenericViewSet` استفاده کردیم و هیچ `queryset` ثابت و پیش‌فرضی در ویو نگذاشتیم (چون نمی‌خواستیم کسی لیست پرداخت‌ها را ببیند)، DRF گیج می‌شود! با دادن پارامتر `basename='payments'` به او می‌گوییم: *"نام داخلی این مسیرها را `payments-initiate` و `payments-mock-verify` بگذار"*.

```python
urlpatterns = [
    path('', include(router.urls)),
]
```

- **چرا؟** اتصال مسیرهای تولید شده توسط روتر DRF به سیستم اصلی URLهای اپلیکیشن. وقتی این فایل در روتر مرکزی (`api/urls.py`) ثبت می‌شود، کل سیستم پرداخت با دو آدرس تمیز و ایزوله در دسترس سیستم‌عامل گونه‌ی شما قرار می‌گیرد!

<aside>
📢

### این معماری به شما اجازه می‌دهد فردا بدون اینکه حتی یک خط از کدهای `views.py` یا `serializers.py` را تغییر دهید، فقط در فایل `services.py` به جای درگاه شبیه‌ساز، کد زرین‌پال یا استرایپ را قرار دهید. سیستم از بیرون دقیقاً به همین شکلی که الان هست کار خواهد کرد!

</aside>

---

<aside>
📢

تست بصری در مرورگر

</aside>

> 1- تست بصری سیستم مالی در Swagger (از صفر تا صد خرید)
> 
> 
> اکنون پازل کامل شده است. سرور را ران کنید و این جریان را در Swagger انجام دهید:
> 
> 1. **لاگین:** توکن خود را در هدر قرار دهید.
> 2. **ساخت فاکتور:** طبق روال قبل، یک سبد خرید را با `POST /api/orders/` به فاکتور تبدیل کنید و `id` آن فاکتور را کپی کنید.
> 3. **درخواست پرداخت:** به مسیر `POST /api/payments/initiate/` بروید. `order_id` فاکتور را وارد کنید.
>     - **خروجی:** سیستم به شما یک `transaction_id` طولانی (UUID) و یک `gateway_url` می‌دهد.
> 4. **شبیه‌سازی بانک:** به مسیر `POST /api/payments/mock_verify/` بروید (این بخش نیاز به لاگین ندارد، چون بانک به سیستم ما لاگین نیست!).
>     - `transaction_id` که گرفتید را در بدنه قرار دهید.
>     - مقدار `is_successful` را `true` بگذارید و `Execute` کنید.
> 5. **بررسی نهایی:** اگر به پنل ادمین یا مسیر `GET /api/orders/` بروید، می‌بینید که وضعیت فاکتور از "در انتظار پرداخت" به شکل خودکار به "تکمیل شده" (Completed) تغییر کرده است و فرآیند خرید با یک شبیه‌ساز کاملاً ایزوله به پایان رسیده است.

اکنون وقت تکمیل آخرین قطعه از پازل فیزیکی تجارت الکترونیک است: **دامنه ارسال و مرسولات (Shipment & Fulfillment Domain)**.

وقتی پرداخت در مرحله قبل با موفقیت انجام شد و وضعیت سفارش به `COMPLETED` تغییر کرد، وظیفه سیستم مالی به پایان می‌رسد؛ اما کار انبار و لجستیک تازه شروع شده است! ما نیاز به سیستمی داریم که به محض تایید پرداخت، به صورت خودکار یک «مرسوله» برای سفارش بسازد تا انباردار بتواند کالا را بسته‌بندی کرده، تحویل پست دهد و کد رهگیری پستی را در سیستم ثبت کند.

این همان دیتابیسی است که وقتی در مرحله بعدی سرور MCP (دستیار هوش مصنوعی) را ساختیم و کاربر در چت پرسید: *"سفارش من کجاست؟"*، هوش مصنوعی با خواندن این جدول به او جواب می‌دهد: *"سفارش شما تحویل اداره پست شده و کد مرسوله شما X است"*.

<aside>
📢

# پایان فاز 7

</aside>

<aside>
📢

# پایان Part-8

</aside>