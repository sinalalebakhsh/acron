# ACRON Methodology Part-5

# فاز 4: Products Domain

<aside>
📢

در Part-4 ، فاز 4 تا قدم 56 پیش رفت

</aside>

<aside>
📢

مستندسازی نیمه خودکار با استفاده از Swagger

</aside>

در دنیای Django REST Framework، ما دو انتخاب معروف برای Swagger داریم: `drf-yasg` (قدیمی و مبتنی بر OpenAPI 2.0) و `drf-spectacular` (مدرن، قدرتمند و مبتنی بر OpenAPI 3.0).

ما قطعاً مسیر حرفه‌ای‌تر یعنی **`drf-spectacular`** را انتخاب می‌کنیم.

<aside>
📢

قدم اول: نصب و تنظیمات پایه

</aside>

> **57- نصب پکیج `drf-spectacular` در محیط مجازی:**
در ترمینال خود دستور زیر را وارد کنید:
> 
> 
> ```bash
> pipenv install drf-spectacular
> ```
> 

> **58- اضافه کردن به requirements.txt**
در ترمینال خود دستور زیر را وارد کنید:
> 
> 
> ```bash
> pipenv requirements > requirements.txt
> ```
> 

> **59- معرفی به جنگو و DRF:**
فایل `config/settings/base.py` را باز کنید. ما باید سه تغییر در این فایل ایجاد کنیم:
> 
> 
> ابتدا پکیج را به اپلیکیشن‌های نصب‌شده اضافه کنید:
> 
> ```python
> INSTALLED_APPS = [
>     # ...
>     'drf_spectacular', # مستندسازی API
>     
>     'apps.accounts',
>     'apps.customers',
>     'apps.products',
> ]
> ```
> 

> **60- سپس به DRF بگویید که برای تولید شِمای (Schema) مستندات، از کلاسِ این پکیج استفاده کند:**
> 
> 
> ```python
> REST_FRAMEWORK = {
>     # تنظیمات قبلی شما (مثل Authentication و Pagination) اینجا می‌مانند...
>     
>     # اضافه کردن کلاس تولیدکننده مستندات
>     'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
> }
> ```
> 

> **61-** در نهایت، تنظیمات ظاهری و هویتی Swagger را به انتهای فایل `base.py` اضافه کنید:
> 
> 
> ```python
> # تنظیمات اختصاصی Swagger
> SPECTACULAR_SETTINGS = {
>     'TITLE': 'ACRON Project API',
>     'DESCRIPTION': 'مستندات جامع APIهای فروشگاه آکرون شامل بخش مشتریان و محصولات',
>     'VERSION': '1.0.0',
>     'SERVE_INCLUDE_SCHEMA': False, # برای تمیز ماندن خروجی نهایی
>     
>     # تنظیمات امنیتی برای تست APIها داخل خود مرورگر
>     'SECURITY': [
>         {'jwtAuth': []}
>     ],
>     'SECURITY_DEFINITIONS': {
>         'jwtAuth': {
>             'type': 'http',
>             'scheme': 'bearer',
>             'bearerFormat': 'JWT',
>         }
>     }
> }
> ```
> 

### کالبدشکافی تنظیمات (بدون Vibe Coding)

- **چرا `DEFAULT_SCHEMA_CLASS` را تغییر دادیم؟** DRF به صورت پیش‌فرض یک سیستم تولید شمای ساده دارد که خیلی امکانات جالبی ندارد. با این خط، ما "مغز" تحلیلگر DRF را با "مغز" قدرتمند `drf-spectacular` جایگزین می‌کنیم تا بتواند روابط پیچیده (مثل گالری تصاویر و JWT) را بفهمد.
- **بخش `SECURITY_DEFINITIONS` چیست؟** یکی از جذاب‌ترین امکانات Swagger این است که دکمه‌ای به نام `Try it out` دارد. اما APIهای پروفایل مشتری ما (مثل `GET /api/customers/me/`) قفل هستند و توکن می‌خواهند. این تنظیمات به Swagger UI می‌فهماند که پروژه ما از `Bearer Token` استفاده می‌کند. با این کار، یک دکمه 🔒 (Authorize) بالای صفحه Swagger ظاهر می‌شود که می‌توانید توکن خود را آنجا قرار دهید و مستقیماً از داخل مرورگر APIها را تست کنید.

<aside>
📢

قدم دوم: مسیردهی (Routing) URLها

</aside>

حالا باید URLهایی بسازیم که فرانت‌اند بتواند از طریق آن‌ها فایل مستندات و رابط کاربری Swagger را ببیند.

> **62- فایل اصلی `config/urls.py` را باز کنید و کدهای زیر را اضافه کنید:**
> 
> 
> ```python
> from django.contrib import admin
> from django.urls import path, include
> from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
> 
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     path('api/', include('apps.api.urls')),
>     
>     # ------------------- Swagger URLs ------------------- #
>     # ۱. تولید فایل خام OpenAPI (به فرمت YAML/JSON)
>     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
>     
>     # ۲. رابط کاربری گرافیکی Swagger (توسعه‌دهندگان بک‌اند و فرانت‌اند)
>     path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
>     
>     # ۳. رابط کاربری Redoc (جایگزین Swagger، مناسب برای ارائه به مدیران)
>     path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
> ]
> ```
> 

<aside>
📢

کالبدشکافی URLهای مستندات

</aside>

- **`SpectacularAPIView` (`/api/schema/`):** این مسیر هیچ گرافیکی ندارد. وقتی این URL را صدا می‌زنید، پکیج تمام Viewها، Serializerها و Modelهای شما را می‌خواند و یک فایل متنی ماشین‌خوان (معمولاً YAML) تولید می‌کند. این فایل "نقشه راه" API شماست.
- **`SpectacularSwaggerView` (`/api/docs/`):** این همان رابط کاربری جذابی است که توسعه‌دهندگان دوستش دارند. این صفحه در واقع فایل خام مرحله قبل را می‌خواند (`url_name='schema'`) و آن را به دکمه‌ها و فرم‌های تعاملی تبدیل می‌کند.
- **`SpectacularRedocView` (`/api/redoc/`):** ابزار Redoc گرافیک متفاوت و کلاسیک‌تری نسبت به Swagger دارد (بدون قابلیت تست تعاملی). بسیاری از شرکت‌های بزرگ مستندات عمومی خود را با Redoc منتشر می‌کنند، چون خواندن آن مانند یک کتاب مرتب است.

<aside>
📢

### اجرای نهایی و تست

</aside>

حالا سرور پروژه را روشن کنید:

```python
python manage.py runserver
```

مرورگر خود را باز کنید و به آدرس زیر بروید:
`http://127.0.0.1:8000/api/docs/`

شما باید یک صفحه زیبا با عنوان "ACRON Project API" ببینید که تمام Endpointهای مربوط به JWT (دریافت و رفرش توکن)، Customers (مشاهده و ویرایش پروفایل) و Products (لیست محصولات) در آن به دقت دسته‌بندی شده‌اند.

> 62- لطفاً این صفحه را بررسی کنید و ببینید آیا فیلدهای محصولات و تصاویر فرعی به درستی در مستندات نمایش داده شده‌اند؟
> 

رسیدیم به بخش جذاب مستندسازی حرفه‌ای! دکوراتور `@extend_schema` دقیقاً همان ابزاری است که تفاوت یک API ساده را با یک API تجاری و استاندارد (مثل APIهای شرکت‌های بزرگ) مشخص می‌کند.

گاهی اوقات `drf-spectacular` با تمام هوشمندی‌اش نمی‌تواند هدف دقیق یک API را حدس بزند. مثلاً نمی‌داند که این API قرار است چه ارورهای خاصی برگرداند یا توضیح انسانیِ آن برای تیم فرانت‌اند چیست. اینجاست که `@extend_schema` وارد عمل می‌شود و کنترل کامل Swagger را به دست شما می‌سپارد.

### معرفی و پیاده‌سازی `@extend_schema`

بیایید این جادو را روی همان `ProductListView` که در مرحله قبل ساختیم پیاده کنیم تا خروجی Swagger آن را از یک حالت رباتی به یک حالت کاملاً خوانا و حرفه‌ای تبدیل کنیم.

> 63-  فایل `apps/products/views.py` را باز کنید و آن را به شکل زیر تغییر دهید:
> 
> 
> ```python
> from drf_spectacular.utils import extend_schema, extend_schema_view # این خط اضافه شد
> 
> # استفاده از دکوراتور برای شخصی‌سازی مستندات این View
> @extend_schema_view(
>     get=extend_schema(
>         summary="دریافت لیست محصولات فروشگاه",
>         description="این متد لیست تمامی محصولات را به همراه اطلاعات برند، دسته‌بندی و گالری تصاویر برمی‌گرداند. این مسیر کاملاً بهینه‌سازی شده (بدون مشکل N+1) است و نیازی به توکن احراز هویت ندارد.",
>         tags=['Products Catalog'], # دسته‌بندی API در سایدبار Swagger
>     )
> )
> 
> ```
> 

<aside>
📢

کالبدشکافی کد (بدون Vibe Coding)

</aside>

- **`@extend_schema_view`:** چون ما از کلاس‌های Generic (مثل `ListAPIView`) استفاده می‌کنیم، متد `get` به صورت مخفی در پس‌زمینه وجود دارد. این دکوراتور به ما اجازه می‌دهد به متدهای مخفیِ کلاس دسترسی پیدا کنیم و به جنگو بگوییم: "تنظیماتی که می‌گویم را فقط روی متد `get` این کلاس اعمال کن."
- **`summary`:** یک عنوان کوتاه و جذاب که در لیست کشویی Swagger با فونت درشت روبروی مسیر API نوشته می‌شود.
- **`description`:** توضیحات تکمیلی که وقتی فرانت‌اند کار روی API کلیک می‌کند، آن را می‌خواند تا دقیقاً بفهمد این مسیر چه دیتایی به او می‌دهد.
- **`tags`:** در Swagger، تمام APIها به صورت پیش‌فرض در یک گروه قرار می‌گیرند که شلوغ می‌شود. با تگ‌گذاری، یک پوشه (گروه) جدید به نام `Products Catalog` در صفحه ساخته می‌شود و این API با نظم خاصی زیرمجموعه آن قرار می‌گیرد.

<aside>
📢

آیا به آموزش بیشتر Swagger در این مرحله نیاز داریم؟

</aside>

**پاسخ کوتاه: فعلاً خیر.** شما اکنون ابزار اصلی (`drf-spectacular`) و ابزار شخصی‌سازی (`@extend_schema`) را در اختیار دارید. این ترکیب برای ۹۵٪ نیازهای مستندسازی یک پروژه در این سطح کافی است. 

درگیر شدن بیشتر با جزئیات Swagger (مثل تعریف دستی پارامترهای Query یا Override کردن کامپوننت‌های امنیتی) در این لحظه، باعث می‌شود از هدف اصلی باز بمانید. مستندسازی باید همگام با توسعه پیش برود، نه اینکه مانع آن شود.

<aside>
📢

بازگشت به مسیر توسعه: تکمیل فاز ۴ (Product Domain)

</aside>

در فاز ۴، ما لیست محصولات (`ProductListView`) را ساختیم. اما در هر فروشگاهی، وقتی روی یک محصول کلیک می‌کنید، وارد **صفحه جزئیات آن محصول (Product Detail)** می‌شوید.

در اینجا به جای استفاده از `id` محصول (مثل `/api/products/1/`)، باید از `slug` استفاده کنیم (مثل `/api/products/samsung-galaxy-s24/`) تا URLها برای سئو (SEO) بهینه باشند.

> 64- فایل `apps/products/views.py` را باز کنید و ویوی جزئیات را به انتهای آن اضافه کنید:
> 
> 
> ```python
> from rest_framework.generics import RetrieveAPIView
> 
> @extend_schema_view(
>     get=extend_schema(
>         summary="دریافت جزئیات یک محصول خاص",
>         description="این مسیر اطلاعات کامل یک محصول را بر اساس Slug آن برمی‌گرداند.",
>         tags=['Products Catalog'],
>     )
> )
> class ProductDetailView(RetrieveAPIView):
>     permission_classes = [AllowAny]
>     serializer_class = ProductSerializer
>     
>     # استفاده از همان تکنیک بهینه‌سازی دیتابیس
>     queryset = Product.objects.select_related(
>         'category', 
>         'brand'
>     ).prefetch_related(
>         'media_gallery'
>     ).all()
>     
>     # جادوی جنگو: جستجو بر اساس فیلد slug به جای id پیش‌فرض
>     lookup_field = 'slug'
> ```
> 

> 65-  فایل `apps/products/urls.py` را باز کنید و مسیر جدید را اضافه کنید:
> 
> 
> ```python
> from django.urls import path
> from .views import ProductListView, ProductDetailView
> 
> urlpatterns = [
>     path('', ProductListView.as_view(), name='product-list'),
>     
>     # مسیر دریافت یک محصول بر اساس اسلاگ
>     path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
> ]
> ```
> 

### کالبدشکافی معماری این بخش

- **`RetrieveAPIView`:** این کلاس آماده DRF، مخصوص برگرداندن **فقط یک رکورد** از دیتابیس است.
- **`lookup_field = 'slug'`:** به صورت پیش‌فرض، DRF در URLها دنبال `pk` (Primary Key یا همان ID) می‌گردد. با نوشتن این یک خط کد، به DRF دستور می‌دهیم که: "از این به بعد، محصول را از طریق فیلد `slug` در دیتابیس پیدا کن، نه `id`."
- **`<slug:slug>/` در URL:** بخش اول (`slug:`) به جنگو می‌گوید که این پارامتر می‌تواند شامل حروف، اعداد، خط تیره و آندرلاین باشد. بخش دوم (`slug`) نام متغیری است که به `lookup_field` در View پاس داده می‌شود.

اکنون فاز ۴ (Product Domain) به یک پایداری بسیار عالی رسیده است. هم مدل‌های بهینه داریم، هم ادمین قدرتمند، هم APIهای بدون مشکل N+1 و هم مستندات تمیز.

<aside>
📢

 یکی از مهم‌ترین اصول مهندسی نرم‌افزار یعنی **DRY (Don't Repeat Yourself)** یا "خودت را تکرار نکن" 

</aside>

<aside>
📢

ریفکتور فاز ۴: استفاده از ViewSet برای جلوگیری از تکرار

</aside>

> 66-  فایل `apps/products/views.py` را باز کنید و کل کدهای قبلی (مربوط به محصولات) را با این کد جایگزین کنید:
> 
> 
> ```python
> from rest_framework.viewsets import ReadOnlyModelViewSet
> from rest_framework.permissions import AllowAny
> from drf_spectacular.utils import extend_schema, extend_schema_view
> from .models import Product
> from .serializers import ProductSerializer
> 
> # تعریف Swagger فقط یک‌بار در بالای ViewSet
> @extend_schema_view(
>     list=extend_schema(
>         summary="دریافت لیست محصولات",
>         description="لیست تمامی محصولات به همراه برند، دسته‌بندی و گالری تصاویر.",
>         tags=['Products Catalog'],
>     ),
>     retrieve=extend_schema(
>         summary="دریافت جزئیات محصول",
>         description="اطلاعات کامل یک محصول بر اساس Slug.",
>         tags=['Products Catalog'],
>     )
> )
> class ProductViewSet(ReadOnlyModelViewSet):
>     permission_classes = [AllowAny]
>     serializer_class = ProductSerializer
>     lookup_field = 'slug'
>     
>     queryset = Product.objects.select_related(
>         'category', 
>         'brand'
>     ).prefetch_related(
>         'media_gallery'
>     ).all()
> ```
> 

**چیستی و چرایی این تغییر:**

- **`ReadOnlyModelViewSet` چیست؟** این کلاس جادویی ترکیبی از `ListAPIView` (برای نمایش همه) و `RetrieveAPIView` (برای نمایش یکی) است. چون محصولات قرار نیست توسط کاربران عادی ساخته (`POST`) یا پاک (`DELETE`) شوند، از نسخه `ReadOnly` استفاده کردیم تا امنیت حفظ شود.
- **چرا `@extend_schema_view` تغییر کرد؟** به جای اینکه دکوراتور را روی دو کلاس مختلف بنویسیم، آن را یک‌بار بالای ViewSet نوشتیم. کلمه `list` به متدِ نمایش همه، و کلمه `retrieve` به متدِ نمایش جزئیات اشاره می‌کند.

> 67-  چون از ViewSet استفاده کردیم، فایل `apps/products/urls.py` هم باید تغییر کند. آن را باز کنید و با این کد جایگزین کنید:
> 
> 
> ```python
> from rest_framework.routers import DefaultRouter
> from .views import ProductViewSet
> 
> # استفاده از روتر برای تولید خودکار URLها
> router = DefaultRouter()
> router.register('', ProductViewSet, basename='product')
> 
> urlpatterns = router.urls
> ```
> 

**چرایی این تغییر:**

- **`DefaultRouter` چیست؟** روترها ابزارهای هوشمندی هستند که وقتی یک `ViewSet` به آن‌ها می‌دهید، خودشان می‌فهمند که باید مسیر `/` را برای لیست محصولات و مسیر `/<slug:slug>/` را برای جزئیات محصول بسازند. این یعنی کدهای `urls.py` به شدت خلوت و تمیز می‌شوند.

<aside>
📢

این قسمت اختیاری هست

</aside>

برای ایجاد یک نقطه ورود (API Root) که تمام مسیرها را به صورت لینک‌های قابل کلیک در مرورگر نمایش دهد، Django REST Framework (DRF) یک قابلیت عالی به نام Browsable API دارد.

برای پیاده‌سازی این ویژگی، بهترین روش استفاده از یک `api_view` است. شما درخواست کردید که از Serializer هم استفاده شود؛ اگرچه برای مسیرهای ثابت (Static URLs) معمولاً نیازی به سریالایزر نیست و دیکشنری‌های ساده پایتون کفایت می‌کنند، اما من کد را طوری تنظیم می‌کنم که هم از سریالایزر عبور کند (برای حفظ ساختار یکپارچه) و هم دسترسی آن برای همه آزاد (Public) باشد.

در ادامه مراحل تغییرات در دو فایل `urls.py` و `views.py` آورده شده است.

### ویرایش فایل `urls.py`

ابتدا باید برای مسیرهای خود پارامتر `name` تعریف کنید تا بتوانیم در صورت نیاز به آن‌ها ارجاع دهیم و مسیر اصلی (root) را به یک view متصل کنیم.

```python
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    # 📌 مسیر اصلی که لیست تمام API ها را نشان می‌دهد
    path('', views.api_root_view, name='api-root'),

     #....
]
```

### . اضافه کردن ویو و سریالایزر در `views.py`

حالا در فایل `project/apps/api/views.py`، یک سریالایزر ساده برای تعیین ساختار خروجی می‌سازیم و سپس ویوی `api_root_view` را با دسترسی آزاد (`AllowAny`) ایجاد می‌کنیم.

برای اینکه لینک‌ها در مرورگر به صورت کامل (Absolute URI) و قابل کلیک نمایش داده شوند، از متد `request.build_absolute_uri()` استفاده می‌کنیم. این روش بسیار امن است زیرا به نام‌گذاری (namespacing) داخل فایل‌های `include` شده وابستگی ندارد.

```python
from rest_framework.permissions import AllowAny
from rest_framework import serializers as rest_serializers

# --- View ---
@api_view(['GET'])
@permission_classes([AllowAny]) # 🔓 دسترسی آزاد برای همه کاربران
def api_root_view(request):
    """
    نقطه ورود API که مسیرهای موجود را لیست می‌کند.
    """
    # ساخت دیتای خام شامل لینک‌های قابل کلیک
    raw_data = {
        "authentication": {
            "token": request.build_absolute_uri('token/'),
            "token_refresh": request.build_absolute_uri('token/refresh/'),
        },
        "user_management": {
            "me": request.build_absolute_uri('me/'),
        },
        "resources": {
            "customers": request.build_absolute_uri('customers/'),
            "products": request.build_absolute_uri('products/'),
        }
    }
    
    # عبور دادن دیتا از سریالایزر (طبق درخواست شما)
    serializer = APIDirectorySerializer(data=raw_data)
    serializer.is_valid(raise_exception=True)
    
    # بازگرداندن پاسخ که توسط DRF به صورت گرافیکی رندر می‌شود
    return Response(serializer.validated_data)

```

### مزایای این روش:

- **رابط کاربری DRF:** وقتی این مسیر `http://your-domain/api/` را در مرورگر باز کنید، پنل زیبای Django REST Framework به شما یک فایل JSON قالب‌بندی شده به همراه لینک‌های آبی‌رنگ و قابل کلیک برای هر بخش (احراز هویت، محصولات و...) نمایش می‌دهد.
- **توسعه‌پذیری:** دسته‌بندی لینک‌ها در دیکشنری (مثل `resources` و `authentication`) به تیم فرانت‌اند کمک می‌کند ساختار API را بهتر درک کنند.

دلیل اینکه در مرورگر صفحه سفید می‌بینید، به احتمال خیلی زیاد به **سمت کلاینت (مرورگر)** برمی‌گردد. در پروژه‌های جنگو، این اتفاق معمولاً به چند دلیل مشخص رخ می‌دهد:

### ۱. تداخل Django Debug Toolbar با DRF (محتمل‌ترین دلیل)

در لاگ‌های شما مشخص است که `debug_toolbar` در حال لود شدن است (`GET /static/debug_toolbar/...`). گاهی اوقات اسکریپت‌ها و استایل‌های Debug Toolbar با رابط کاربری DRF تداخل پیدا می‌کنند (مخصوصاً بر سر نسخه jQuery) و باعث می‌شوند رندر صفحه در مرورگر متوقف شود و یک صفحه سفید ببینید.

- **راه‌حل تست:** برای چند لحظه در فایل `settings.py`، میدل‌ور (Middleware) مربوط به `debug_toolbar` را کامنت کنید و سرور را ری‌استارت کنید. اگر صفحه DRF نمایش داده شد، مشکل از همین تداخل است.

### ۲. افزونه‌های مرورگر (AdBlockers یا JSON Viewers)

بسیاری از مسدودکننده‌های تبلیغات (مثل uBlock Origin یا AdBlock) وقتی کلمه `api` را در URL می‌بینند، به صورت پیش‌فرض درخواست‌ها را بلاک کرده یا تگ‌های صفحه را پنهان می‌کنند. همچنین اگر افزونه‌ای برای زیباسازی JSON (JSON Formatter) نصب کرده باشید، ممکن است سعی کند صفحه HTMLِ تولید شده توسط DRF را به عنوان JSON پارس کند و در نتیجه کرش کند و صفحه سفید شود.

- **راه‌حل تست:** مسیر را در حالت ناشناس مرورگر (Incognito/Private Window) باز کنید.

### ۳. بررسی دیتای خام با پارامتر format

برای اینکه خیالتان راحت شود که دیتای سریالایزر به درستی در حال ارسال است و مشکل فقط از قالب گرافیکی DRF است، به انتهای URL خود در مرورگر این عبارت را اضافه کنید:
`http://127.0.0.1:8000/api/?format=json`
با این کار DRF متوجه می‌شود که شما صفحه HTML را نمی‌خواهید و فقط دیتای خالص JSON را به شما برمی‌گرداند. اگر با این کار دیتا را دیدید، کدهای `views.py` شما کاملاً بی‌نقص هستند.

### ۴. کنسول مرورگر (Developer Tools)

کلید `F12` را در مرورگر بزنید و به تب **Console** بروید. اگر صفحه به دلیل خطاهای جاوااسکریپتی (مثل لود نشدن صحیح یک فایل یا تداخل متغیرها) سفید شده باشد، خطاها را با رنگ قرمز در اینجا خواهید دید.

<aside>
📢

# پایان Part-5

</aside>