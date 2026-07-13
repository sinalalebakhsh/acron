# ACRON Methodology Part-0 Table of contents

![04- ChatGPT Image Jun 15, 2026, 01_54_47 AM.png](04-_ChatGPT_Image_Jun_15_2026_01_54_47_AM.png)

![02- MVT Design Pattern.png](02-_MVT_Design_Pattern.png)

![03- Blank diagram.jpeg](03-_Blank_diagram.jpeg)

# فاز 1: Foundation

هدف:

<aside>
📢

- ساخت پروژه
- ساختار settings
- MySQL
- apps
- core
</aside>

# فاز 2: Infrastructure

هدف:

<aside>
📢

- CustomUser
- Admin
- DRF
- JWT
- Pagination
- Permissions
- Authentication
- Base API Settings
</aside>

# فاز 3: Customer Domain

**هدف:**

ساخت اولین Domain واقعی پروژه.

تا الان همه چیز Infrastructure بود.

از اینجا وارد Business Domain می‌شویم.

<aside>
📢

- Customer Model
- Customer Signal
- Customer Admin
- Customer Serializer
- GET /api/customers/me/
- PATCH /api/customers/me/
- JWT Protection
</aside>

# فاز 4: Product Domain

نحوه آپلود ، تغییر(جابه جایی) ، حذف تصویر توسط ادمین برای محصولات سایت 

نحوه آپلود ، تغییر(جابه جایی) ، حذف تصویر  توسط کاربران برای پروفایل ، محصولات شخصی ، ارسال تصویر در چت شخصی بین کاربران.

https://pillow.readthedocs.io/en/stable/handbook/tutorial.html#identify-image-files

https://www.geeksforgeeks.org/python/imagefield-django-models/

مدل‌ها:

- Category
- Brand
- Product
- ProductImage
- Comment
- 
- UUID
- Slug
- Inventory
- Optimization
- select_related
- prefetch_related
- N+1 Problem

# فاز 5: Cart Domain

مدل‌ها:

- Cart
- CartItem

# فاز 6: Order Domain

مدل ها:

- Order
- OrderItem
- OrderStatus

# فاز 7: Payment Domain

مدل ها:

- Payment
- Transaction

# فاز 8: Service Layer

مدل ها:

- OrderService
- CartService
- PaymentService

اینجا پروژه از CRUD ساده خارج می‌شود. مثلاً:

```python
OrderService.create_order()
PaymentService.pay()
CartService.add_item()
```

# فاز 9: Event Bus

مثلاً: 

```python
OrderCreatedEvent
```

باعث می شود:

```python
SendEmailHandler
```

```python
CreateInvoiceHandler
```

اجرا شوند.

# فاز 10: Production Ready

- Testing
- Docker
- Redis
- Celery
- Nginx
- PostgreSQL
- Logging
- Monitoring

ارتباط Swagger و DRF چگونه شکل می‌گیرد؟

Swagger به صورت پیش‌فرض کدهای پایتون یا جنگو را نمی‌فهمد. برای برقراری این ارتباط، ما از پکیج‌های واسطه (مانند `drf-spectacular` که در حال حاضر مدرن‌ترین و پیشنهادی‌ترین گزینه است، یا پکیج قدیمی‌تر `drf-yasg`) استفاده می‌کنیم.

این پکیج‌ها کدهای پروژه DRF شما (مانند Viewها، Serializerها، URLها و Permissionها) را می‌خوانند، آن‌ها را تحلیل می‌کنند و به صورت خودکار یک فایل استاندارد (معمولاً JSON یا YAML) تولید می‌کنند. سپس Swagger UI این فایل را می‌خواند و آن را به یک رابط کاربری زیبا و تعاملی در مرورگر تبدیل می‌کند.

---

اهمیت این ارتباط در چیست؟

اهمیت اصلی Swagger در ایجاد یک **زبان مشترک** بین تیم‌های مختلف است:

- **تیم بک‌اند (شما):** کدهایتان را می‌نویسید و بدون نیاز به نوشتن دستی مستندات، APIهایتان به روز می‌مانند.
- **تیم فرانت‌اند / موبایل:** دقیقاً می‌دانند چه Endpointهایی وجود دارد، چه پارامترهایی (Body, Query, Path) باید ارسال کنند و در جواب چه ساختار داده‌ای (JSON) دریافت خواهند کرد.
- **تیم تست (QA):** به راحتی می‌توانند ورودی‌های مختلف را تست کرده و خروجی‌ها را بررسی کنند.

---

چه کمکی به پروژه Django REST Framework می‌کند؟

اضافه کردن Swagger به یک پروژه DRF مزایای فوق‌العاده‌ای دارد:

- **مستندسازی خودکار و همیشه به‌روز (Auto-Documentation):** بزرگترین کابوس برنامه‌نویس‌ها، مستنداتی است که با کد واقعی هم‌خوانی ندارند. در DRF وقتی شما فیلدی را به Serializer اضافه یا کم می‌کنید، Swagger به صورت خودکار در همان لحظه مستندات را آپدیت می‌کند.
- **تست تعاملی (Interactive Testing):** رابط کاربری Swagger دارای دکمه‌ای به نام `Try it out` است. این یعنی توسعه‌دهندگان فرانت‌اند نیازی به ابزارهایی مثل Postman برای تست ساده APIها ندارند؛ آن‌ها می‌توانند مستقیماً از داخل مرورگر درخواست بفرستند و جواب را ببینند.
- **پشتیبانی از احراز هویت (Authentication):** شما می‌توانید به Swagger بگویید که پروژه شما از چه نوع توکنی (مثل JWT یا Token Auth) استفاده می‌کند. کاربر می‌تواند در همان صفحه Swagger لاگین کرده و APIهای محافظت‌شده را تست کند.
- **تولید خودکار کدهای کلاینت (Code Generation):** ابزارهایی وجود دارند که می‌توانند فایل خروجی Swagger را بگیرند و کدهای اتصال به API را برای فرانت‌اند (مثلاً در React، Angular یا Flutter) به صورت خودکار تولید کنند. این کار سرعت توسعه تیم را به شدت بالا می‌برد.
- **استانداردسازی کدها:** وقتی می‌دانید که کدهای شما قرار است توسط Swagger خوانده و مستند شوند، ناخودآگاه کدهای تمیزتری می‌نویسید، Docstringهای بهتری برای Viewها قرار می‌دهید و از Serializerهای استانداردتری استفاده می‌کنید.

# فاز 11 **Microservices**

هدف:

- جداسازی Backend
- جداسازی Frontend
- جداسازی Database
- جداسازی Presentation
- تعیین ساختار Business Logic Layer
- تعیین ساختار Data Access Layer

---

مهم ترین قسمت تمام پروژه اینجا طراحی و توسعه داده میشود ، یعنی کدهای به شدت **ماژولار و تفکیک‌شده برای توزیع پذیری تمام پروژه برای برنامه نویسان.**

تکامل به سمت سیستم سلسله‌مراتبی (زمانی که پروژه بزرگ شد)

وقتی پروژه شما رشد کرد و ده‌ها مشارکت‌کننده پیدا کرد، دیگر زمان کافی برای بررسی همه PRها نخواهید داشت. اینجا دقیقاً نقطه‌ای است که این مدل اجرا می‌شود:

- **تعریف CODEOWNERS:** در گیت‌هاب و گیت‌لب فایلی به نام `CODEOWNERS` وجود دارد. شما می‌توانید در این فایل تعیین کنید که مثلاً پوشه `/api` متعلق به شخص X و پوشه `/frontend` متعلق به شخص Y است.
- **تفویض اختیار:** از این پس، اگر کسی بخواهد در پوشه `/api` تغییری ایجاد کند، گیت‌هاب به طور خودکار از شخص X می‌خواهد که کد را بررسی کند. وقتی شخص X تایید کرد، شما (به عنوان خالق پروژه) با خیال راحت و بدون نیاز به خواندن خط به خط کد، آن را در سیستم اصلی ادغام می‌کنید. شما به شخص X اعتماد می‌کنید، نه به توسعه‌دهنده ناشناس.

مستندسازی قوانین بازی (CONTRIBUTING.md)

یک سیستم توزیع‌شده بدون قانون، به هرج و مرج ختم می‌شود.

- **اقدام شما:** یک فایل `CONTRIBUTING.md` در پروژه بنویسید. در آن توضیح دهید که معماری پروژه چیست، نام‌گذاری شاخه‌ها چطور باید باشد و کدهای ارسالی چه استانداردهایی باید داشته باشند.

---

> تبدیل پروژه به معماری 3 لایه
> 
> 
> معماری سه‌لایه یعنی شما بدانید چگونه کدهای پردازشی (Logic) را از کدهای دیتابیس (ORM) و کدهای ارسال پاسخ (API Views) جدا کنید تا اگر فردا دیتابیس عوض شد یا طراحی API تغییر کرد، نیازی به دست زدن به منطق اصلی برنامه نداشته باشید.
> 
> منظور معماری سه‌لایه در سطح سمت سرور (Backend) است. این سه لایه عبارتند از:
> 
> ۱. لایه نمایش (Presentation Layer)
> 
> - **وظیفه:** این لایه مستقیماً با کاربر یا کلاینت (مثل اپلیکیشن موبایل یا وب‌سایت) در ارتباط است. در واقع این لایه موظف است دریافت اطلاعات از کاربر را مدیریت کرده و نتایج را به شکلی زیبا و قابل فهم (مثل JSON در APIها) به او برگرداند.
> - **در چارچوب Django:** اگر از Django REST Framework استفاده کنید، بخش‌هایی مثل `Serializers` و `Views` دقیقاً همین نقش را بازی می‌کنند (دریافت درخواست، اعتبارسنجی اولیه، و ارسال پاسخ).
> 
> ۲. لایه منطق تجاری (Business Logic Layer)
> 
> - **وظیفه:** این لایه «مغز متفکر» برنامه است. قوانین اصلی کسب‌وکار در اینجا قرار دارد. مثلاً اگر یک فروشگاه اینترنتی دارید، محاسبه‌ی تخفیف‌ها، بررسی موجودی کالا، و اینکه آیا کاربر اجازه‌ی خرید این محصول را دارد یا خیر، همگی در این لایه پردازش می‌شوند.
> - **مهم‌ترین ویژگی:** این لایه نباید بداند اطلاعات از کجا آمده‌اند (دیتابیس یا فایل) و قرار است کجا بروند (موبایل یا وب). فقط پردازش را انجام می‌دهد.
> 
> ۳. لایه دسترسی به داده (Data Access Layer)
> 
> - **وظیفه:** این لایه فقط و فقط با ذخیره‌سازی و بازیابی اطلاعات سر و کار دارد (مثل ارتباط با دیتابیس‌های PostgreSQL، MySQL و...). هیچ قانونی درباره‌ی کسب‌وکار در این لایه نیست.
> - **در چارچوب Django:** در Django، سیستم **ORM** (مدل‌ها یا Models) و نوشتن کوئری‌ها نقش این لایه را ایفا می‌کنند.

# چک لیست :

**فاز ۱: Foundation (پایه‌ریزی)**

- [ ]  ساخت پوشه پروژه و ایجاد محیط مجازی با `pipenv`
- [ ]  نصب Django و فعال‌سازی محیط مجازی (`pipenv shell`)
- [ ]  ساخت پروژه جنگو در مسیر فعلی (`django-admin startproject config .`)
- [ ]  ساخت اپلیکیشن `accounts` و انتقال آن به پوشه `apps/`
- [ ]  ساخت مدل `CustomUser` با ایمیل یونیک در `apps/accounts/models.py`
- [ ]  تبدیل `settings.py` به پکیج (`base.py`, `development.py`, `production.py`, `__init__.py`)
- [ ]  انتقال تنظیمات مشترک به `base.py` (BASE_DIR, SECRET_KEY, INSTALLED_APPS, MIDDLEWARE و ...)
- [ ]  تنظیم `DEBUG = True` در `development.py`
- [ ]  تنظیم `AUTH_USER_MODEL = "accounts.CustomUser"` در `base.py`
- [ ]  ساخت اپلیکیشن‌های Domain (customers, products, carts و ...) و انتقال به `apps/`
- [ ]  کامنت کردن اپلیکیشن‌های غیرضروری در `INSTALLED_APPS` (به جز accounts)
- [ ]  اصلاح فایل `apps.py` تمام اپ‌ها (تغییر `name` به `'apps.xxx'`)
- [ ]  ساخت دستی پکیج `core/` (بدون startapp) و فایل‌های خالی آن
- [ ]  تنظیم دیتابیس MySQL در `development.py` (با utf8mb4)
- [ ]  نصب درایور `mysqlclient`
- [ ]  ساخت دیتابیس `acron` در MySQL Workbench
- [ ]  اجرای `python manage.py check` برای تست اتصال
- [ ]  اجرای `makemigrations` و `migrate` برای ساخت جداول
- [ ]  ساخت سوپریوزر (`createsuperuser`)
- [ ]  اجرای سرور و تست ورود به ادمین

**فاز ۲: Infrastructure (زیرساخت API)**

- [ ]  نصب `djangorestframework` و `djangorestframework-simplejwt`
- [ ]  ثبت `rest_framework` و `apps.accounts` در `INSTALLED_APPS`
- [ ]  تنظیمات پایه DRF و JWT در `base.py` (اعتبارسنجی، توکن لایف‌تایم، پجینیشن)
- [ ]  ساخت اپلیکیشن `api` و انتقال آن به `apps/`
- [ ]  ساخت `urls.py` در `apps/api/` و اتصال آن به `config/urls.py` (مسیر `/api/`)
- [ ]  تست مسیر API Root
- [ ]  افزودن مسیرهای JWT (`/api/token/` و `/api/token/refresh/`)
- [ ]  ساخت اولین Protected View (`/api/me/`)
- [ ]  تست کامل جریان JWT با Postman (دریافت توکن، دسترسی به ME، تست خطای 401، تست انقضای توکن، رفرش توکن)
- [ ]  ساخت `UserSerializer` در `apps/api/serializers.py`
- [ ]  ساخت پرمیشن سفارشی `IsOwner` در `apps/api/permissions.py` (برای استفاده در آینده)

**فاز ۳: Customer Domain (دامنه مشتری)**

- [ ]  فعال کردن `apps.customers` در `INSTALLED_APPS`
- [ ]  نوشتن مدل `Customer` با تصمیمات معماری گرفته شده (کدها در پایین)
- [ ]  ثبت مدل در فایل `admin.py`
- [ ]  نوشتن `CustomerSerializer`
- [ ]  اجرای `makemigrations customers` و