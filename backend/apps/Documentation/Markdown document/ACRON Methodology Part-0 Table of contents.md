# ACRON Methodology Part-0 Table of contents

![](https://www.hotspotshield.com/imgs/illustrations/small/shield.png)

## Protecting your private data

Protect
 your identity, integrity and family data while searching, browsing and 
shopping, in dating apps and communicating. We encrypt your data and do 
not make any records of your activities.

# **The ACRON Vision**

```python
                         ACRON
                           │
          ┌────────────────┼────────────────┐
          │                │                │
       Social           Marketplace          AI
          │                │                │
      ┌───┴───┐        ┌───┴────┐       ┌───┴────┐
      │       │        │        │       │        │
   Dating   Chat      Employer Worker  Advisor Recommendation
      │       │        │        │       │        │
      └───────┴────────┴────────┴───────┴────────┘
                           │
                           ▼
                    Explore Engine
                           │
                           ▼
                  Personalization
                           │
                           ▼
                   AI / ML Layer
```

### قانون ACRON × Sina

**هیچ کدی را صرفاً برای اینکه «کار کند» وارد پروژه نمی‌کنیم.**

هر تغییر باید حداقل این چرخه را داشته باشد:

```python
1. مسئله چیست؟
        ↓
2. چرا باید حلش کنیم؟
        ↓
3. معماری فعلی چه می‌گوید؟
        ↓
4. چه راه‌حل‌هایی داریم؟
        ↓
5. چرا این راه‌حل را انتخاب کردیم؟
        ↓
6. چه فایل‌هایی باید تغییر کنند؟
        ↓
7. کد را خط‌به‌خط می‌نویسیم
        ↓
8. هر خط را توضیح می‌دهیم
        ↓
9. اجرا می‌کنیم
        ↓
10.ا Test می‌نویسیم
        ↓
11. نتیجه را بررسی می‌کنیم
        ↓
12. بعد می‌رویم مرحله بعد
```

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

<aside>
💡

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
</aside>

# فاز 5: Cart Domain

مدل‌ها:

<aside>
💡

- Cart
- CartItem
</aside>

# فاز 6: Order Domain

مدل ها:

<aside>
💡

- Order
- OrderItem
- OrderStatus
</aside>

# فاز 7: Payment Domain

مدل ها:

<aside>
💡

- Payment
- Transaction
</aside>

# فاز 8: Shipment & Fulfillment Domain

مدل ها:

<aside>
💡

- ShipmentStatus
- CarrierChoices
- Shipment
</aside>

# فاز 9:  MCP - Model Context Protocol

اپلیکیشن ها:

<aside>
💡

- MCP Model Context Protocol
- advisor
</aside>

# فاز 10: Service Layer

مدل ها:

<aside>
💡

- OrderService
- CartService
- PaymentService
</aside>

اینجا پروژه از CRUD ساده خارج می‌شود. مثلاً:

```python
OrderService.create_order()
PaymentService.pay()
CartService.add_item()
```

# فاز 11: Frontend  - Presentation Layer

use react, axios, html, css, Auth Context, etc.

# فاز 12: AI - Advisor

# فاز 12: Event Bus

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

# فاز 13: PRT - Production Ready Testing

- Testing

# فاز 14: PRC - Production Ready Cashing

- Redis
- Celery

# فاز 15: PRS - Production Ready Serving

- Docker
- Nginx

# فاز 16: PRD - 
Production Ready Advanced Data Base

- PostgreSQL

# فاز 17: PRM - Production Ready Monitoring

- Monitoring
- Logging

# فاز 18: **Microservices**

هدف:

- جداسازی Backend
- جداسازی Frontend
- جداسازی Database
- جداسازی Presentation
- تعیین ساختار Business Logic Layer
- تعیین ساختار Data Access Layer

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