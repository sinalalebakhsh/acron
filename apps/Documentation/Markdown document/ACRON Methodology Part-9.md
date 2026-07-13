# ACRON Methodology Part-9

<aside>
📢

در Part-8 ، فاز 7  Payment Domain تمام شد

</aside>

# فاز 8: Shipment & Fulfillment Domain

---

اکنون وقت تکمیل آخرین قطعه از پازل فیزیکی تجارت الکترونیک است: **دامنه ارسال و مرسولات (Shipment & Fulfillment Domain)**.

وقتی پرداخت در مرحله قبل با موفقیت انجام شد و وضعیت سفارش به `COMPLETED` تغییر کرد، وظیفه سیستم مالی به پایان می‌رسد؛ اما کار انبار و لجستیک تازه شروع شده است! ما نیاز به سیستمی داریم که به محض تایید پرداخت، به صورت خودکار یک «مرسوله» برای سفارش بسازد تا انباردار بتواند کالا را بسته‌بندی کرده، تحویل پست دهد و کد رهگیری پستی را در سیستم ثبت کند.

این همان دیتابیسی است که وقتی در مرحله بعدی سرور MCP (دستیار هوش مصنوعی) را ساختیم و کاربر در چت پرسید: *"سفارش من کجاست؟"*، هوش مصنوعی با خواندن این جدول به او جواب می‌دهد: *"سفارش شما تحویل اداره پست شده و کد مرسوله شما X است"*.

> 1-باید یک اپلیکیشن به نام `shipments` در پوشه `apps/` ایجاد کنیم و آن را به `INSTALLED_APPS` اضافه کنیم:
> 
> 
> ```python
> python manage.py startapp shipments apps/shipments
> ```
> 

**طراحی مدل `Shipment` (دیتابیس):**

- این جدول با یک رابطه یک‌به‌یک (OneToOne) به جدول `Order` متصل می‌شود و فیلدهایی مثل **وضعیت ارسال** (در حال آماده‌سازی، تحویل پیک/پست شده، تحویل مشتری شده)، **کد رهگیری پستی** (Tracking Number) و **تاریخ تخمینی تحویل** را در خود نگه می‌دارد.

 **اتصال اتوماتیک (Automated Trigger):**

- ما لایه `PaymentService` که در مرحله قبل نوشتیم را طوری ارتقا می‌دهیم که وقتی متد `verify_mock_payment` با موفقیت اجرا شد، فقط وضعیت فاکتور را تغییر ندهد؛ بلکه در همان لحظه، متد `create_shipment` از لایه سرویس مرسولات را فراخوانی کند تا یک مرسوله جدید به صورت خودکار برای انبار صادر شود.

> 2-  فایل `config/settings.py` را باز کرده و آن را در لیست `LOCAL_APPS` ثبت کنید:
> 
> 
> ```python
> LOCAL_APPS = [
>     # ... اپلیکیشن‌های قبلی
>     'apps.shipments',
> ]
> ```
> 

> 3-  طراحی مدل مرسوله (`apps/shipments/models.py`)
> 
> 
> در این بخش دیتابیس لجستیک و انبار را پیاده‌سازی می‌کنیم.
> 
> ```python
> from django.db import models
> from apps.orders.models import Order
> 
> class ShipmentStatus(models.TextChoices):
>     PREPARING = 'PRE', 'در حال آماده‌سازی و بسته‌بندی'
>     SHIPPED = 'SHI', 'تحویل شرکت حمل و نقل شده'
>     DELIVERED = 'DEL', 'تحویل مشتری شده'
>     CANCELED = 'CAN', 'لغو شده'
> 
> class CarrierChoices(models.TextChoices):
>     POST = 'POST', 'شرکت ملی پست'
>     TIPAX = 'TIPX', 'تیپاکس'
>     PEYK = 'PEYK', 'پیک اختصاصی'
> 
> class Shipment(models.Model):
>     order = models.OneToOneField(
>         Order, 
>         on_delete=models.PROTECT, 
>         related_name='shipment',
>         verbose_name="سفارش مربوطه"
>     )
>     status = models.CharField(
>         max_length=3, 
>         choices=ShipmentStatus.choices, 
>         default=ShipmentStatus.PREPARING,
>         verbose_name="وضعیت ارسال"
>     )
>     carrier = models.CharField(
>         max_length=4,
>         choices=CarrierChoices.choices,
>         default=CarrierChoices.POST,
>         verbose_name="شرکت حمل و نقل"
>     )
>     tracking_number = models.CharField(
>         max_length=100, 
>         blank=True, 
>         null=True, 
>         verbose_name="کد رهگیری مرسوله"
>     )
>     
>     created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد مرسوله")
>     shipped_at = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ خروج از انبار")
>     delivered_at = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ تحویل به مشتری")
> 
>     class Meta:
>         verbose_name = "مرسوله"
>         verbose_name_plural = "مرسولات"
>         ordering = ['-created_at']
> 
>     def __str__(self):
>         return f"Shipment for Order {self.order.id} - Status: {self.get_status_display()}"
> ```
> 

#### چرایی این طراحی معماری:

- **چرا `OneToOneField`؟** هر فاکتور یا سفارش (`Order`) دقیقاً و منحصراً **یک مرسوله فیزیکی** در انبار دارد. رابطه‌ی یک‌به‌یک بهترین تضمین برای جلوگیری از ساخت مرسولات تکراری برای یک فاکتور است.
- **چرا `on_delete=models.PROTECT`؟** خطرناک‌ترین اتفاق در دیتابیس‌های فروشگاهی، حذف تصادفی سوابق است. با استفاده از `PROTECT` به جنگو می‌گوییم: *"اگر کسی خواست یک سفارش را حذف کند ولی برای آن مرسوله صادر شده بود، اجازه حذف نده و خطا صادر کن"*. این کار امنیت تاریخچه داده‌ها را بالا می‌برد.

> 4-  لایه مغز متفکر مرسولات (`apps/shipments/services.py`)
> 
> 
> طبق اصول پروژه، منطق بیزینس را از ویو جدا کرده و درون یک کلاس سرویس پیاده می‌کنیم.
> 
> ```python
> from django.utils import timezone
> from .models import Shipment, ShipmentStatus
> 
> class ShipmentService:
>     
>     @staticmethod
>     def create_shipment(order) -> Shipment:
>         """
>         صدا زدن اتوماتیک انبار برای آماده‌سازی کالا پس از پرداخت موفق
>         """
>         # جلوگیری از ایجاد مرسوله تکراری در صورت دبل‌کلیک یا خطای زیرساختی
>         shipment, created = Shipment.objects.get_or_create(order=order)
>         return shipment
> 
>     @staticmethod
>     def update_tracking_info(shipment_id: int, carrier: str, tracking_number: str) -> Shipment:
>         """
>         متدی مخصوص پنل انباردار برای ثبت کد مرسوله پستی
>         """
>         shipment = Shipment.objects.get(id=shipment_id)
>         shipment.carrier = carrier
>         shipment.tracking_number = tracking_number
>         shipment.status = ShipmentStatus.SHIPPED
>         shipment.shipped_at = timezone.now()
>         shipment.save()
>         
>         # خلاقیت جدید: در این نقطه می‌توان وب‌هوک پیامک یا ایمیل اطلاع‌رسانی به کاربر را شلیک کرد.
>         return shipment
> ```
> 

#### خلاقیت جدید معماری (Intelligent Tracking Link):

به عنوان یک ارزش افزوده خلاقانه، متد زیر را به دکمه یا خروجی مدل `Shipment` اضافه می‌کنیم تا کاربر بدون نیاز به کپی-پیست کردن کد رهگیری، مستقیماً با کلیک روی یک لینک هوشمند به صفحه رهگیری سامانه پست یا تیپاکس هدایت شود:

> 5-  این متد را می‌توانید داخل خود کلاس مدل `Shipment` در فایل `models.py` قرار دهید.
> 
> 
> ```python
> def get_tracking_url(self):
>         """
>         تولید خودکار لینک رهگیری بر اساس شرکت حمل و نقل برای فرانت‌اند یا دستیار هوشمند
>         """
>         if not self.tracking_number:
>             return None
>         if self.carrier == 'POST':
>             return f"https://tracking.post.ir/?id={self.tracking_number}"
>         elif self.carrier == 'TIPX':
>             return f"https://tipaxco.com/tracking?id={self.tracking_number}"
>         return None
> ```
> 

### شلیک اتوماتیک مرسوله (اتصال لایه پرداخت به انبار)

حالا باید زنجیره انتقال داده را متصل کنیم.

> 6-   فایل **`apps/payments/services.py`** را باز کنید. متد `verify_mock_payment` را پیدا کنید و خط مربوط به فراخوانی سرویس مرسوله را به آن اضافه کنید:
> 
> 
> ```python
> from apps.shipments.services import ShipmentService  # <--- اضافه کردن این ایمپورت
> 
> class PaymentService:
>     # ... متدهای قبلی
>     
>     @staticmethod
>     def verify_mock_payment(transaction_id, is_successful):
>         # ... کدهای قبلی شما که وضعیت فاکتور را تغییر می‌داد
>         
>         if is_successful:
> 						# کد های قبلی را تغییر ندهید
> 
> 						            # فقط 3 خط زیر رار اضافه کنید
>             # === اتصال زنجیره معماری ===
>             # به محض موفقیت پرداخت، به صورت خودکار دستور خروج از انبار صادر می‌شود
>             ShipmentService.create_shipment(payment.order)
>             
>         else:
>             payment.status = 'F' # Failed
>             payment.save()
>             
>         return payment
> ```
> 

ساخت سریالایزر و ویو برای پیگیری کاربران (`serializers.py` & `views.py`)

کاربر باید بتواند وضعیت مرسوله خود را ببیند.

> 7-  فایل **`apps/shipments/serializers.py`** را بسازید:
> 

> 8-  داخل فایل **`apps/shipments/serializers.py`** این کد را بنویسید:
> 
> 
> ```python
> from rest_framework import serializers
> from .models import Shipment
> 
> class ShipmentTrackerSerializer(serializers.ModelSerializer):
>     status_display = serializers.CharField(source='get_status_display', read_only=True)
>     carrier_display = serializers.CharField(source='get_carrier_display', read_only=True)
>     tracking_url = serializers.CharField(source='get_tracking_url', read_only=True)
> 
>     class Meta:
>         model = Shipment
>         fields = [
>             'id', 'status', 'status_display', 'carrier', 
>             'carrier_display', 'tracking_number', 'tracking_url',
>             'created_at', 'shipped_at', 'delivered_at'
>         ]
>         
>         
>         
> ```
> 

> 9- فایل **`apps/shipments/views.py`** را بسازید:
> 
> 
> ```python
> from rest_framework.viewsets import ReadOnlyModelViewSet
> from rest_framework.permissions import IsAuthenticated
> from .models import Shipment
> from .serializers import ShipmentTrackerSerializer
> 
> class CustomerShipmentViewSet(ReadOnlyModelViewSet):
>     """
>     ویو فقط خواندنی (ReadOnly) برای اینکه کاربران وضعیت مرسوله خود را تعقیب کنند.
>     """
>     serializer_class = ShipmentTrackerSerializer
>     permission_classes = [IsAuthenticated]
> 
>     def get_queryset(self):
>         # هر کاربر فقط مرسوله‌ای را می‌بیند که فاکتور آن متعلق به خودش است
>         return Shipment.objects.filter(order__customer__user=self.request.user)
>         
>         
>     
>      
> ```
> 

**چرا `ReadOnlyModelViewSet`؟** مشتری نباید بتواند وضعیت مرسوله را تغییر دهد یا کد رهگیری را دستکاری کند! او فقط حق دیدن (GET) دارد.

تنظیم نهایی URLها

> 10-  فایل **`apps/shipments/urls.py`** را بسازید
> 

> 11-  داخل فایل **`apps/shipments/urls.py`** را بنویسید:
> 
> 
> ```python
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CustomerShipmentViewSet
> 
> router = DefaultRouter()
> router.register('track', CustomerShipmentViewSet, basename='shipment-track')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

> 12-  و در نهایت آن را در روتر مرکزی یعنی **`apps/api/urls.py`** ریجستر کنید:
> 
> 
> ```python
> urlpatterns = [
>     # ... مسیرهای قبلی
>     path('shipments/', include('apps.shipments.urls')),
> ]
> ```
> 

> 13-  داخل مسیر acron/apps/shipments/apps.py مورد زیر را تغییر دهید به حالت زیریش
> 
> 
> ```python
>     name = 'shipments' # حالت قدیمی
>     name = 'apps.shipments' # تغییر دهید به این حالت
> ```
> 

> 14-  دستور نهایی برای دیتابیس
> 
> 
> کدها کامل شده‌اند. حالا دستورات زیر را در ترمینال بزنید تا جداول لجستیک خلق شوند:
> 
> ```python
> python manage.py makemigrations
> python manage.py migrate
> ```
> 

خروجی شبیه به زیر خواهد بود:

```python
$ python manage.py makemigrations
Migrations for 'shipments':
  apps\shipments\migrations\0001_initial.py
    + Create model Shipment

$ python manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, auth, carts, contenttypes, customers, orders, payments, products, sessions, shipments
Running migrations:
  Applying shipments.0001_initial... OK

```

<aside>
📢

## هسته فیزیکی و تجاری پروژه ACRON به بلوغ ۱۰۰٪ رسید. اکنون اگر خریدی انجام شود، دیتابیس انبار به صورت خودکار به روز می‌شود.

</aside>

در دنیای واقعی، سیستم بدون پنل مدیریت (Backoffice) مثل یک ماشین مسابقه‌ای است که داشبورد ندارد. شما نمی‌توانید ببینید آیا موتور درست کار می‌کند یا نه. اضافه کردن این جریان به پنل ادمین جنگو (Django Admin) دو مزیت حیاتی برای ما دارد:

1. **تایید بصری چرخه:** ما می‌توانیم با چشم خودمان ببینیم که وقتی یک پرداخت موفق در Swagger ثبت شد، چطور وضعیت فاکتور در ثانیه تغییر می‌کند و مرسوله انبار صادر می‌شود.
2. **آماده‌سازی برای MCP:** وقتی دستیار هوش مصنوعی (MCP) را ساختیم، برای تست کردن آن نیاز داریم که به عنوان ادمین، وضعیت مرسوله را به «ارسال شده» تغییر دهیم یا کد پست دستی وارد کنیم تا ببینیم آیا هوش مصنوعی در چت این تغییرات را به کاربر درست گزارش می‌دهد یا خیر.

داشبورد مدیریت پروژه ACRON را در سه اپلیکیشن `orders` و `payments` و `shipments` در این مرحله می سازیم:

### مدیریت فاکتورها و اقلام سفارشی (`apps/orders/admin.py`)

یک خطای رایج این است که فاکتور و آیتم‌های داخل آن را جداگانه ثبت می‌کنند. خلاقیت معماری در اینجا، استفاده از **`TabularInline`** است تا ادمین بتواند در همان صفحه فاکتور، ببیند کاربر چه کالاهایی خریده است.

> 15-  فایل `apps/orders/admin.py` را باز کنید و کدهای زیر را قرار دهید:
> 
> 
> ```python
> from django.contrib import admin
> from .models import Order, OrderItem
> 
> class OrderItemInline(admin.TabularInline):
>     model = OrderItem
>     extra = 0
>     # فاکتور نهایی نباید توسط ادمین دستکاری شود تا جلوی فساد مالی گرفته شود
>     readonly_fields = ['product', 'quantity', 'unit_price']
>     can_delete = False
> 
> @admin.register(Order)
> class OrderAdmin(admin.ModelAdmin):
>     list_display = ['id', 'customer', 'status', 'created_at']
>     list_filter = ['status', 'created_at']
>     search_fields = ['id', 'customer__user__username']
>     inlines = [OrderItemInline]
>     
>     # سفارشات ثبت شده نباید خودسرانه حذف شوند
>     def has_delete_permission(self, request, obj=None):
>         return False
> ```
> 

مدیریت تراکنش‌های مالی (`apps/payments/admin.py`)

تراکنش‌های مالی بسیار حساس هستند. ادمین نباید بتواند مبلغ یا کد پیگیری بانک را ویرایش کند! او فقط باید بتواند آن‌ها را گزارش‌گیری کند.

> 16-  فایل `apps/payments/admin.py` را باز کنید:
> 
> 
> ```python
> from django.contrib import admin
> from .models import Payment
> 
> @admin.register(Payment)
> class PaymentAdmin(admin.ModelAdmin):
>     list_display = ['transaction_id', 'order', 'amount', 'status', 'created_at']
>     list_filter = ['status', 'created_at']
>     search_fields = ['transaction_id', 'order__id']
>     
>     # تمام فیلدهای مالی را برای ادمین Read-Only می‌کنیم تا امنیت حفظ شود
>     readonly_fields = ['transaction_id', 'order', 'amount', 'status', 'created_at', 'updated_at']
> 
>     def has_add_permission(self, request):
>         return False # ادمین نباید بتواند دستی تراکنش مالی خلق کند
> 
>     def has_delete_permission(self, request, obj=None):
>         return False # تراکنش مالی هرگز نباید حذف شود
> ```
> 

### پنل کنترل انبار و لجستیک (`apps/shipments/admin.py`)

اینجا دقیقاً همان‌جایی است که انباردار وارد می‌شود. او فاکتورهای آماده ارسال را می‌بیند، کالا را بسته‌بندی می‌کند، شرکت حمل و نقل (پست/تیپاکس) را انتخاب کرده و **کد رهگیری** را وارد می‌کند.

> 17-  فایل `apps/shipments/admin.py` را باز کنید:
> 
> 
> ```python
> from django.contrib import admin
> from .models import Shipment
> 
> @admin.register(Shipment)
> class ShipmentAdmin(admin.ModelAdmin):
>     list_display = ['id', 'order', 'status', 'carrier', 'tracking_number', 'created_at']
>     list_filter = ['status', 'carrier', 'created_at']
>     search_fields = ['order__id', 'tracking_number']
>     
>     # سفارش مربوطه نباید در انبار جابجا شود
>     readonly_fields = ['order', 'created_at', 'shipped_at', 'delivered_at']
>     
>     fieldsets = (
>         ("اطلاعات پایه سفارش", {
>             'fields': ('order', 'created_at')
>         }),
>         ("وضعیت لجستیک و انبارداری", {
>             'fields': ('status', 'carrier', 'tracking_number')
>         }),
>         ("زمان‌بندی‌های ارسال", {
>             'fields': ('shipped_at', 'delivered_at'),
>             'classes': ('collapse',) # این بخش را پنهان میکند تا صفحه شلوغ نشود
>         }),
>     )
> ```
> 

> تست سناریوی کامل (The Grand Test)
> 
> 
> حالا سرور را ران کنید (`python manage.py runserver`) و به آدرس `http://127.0.0.1:8000/admin/` بروید. یک سوپر یوزر بسازید و لاگین کنید. حالا این زنجیره شگفت‌انگیز را تست کنید:
> 
> 1. از طریق Swagger یک سفارش جدید بسازید (وضعیت فاکتور شما `P` یا همان Pending است).
> 2. در پنل ادمین بخش **Orders** را باز کنید. فاکتور خود را می‌بینید که منتظر پرداخت است. اگر بخش **Shipments** را نگاه کنید، می‌بینید که هنوز هیچ مرسوله‌ای برای آن صادر نشده است (چون پولی پرداخت نشده).
> 3. حالا به Swagger بروید و متد `POST /api/payments/payments/initiate/` را صدا بزنید تا برای فاکتورتان لینک درگاه و تراکنش ساخته شود.
> 4. سپس متد شبیه‌ساز بانک یعنی `POST /api/payments/payments/mock_verify/` را با `is_successful=True` اجرا کنید.
> 5. **لحظه جادویی:** حالا پنل ادمین جنگو را رفرش کنید!
>     - در بخش **Orders**، وضعیت فاکتور به صورت خودکار به `Completed` تغییر کرده است.
>     - در بخش **Payments**، وضعیت تراکنش موفق ثبت شده است.
>     - و شاهکار اینجاست: در بخش **Shipments**، به صورت کاملاً اتوماتیک یک رکورد مرسوله جدید برای انبار صادر شده که وضعیت آن **"در حال آماده‌سازی و بسته‌بندی"** است!
> 
> حالا شما به عنوان یک ادمین/انباردار می‌توانید وارد آن مرسوله شوید، وضعیتش را به "تحویل شرکت حمل و نقل شده" تغییر دهید و یک کد رهگیری فرضی (مثل `1234567890`) در آن بنویسید و ذخیره کنید.
> 
> با این کار، سیستم ما اکنون صاحب یک **دیتای کاملاً زنده، منطقی و واقعی** شد. هسته بیزینس فروشگاه شما آماده است.
> 

<aside>
📢

# پایان فاز 8: Shipment & Fulfillment Domain

</aside>

<aside>
📢

# پایان Part-9

</aside>