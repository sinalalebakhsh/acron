# ACRON Project Export

## Project Structure
```text
├── .github/
│   └── workflows/
│       └── django.yml
├── apps/
│   ├── Documentation/
│   │   ├── Markdown document/
│   │   │   ├── ACRON Methodology Part-0.md
│   │   │   ├── ACRON Methodology Part-1.md
│   │   │   ├── ACRON Methodology Part-2.md
│   │   │   ├── ACRON Methodology Part-3.md
│   │   │   ├── ACRON Methodology Part-4.md
│   │   │   ├── ACRON Methodology Part-5.md
│   │   │   ├── ACRON Methodology Part-6.md
│   │   │   ├── ACRON Methodology Part-7.md
│   │   │   ├── ACRON Methodology Part-8.md
│   │   │   └── ACRON Methodology Part-9.md
│   │   └── html document/
│   ├── accounts/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── carts/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── customers/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_api.py
│   │   │   ├── test_models.py
│   │   │   ├── test_serializers.py
│   │   │   └── test_signals.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── notifications/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── orders/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── payments/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── services.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── products/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── reviews/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── shipments/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── services.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── brands/
│   └── 2026/
│       └── 07/
├── categories/
│   └── 2026/
│       └── 07/
├── config/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   ├── wsgi.py
│   └── zxcZXCsettings.txt
├── core/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── mixins.py
│   ├── pagination.py
│   ├── permissions.py
│   └── services.py
├── products/
│   ├── gallery/
│   │   └── 2026/
│   │       └── 07/
│   └── main/
│       └── 2026/
│           └── 07/
├── CONTRIBUTING.md
├── Documentation.md
├── README.md
├── acron_codebase.md
└── requirements.txt

```
---

## Source Code Files

### File: `CONTRIBUTING.md`
```md

# Contributing to the ACRON

Thank you very much for your interest in contributing to the development of ACRON! Your presence will greatly help the growth and improvement of this architecture.<br>

To make the participation process transparent and enjoyable for everyone, please read the following guide before you begin.<br>

## 🐛(Bug Reports)
If you encounter an error in the project, please check the Issues section to make sure it has not already been filed before creating a new issue. <br>

To file a new bug, include the following in your description:
*   The version of Python and Django you are using.
    
*   Detailed steps to reproduce the error.

*   Expected behavior and behavior that is currently occurring.<br>

## 💡 Feature Requests
We always welcome new ideas! To suggest a feature:<br>
1. Create a new Issue with the tag `enhancement`.<br>
2. Clearly explain what problem this feature solves or what value it adds to ACRON.<br>

## 💻 Development Setup

To run the project on your system and start development, follow these steps:<br>

1. **Fork Or Clone:** 

```bash
git clone [https://github.com/sinalalebakhsh/acron.git](https://github.com/sinalalebakhsh/acron.git)

cd acron

pipenv shell

```

📏 Coding Standards

To maintain code integrity, please note the following:

* Python code must follow PEP 8 standards.
* Variables, functions, and classes must be named meaningfully and readably.
* If you add a new feature or change the logic of the APIs, please also update the docstrings.

🔀 Steps to Submit a Pull Request (PR)

1. Fork the project and clone it to your system.<br>

2. Create a new branch for your changes. <br>

3. The branch name should be descriptive of your work (e.g. fix-database-query or feature-add-swagger).<br>

```
git checkout -b feature-your-feature-name
```

4. Apply your changes and make sure the project runs without errors.

5. Write clear and readable commits.

6. Push the changes to your forked repository.

7. On GitHub, submit a Pull Request to the main (or develop, if available) branch.

Your changes will be reviewed as soon as possible and feedback will be provided if any corrections are needed. <br>

Thanks again for your support! <br>

Sina Lalehbakhsh <br>
2026, Friday, Tir 19, 1405 AP <br>




```

### File: `Documentation.md`
```md
## ACRON Methodology Documentation Parts:

* [Part-0](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-0-Table-of-contents-38fda1eb8b9d8073a8cfebf21856e8f3)
* [Part-1](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-1-386da1eb8b9d80b7b9c9d781ee65d5db)
* [Part-2](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-2-38fda1eb8b9d801aaf55c8c2629235bb)
* [Part-3](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-3-390da1eb8b9d8029b85ed7359b7497ec)
* [Part-4](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-4-390da1eb8b9d8065b570d372ffd41e8d)
* [Part-5](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-5-390da1eb8b9d80d1a809d7536e73c092)
* [Part-6](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-6-395da1eb8b9d80649254fa95c4a9ef97)
* [Part-7](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-7-397da1eb8b9d80a48ae4d3d71d491885)
* [Part-8](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-8-399da1eb8b9d80fc95b4da6179551f44)
* [Part-9](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-9-39ada1eb8b9d80e0a6fbefe0ba308fb2)



```

### File: `README.md`
```md
# 🚀 ACRON: Enterprise Django Reference Architecture

> *"Plant the acorn seed, and it will grow into a mighty oak."*

**ACRON** is an open-source reference architecture designed to bridge the gap between basic Django tutorials and real-world, enterprise-grade software engineering. It provides a structured, step-by-step development roadmap for both Junior and Senior developers. 

Our core philosophy follows the **80/20 Rule**:
* **80% Progress Structure & Engineering:** Strict adherence to clean architecture, scalability, financial data integrity, and industry best practices.
* **20% Creativity & "Artomize":** Leaving room for developer innovation, flexibility, and randomized artistic problem-solving!

---

## 🔗 Documentation & Methodology
* 📖 **Core Methodology Documentation:** [Read Documentation Parts](https://github.com/sinalalebakhsh/acron/blob/main/Documentation.md)
* 🧠 **Project Roadmap & Introduction:** [View on Notion](https://sinalalenakhsh.notion.site/ACRON-387da1eb8b9d8005a372ce7394463792)
* 🤝 **Contributing Guide:** [How to Contribute](https://github.com/sinalalebakhsh/acron/blob/main/CONTRIBUTING.md)

---

## 🏛️ Architecture & Technical Highlights (What We Built)

Unlike standard Django apps that rely on "Fat Views" or messy serializers, ACRON is built upon a **production-ready, highly decoupled architecture**:

* **True Service-Layer Architecture:** Complete separation of concerns. HTTP requests and formatting live in Views/Serializers, while 100% of the business logic is isolated in highly testable `services.py` modules.
* **Financial Integrity & ACID Compliance:** Utilization of `@transaction.atomic` boundaries, immutable order snapshots (freezing historical prices), and automated Time-To-Live (TTL) expiration mechanisms for inventory safety.
* **Database & Query Optimization:** Built-in protection against N+1 query disasters using Django ORM's `select_related` and `prefetch_related`.
* **Enterprise Security:** Implementing non-sequential UUID primary keys for sensitive domains (Carts, Orders) and strict JWT authentication flows.
* **Modern API Documentation:** Fully automated, interactive OpenAPI 3.0 documentation integrated via `drf-spectacular` (Swagger UI & Redoc).

---

## 👥 Who Are You? (Welcome to the Community!)

We believe in open, collaborative software development. No matter your current role, there is a place for you here:

* 💻 **Can you be a contributor to this project?** **Yes!** Check our contributing issues and submit a PR.
* 🚪 **Can you invite yourself into this project?** **Yes!** This is an open-source initiative built for the community.
* 👁️ **Can you just be a visitor exploring the code?** **Yes!** Feel free to use ACRON as an architectural template for your own projects.
* 📈 **Can you invest in or adopt this reference project?** **Yes!** It is built to scale for commercial and financial systems.
* 🔍 **Can you be a code reviewer?** **Yes!** We welcome architectural critiques and code reviews.

---

## 🗺️ Roadmap & Future Developments

We are actively developing and expanding the architecture. Next steps in our roadmap include:
- [x] **API Documentation:** Integrated OpenAPI 3.0 / Swagger UI.
- [x] **Payment Gateway Domain:** Connecting orders to banking interfaces with secure callback handling.
- [ ] **Asynchronous Background Tasks:** Integrating Celery and Redis for automated inventory release and notification systems.
- [ ] **Shared Core Services:** Expanding `core/services.py` for enterprise SMS, Email, and PDF generation.

---

## 🤖 Our Philosophy on AI & Code Quality: No "Vibe Coding"

We explicitly **do not use "Vibe Coding"** in this project. 

Copy-pasting unverified AI-generated code without understanding the underlying architectural mechanics is the number one trap for modern developers. In the ACRON ecosystem, **artificial intelligence is treated strictly as an assistant and a tool—nothing more, nothing less.** The core architecture, database schema design, and domain logic are driven by human engineering and critical thinking.

We acknowledge the assistance of the following AI tools in debugging, translating, and refining code details:
* [Gemini](https://gemini.google.com/)
* [Claude](https://claude.ai/)
* [ChatGPT](https://chatgpt.com)
* [Chat Z AI](https://chat.z.ai) / [DeepSeek](https://chat.deepseek.com/)
* [OCR & Converting Tools](https://ocr.z.ai/)
* [Image & Design Assistants](https://image.z.ai/)

### 🌍 A Note from the Founder
Despite the severe challenges and limitations imposed by geographical sanctions on developers in Iran, this project was developed with passion, resilience, and the aid of modern technology. **It is my sincere hope that a future of friendly relationships, open collaboration, and borderless connection will be established between Iranian developers and the global tech community.**





```

### File: `acron_codebase.md`
```md

```

### File: `requirements.txt`
```txt
-i https://pypi.org/simple
asgiref==3.11.1; python_version >= '3.9'
attrs==26.1.0; python_version >= '3.9'
django==6.0.6; python_version >= '3.12'
django-debug-toolbar==7.0.0; python_version >= '3.10'
djangorestframework==3.17.1; python_version >= '3.10'
djangorestframework-simplejwt==5.5.1; python_version >= '3.9'
drf-spectacular==0.29.0; python_version >= '3.7'
inflection==0.5.1; python_version >= '3.5'
jsonschema==4.26.0; python_version >= '3.10'
jsonschema-specifications==2025.9.1; python_version >= '3.9'
mysqlclient==2.2.8; python_version >= '3.10'
numpy==2.5.0; python_version >= '3.12'
opencv-python==5.0.0.93; python_version >= '3.6'
pillow==12.3.0; python_version >= '3.10'
pyjwt==2.13.0; python_version >= '3.9'
pyyaml==6.0.3; python_version >= '3.8'
referencing==0.37.0; python_version >= '3.10'
rpds-py==2026.6.3; python_version >= '3.11'
sqlparse==0.5.5; python_version >= '3.8'
tzdata==2026.2; python_version >= '2'
uritemplate==4.2.0; python_version >= '3.9'

```

### File: `.github\workflows\django.yml`
```yml
name: Django CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    # ۱. راه‌اندازی دیتابیس موقت MySQL روی سرور گیت‌هاب
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: '1234' # دقیقاً مطابق پسورد شما در development.py
          MYSQL_DATABASE: 'acron'      # دقیقاً مطابق نام دیتابیس شما
        ports:
          - 3306:3306
        options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=3

    strategy:
      matrix:
        # ۲. هماهنگی باrequirements: جنگو ۶ حداقل به پایتون ۳.۱۲ نیاز دارد
        python-version: ["3.12", "3.13"]

    steps:
    - uses: actions/checkout@v5

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'

    # ۳. نصب ابزارهای لینوکسی مورد نیاز برای کامپایل کتابخانه mysqlclient
    - name: Install Linux Dependencies for MySQL
      run: |
        sudo apt-get update
        sudo apt-get install -y default-libmysqlclient-dev pkg-config build-essential

    - name: Install Python Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # ۴. اجرای تست‌ها با معرفی آدرس جدید فایل تنظیمات
    - name: Run Tests
      env:
        DJANGO_SETTINGS_MODULE: config.settings.development
      run: |
        python manage.py test

```

### File: `apps\accounts\__init__.py`
```python

```

### File: `apps\accounts\admin.py`
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email',"usable_password", "password1", "password2", 'first_name' ,'last_name'),
            },
        ),
    )


```

### File: `apps\accounts\apps.py`
```python
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'


```

### File: `apps\accounts\models.py`
```python
from django.contrib.auth.models import AbstractUser

from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    


    
```

### File: `apps\accounts\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\accounts\views.py`
```python
from django.shortcuts import render

# Create your views here.

```

### File: `apps\api\__init__.py`
```python

```

### File: `apps\api\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `apps\api\apps.py`
```python
from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api'
```

### File: `apps\api\models.py`
```python
from django.db import models

# Create your models here.

```

### File: `apps\api\permissions.py`
```python
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool((request.user and request.user.is_staff))




```

### File: `apps\api\serializers.py`
```python
# apps/api/serializers.py

from rest_framework import serializers


from apps.accounts import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser

        fields = ['id', 'username', 'email', 'first_name', 'last_name',]


```

### File: `apps\api\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\api\urls.py`
```python
# This file defines the URL patterns for the API app,
# which includes endpoints for managing carts, customers, products, orders, and payments.
from django.urls import include, path


# Importing TokenObtainPairView and TokenRefreshView from rest_framework_simplejwt.views,
# to handle JWT authentication for obtaining and refreshing tokens.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Importing views from the current module,
# which contains the logic for handling various API endpoints.
from . import views



urlpatterns = [
    # API
    path('', include('apps.carts.urls')), 
    # orders
    path('', include('apps.orders.urls')), 
    # 🔑 JWT Authentication
    # JWT
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # 🔐 protected route
    path('me/', views.me),
    #  customers
    path('customers/', include('apps.customers.urls')), # مسیر مشتریان
    #  products
    path('products/', include('apps.products.urls')), # مسیر محصولات اضافه شد!
    # payments
    path('payments/', include('apps.payments.urls')), # مسیر پرداخت اضافه شد!
    # shipments
    path('shipments/', include('apps.shipments.urls')), # مسیر مرسولات اضافه شد!

]
```

### File: `apps\api\views.py`
```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import serializers as rest_serializers


from . import serializers


# 🔐 API محافظت‌شده
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)


# --- Serializer ---
class APIDirectorySerializer(rest_serializers.Serializer):
    """
    یک سریالایزر برای اعتبارسنجی و فرمت‌دهی لیست مسیرهای API.
    """
    authentication = rest_serializers.DictField(child=rest_serializers.URLField())
    user_management = rest_serializers.DictField(child=rest_serializers.URLField())
    resources = rest_serializers.DictField(child=rest_serializers.URLField())




```

### File: `apps\carts\__init__.py`
```python

```

### File: `apps\carts\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `apps\carts\apps.py`
```python
from django.apps import AppConfig


class CartsConfig(AppConfig):
    name = 'apps.carts'

```

### File: `apps\carts\models.py`
```python
from django.db import models

import uuid

from apps.products.models import Product


class Cart(models.Model):
    # الف) جایگزینی 
    # ID
    #  عددی با 
    # UUID
    #  به عنوان کلید اصلی امنیتی
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    # ب) اتصال آیتم به سبد خرید
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    
    # ج) اتصال آیتم به محصول
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    
    # د) تعداد محصول در سبد
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        # هـ) جلوگیری از ساخت دو ردیف برای یک محصول تکراری در یک سبد
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"# Create your models here.





```

### File: `apps\carts\serializers.py`
```python
from rest_framework import serializers
from .models import Cart, CartItem
from apps.products.models import Product

# ۱. ساخت یک سریالایزر سبک و بهینه برای محصول داخل سبد خرید
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # ما در سبد خرید به توضیحات طولانی یا برند نیازی نداریم، فقط اطلاعات حیاتی!
        fields = ['id', 'name', 'price', 'main_image']


# ۲. سریالایزر آیتم‌های داخل سبد (CartItem)
class CartItemSerializer(serializers.ModelSerializer):
    # نمایش اطلاعات محصول به صورت تو در تو، اما با سریالایزر سبک
    product = SimpleProductSerializer(read_only=True)
    
    # تعریف یک فیلد محاسباتی که در دیتابیس وجود ندارد
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    # متد متصل به فیلد محاسباتی بالا
    def get_total_price(self, cart_item: CartItem):
        # قیمت محصول × تعداد آن
        return cart_item.quantity * cart_item.product.price


# ۳. سریالایزر اصلی سبد خرید (Cart)
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    # اتصال آیتم‌ها به سبد خرید (توجه: کلمه items همان related_name در مدل است)
    items = CartItemSerializer(many=True, read_only=True)
    
    # فیلد محاسباتی برای جمع کل مبلغ کل سبد خرید
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'grand_total']

    # متد متصل به فیلد محاسباتی مبلغ کل
    def get_grand_total(self, cart: Cart):
        # یک حلقه پایتونی برای جمع زدن قیمت کل تک‌تک آیتم‌های این سبد
        return sum([item.quantity * item.product.price for item in cart.items.all()])
    

# این کلاس فقط برای زمانی است که کلاینت می‌خواهد محصولی را به سبد اضافه کند (POST)
class AddCartItemSerializer(serializers.ModelSerializer):
    # کلاینت فقط این دو شناسه را برای ما می‌فرستد
    product_id = serializers.IntegerField()
    cart_id = serializers.UUIDField()

    class Meta:
        model = CartItem
        fields = ['id', 'cart_id', 'product_id', 'quantity']

    # اعتبارسنجی: آیا این محصول اصلاً در فروشگاه وجود دارد؟
    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("محصولی با این شناسه یافت نشد.")
        return value

    # اعتبارسنجی: آیا این سبد خرید اصلاً وجود دارد؟
    def validate_cart_id(self, value):
        if not Cart.objects.filter(id=value).exists():
            raise serializers.ValidationError("سبد خریدی با این شناسه یافت نشد.")
        return value

    # قلب تپنده این بخش: تغییر رفتار ذخیره‌سازی برای دور زدن خطای دیتابیس
    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            # سناریو ۱: آیا این محصول از قبل در این سبد خرید وجود دارد؟
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            
            # بله وجود دارد! پس فقط تعداد جدید را با تعداد قبلی جمع کن
            cart_item.quantity += quantity
            cart_item.save()
            
            self.instance = cart_item
            
        except CartItem.DoesNotExist:
            # سناریو ۲: محصول در سبد نیست. پس یک ردیف جدید در دیتابیس بساز
            self.instance = CartItem.objects.create(
                cart_id=cart_id, 
                product_id=product_id, 
                quantity=quantity
            )

        return self.instance


# این کلاس فقط برای زمانی است که کلاینت می‌خواهد تعداد را تغییر دهد (PATCH)
# مثلاً کاربر در سبد خرید دکمه + یا - را می‌زند
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']









```

### File: `apps\carts\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\carts\urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
# ثبت ویوست سبد خرید (آی‌دی این مسیر از نوع UUID خواهد بود)
router.register('carts', CartViewSet, basename='carts')

# ثبت ویوست آیتم‌های سبد خرید
router.register('cart-items', CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', include(router.urls)),
]




```

### File: `apps\carts\views.py`
```python
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import AllowAny


from .models import Cart, CartItem

from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer

@extend_schema_view(
    create=extend_schema(summary="ساخت سبد خرید جدید", tags=['Carts']),
    retrieve=extend_schema(summary="دریافت محتویات سبد خرید", tags=['Carts']),
    destroy=extend_schema(summary="حذف کامل سبد خرید", tags=['Carts']),
)
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    """
    ویو برای مدیریت خودِ سبد خرید (بدون آیتم‌ها).
    توجه: متد List حذف شده است زیرا هیچ کاربری نباید لیست سبد خرید دیگران را ببیند.
    """
    # این خط را اضافه کنید تا قفل شکسته شود
    permission_classes = [AllowAny]
    
    
    # بهینه‌سازی کوئری دیتابیس برای جلوگیری از مشکل N+1 در دریافت آیتم‌های سبد
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer


@extend_schema_view(
    create=extend_schema(summary="افزودن محصول به سبد خرید", tags=['Cart Items']),
    partial_update=extend_schema(summary="تغییر تعداد یک محصول در سبد", tags=['Cart Items']),
    destroy=extend_schema(summary="حذف یک محصول از سبد خرید", tags=['Cart Items']),
)
class CartItemViewSet(ModelViewSet):
    """
    ویو برای مدیریت آیتم‌های داخل سبد خرید.
    """
    # این خط را اضافه کنید تا قفل شکسته شود
    permission_classes = [AllowAny]


    # جلوگیری از استفاده از متد PUT (ما فقط به PATCH برای تغییر تعداد نیاز داریم)
    http_method_names = ['post', 'patch', 'delete']
    
    queryset = CartItem.objects.select_related('product').all()

    # جادوی DRF: انتخاب سریالایزر به صورت دینامیک بر اساس نوع درخواست (Method)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        
        return CartItemSerializer





```

### File: `apps\customers\__init__.py`
```python

```

### File: `apps\customers\admin.py`
```python
from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'user',
        'phone_number',
        'birth_date',
    ]

    search_fields = [
        'user__username',
        'phone_number',
    ]
```

### File: `apps\customers\apps.py`
```python
from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.customers'

    def ready(self):
        from . import signals






```

### File: `apps\customers\models.py`
```python
from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    province = models.CharField(max_length=50, verbose_name="استان")
    city = models.CharField(max_length=50, verbose_name="شهر")
    street = models.TextField(verbose_name="آدرس دقیق (خیابان، پلاک، واحد)")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")

    def __str__(self):
        return f"{self.province}, {self.city} - {self.postal_code}"
    

    
```

### File: `apps\customers\serializers.py`
```python
from datetime import date

from rest_framework import serializers

from .models import Customer

from apps.accounts import models as accounts_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = accounts_models.CustomUser

        fields = [
            'id',
            'username',
            'email',
        ]




class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Customer

        fields = [
            'id',
            'uuid',
            'phone_number',
            'birth_date',
            'user',
        ]
        read_only_fields = [
            'id',
            'uuid',
            'user',
        ]

    def validate_phone_number(self, value):
        if value and len(value)<10:
                raise serializers.ValidationError(
                "Phone number is too short."
                    )
        
        return value

    def validate_birth_date(self, value):

        if value and value > date.today():
            raise serializers.ValidationError(
                "Birth date cannot be in future."
            )

        return value



from rest_framework import serializers
from .models import Customer, Address
from django.contrib.auth import get_user_model

User = get_user_model()

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'province', 'city', 'street', 'postal_code']

class CustomerProfileSerializer(serializers.ModelSerializer):
    # دریافت نام و ایمیل از جدول User (به صورت فقط‌خواندنی)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    
    # نمایش لیست آدرس‌های کاربر
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'addresses']

        

```

### File: `apps\customers\signals.py`
```python
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import CustomUser
from .models import Customer

@receiver(post_save, sender=CustomUser)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(
            user=instance
        )



```

### File: `apps\customers\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\customers\urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerProfileView, AddressViewSet

router = DefaultRouter()
router.register('addresses', AddressViewSet, basename='addresses')

urlpatterns = [
    path('profile/', CustomerProfileView.as_view(), name='customer-profile'),
    path('', include(router.urls)),
]




```

### File: `apps\customers\views.py`
```python
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated


from .models import Customer, Address

from .serializers import CustomerProfileSerializer, AddressSerializer,CustomerSerializer



class CustomerMeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomerSerializer(request.user.customer)
        return Response(serializer.data)

    def patch(self, request):
        serializer = CustomerSerializer(request.user.customer,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class CustomerProfileView(RetrieveUpdateAPIView):
    """
    این ویو برای مشاهده و ویرایش پروفایل کاربری خود شخص است.
    """
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # این متد جادویی باعث می‌شود نیازی به ارسال ID در URL نباشد.
        # کاربر بر اساس توکنی که می‌فرستد، فقط پروفایل خودش را دریافت می‌کند.
        customer, created = Customer.objects.get_or_create(user=self.request.user)
        return customer

class AddressViewSet(ModelViewSet):
    """
    مدیریت آدرس‌های پستی کاربر
    """
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # هر کاربر فقط آدرس‌های خودش را می‌بیند
        return Address.objects.filter(customer__user=self.request.user)

    def perform_create(self, serializer):
        # در زمان ساخت آدرس جدید، فیلد customer به صورت خودکار با کاربر فعلی پر می‌شود
        customer, created = Customer.objects.get_or_create(user=self.request.user)
        serializer.save(customer=customer)





```

### File: `apps\customers\tests\__init__.py`
```python

```

### File: `apps\customers\tests\test_api.py`
```python
import datetime

from rest_framework.test import APITestCase
from rest_framework import status

from apps.accounts.models import CustomUser


class CustomerMeApiTest(APITestCase):

    def setUp(self):

        self.user = CustomUser.objects.create_user(
            username='api_user',
            email='api@test.com',
            password='12345678'
        )

    def test_authentication_required(self):

        response = self.client.get(
            '/api/customers/me/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_get_customer_profile(self):

        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.get(
            '/api/customers/me/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['user']['username'],
            self.user.username
        )

    def test_patch_customer_profile(self):

        self.client.force_authenticate(
            user=self.user
        )

        response = self.client.patch(
            '/api/customers/me/',
            {
                'phone_number': '09121234567'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['phone_number'],
            '09121234567'
        )
    
    def test_patch_invalid_phone_number(self):
        # ۱. احراز هویت کاربر
        self.client.force_authenticate(user=self.user)
        
        # ۲. ارسال درخواست ویرایش با شماره تلفن غلط (کمتر از 10 کاراکتر)
        response = self.client.patch(
            '/api/customers/me/',
            {
                'phone_number': '123' 
            },
            format='json'
        )

        # ۳. بررسی اینکه آیا سیستم خطای 400 داده است؟
        # (Bad Request)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        # ۴. بررسی اینکه آیا خطا دقیقاً مربوط به فیلد 
        # phone_number
        #  است؟
        self.assertIn('phone_number', response.data)


    def test_patch_future_birth_date(self):
        self.client.force_authenticate(user=self.user)
        
        # ۱. ساخت یک تاریخ در آینده (مثلاً 10 روز بعد از امروز)
        future_date = (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        
        # ۲. ارسال تاریخ آینده به سرور
        response = self.client.patch(
            '/api/customers/me/',
            {
                'birth_date': future_date
            },
            format='json'
        )

        # ۳. بررسی اینکه آیا سیستم خطای 400 داده است؟
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        
        # ۴. بررسی اینکه آیا خطا مربوط به فیلد 
        # birth_date
        #  است؟
        self.assertIn('birth_date', response.data)





```

### File: `apps\customers\tests\test_models.py`
```python
# apps/customers/tests/test_models.py
from django.test import TestCase

from apps.accounts.models import CustomUser
from apps.customers.models import Customer


class CustomerModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='sina',
            email='sina@test.com',
            password='12345678'
        )

    def test_customer_created_by_signal(self):
        self.assertTrue(
            Customer.objects.filter(
                user=self.user
            ).exists()
        )

    def test_customer_has_uuid(self):
        customer = self.user.customer

        self.assertIsNotNone(
            customer.uuid
        )

    def test_customer_str(self):
        customer = self.user.customer

        self.assertEqual(
            str(customer),
            self.user.username
        )
    

```

### File: `apps\customers\tests\test_serializers.py`
```python
from django.test import TestCase

from apps.accounts.models import CustomUser
from apps.customers.serializers import CustomerSerializer


class CustomerSerializerTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='serializer_user',
            email='serializer@test.com',
            password='12345678'
        )

        self.customer = self.user.customer

    def test_serializer_contains_expected_fields(self):

        serializer = CustomerSerializer(
            self.customer
        )

        data = serializer.data

        self.assertIn('id', data)
        self.assertIn('uuid', data)
        self.assertIn('phone_number', data)
        self.assertIn('birth_date', data)
        self.assertIn('user', data)

    def test_nested_user_serializer(self):

        serializer = CustomerSerializer(
            self.customer
        )

        user_data = serializer.data['user']

        self.assertEqual(
            user_data['username'],
            self.user.username
        )

        self.assertEqual(
            user_data['email'],
            self.user.email
        )


```

### File: `apps\customers\tests\test_signals.py`
```python
from django.test import TestCase

from apps.accounts.models import CustomUser
from apps.customers.models import Customer


class CustomerSignalTest(TestCase):

    def test_signal_creates_customer(self):

        user = CustomUser.objects.create_user(
            username='signal_user',
            email='signal@test.com',
            password='12345678'
        )

        self.assertTrue(
            Customer.objects.filter(
                user=user
            ).exists()
        )

    def test_only_one_customer_created(self):

        user = CustomUser.objects.create_user(
            username='signal_user2',
            email='signal2@test.com',
            password='12345678'
        )

        self.assertEqual(
            Customer.objects.filter(
                user=user
            ).count(),
            1
        )

    

```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-0.md`
```md
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
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-1.md`
```md
# ACRON Methodology Part-1

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

خروجی:

```bash
apps/
config/
core/
```

> 1- یک پروژه بدون pipenv بساز . 
تنها چیزی که داره یک فایل [README.md](http://README.md) داره و یک فایل LICENSE .
> 

> 2- داخل ترمینال محیط مجازی رو اینجوری بساز
> 
> 
> ```python
> pipenv install django
> ```
> 

> 3- داخل ترمینال محیط مجازی رو فعال کن
> 
> 
> ```python
> pipenv shell
> ```
> 

> 4- مسیر نگهداری محیط مجازی رو می تونی داخل ترمینال مشاهده کنی
> 
> 
> ```python
> pipenv --venv
> ```
> 

نتیجه به طور مثال شبیه این است: C:\Users\sina\.virtualenvs\acron-t_tS49nj

> 5- داخل ترمینال این رو بنویس تا ساختن پروژه رو شروع کنی
> 
> 
> ```python
> django-admin startproject config .
> ```
> 

این FOLDER یک APP نیست. نیازی نیست از دستور python [manage.py](http://manage.py) startapp core استفاده کنی.

```python
core/
├── permissions.py
├── pagination.py
├── mixins.py
├── exceptions.py
├── services.py
└── models.py (اختیاری)
```

در حالی که مدیریت کاربران یک Domain مستقل است:

```python
accounts/
├── models.py
├── admin.py
├── views.py
├── serializers.py
├── permissions.py
└── urls.py
```

ساختار پیشنهادی حرفه‌ای

```python
apps/
├── accounts/
├── customers/
├── products/
├── carts/
├── orders/
├── payments/
└── reviews/

core/
├── permissions.py
├── pagination.py
├── mixins.py
├── exceptions.py
└── services.py
```

چرا User را داخل core نگذاریم؟

فرض کن دو سال بعد:

```python
class CustomUser(AbstractUser):
    ...
```

بزرگ شود و این قابلیت‌ها را اضافه کنی:

- Login
- Register
- JWT
- OTP
- Email Verification
- Password Reset
- Profile
- Roles
- Permissions

اگر همه این‌ها داخل `core` باشند، `core` تبدیل به یک App شلوغ و نامفهوم می‌شود.

پروژه‌های حرفه‌ای معمولاً چه می‌کنند؟

خیلی از پروژه‌های بزرگ از یکی از این نام‌ها استفاده می‌کنند:

- accounts
- users
- authentication

رایج‌ترین گزینه: accounts است.
این ساختار از نظر Domain Design، توسعه‌پذیری و نگهداری، از قرار دادن User داخل `core` تمیزتر است.

---

---

Best Practice برای **Custom User**،  این است که App جداگانه‌ای به نام **accounts** (یا users) داشته باشی، نه **core**.   
دلیلش این است که `core` معمولاً برای چیزهای مشترک پروژه استفاده می‌شود.

ساخت CustomUser

- به جای User پیش‌فرض Django از CustomUser استفاده می‌کنیم.
- فعلاً فقط Email را Unique می‌کنیم.
- بعداً می‌توانیم Role، OTP، Avatar و ... را اضافه کنیم.

مدل ها:

- Customer

> 6- داخل ترمینال این رو بنویس تا اولین App رو بسازی
> 
> 
> ```python
> python manage.py startapp accounts
> ```
> 

> 7- داخل ترمینال این رو بنویس تا یک فولدر بسازی
> 
> 
> ```python
> mkdir apps
> ```
> 

> 8- داخل ترمینال این رو بنویس تا App که ساختی ( accounts ) بره داخل فولدر /apps
> 
> 
> ```python
> mv accounts apps/
> ```
> 

> 9- در پایان این مرحله ساختار باید شبیه این باشد:
> 
> 
> ```python
> acron/
> │
> ├── apps/
> │   └── accounts/
> │
> ├── config/
> │
> └── manage.py
> ```
> 

> 10- این قطعه کد رو داخل این مسیر اضافه کن:
> 
> 
> apps/accounts/models.py
> 
> ```python
> from django.contrib.auth.models import AbstractUser
> 
> from django.db import models
> 
> class CustomUser(AbstractUser):
>     email = models.EmailField(unique=True)
>     def __str__(self):
>         return self.username
> ```
> 

نکته بسیار مهم‌تر این تنظیم باید **قبل از اولین Migration پروژه** انجام شود.

کل فایل [settings.py](http://settings.py) رو میخوایم کم کمک منتقل کنیم داخل این فایل ها داخل این مسیر :

- acron/config/settings/__init__.py
- acron/config/settings/base.py
- acron/config/settings/development.py
- acron/config/settings/production.py

```python
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 6.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1r%tnk@im4n@uk5zx!q*i@wkr69darorwnglm%sa!_1ou=8#_w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

```

🎯 هدف جدا کردن تنظیمات به این ساختار:

```bash
config/settings/
├── base.py
├── development.py
└── production.py
```

🧠 قانون کلی تقسیم‌بندی

| نوع تنظیم | می‌رود به |
| --- | --- |
| مشترک بین همه محیط‌ها | base.py |
| مخصوص توسعه (local) | development.py |
| مخصوص production | production.py |

> 11- تبدیل settings.py
> 
> 
> از: config/settings.py
> 
> به 
> 
> ```python
> config/settings/
> ├── __init__.py
> ├── base.py
> ├── development.py
> └── production.py
> ```
> 

🧩 حالا خط به خط فایل را ، کم کم منتقل میکنیم. اگر قسمتی را فراموش کنیم قطعا بعدا مشاهده خواهد شد با ارورها.

---

BASE_DIR 

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
```

📍 کجا برود؟

config/settings/base.py

چرا؟

چون همه محیط‌ها به path پروژه نیاز دارند.

> 12- آنگاه قطعه کد زیر را داخل config/settings/base.py بگذار
> 
> 
> ```python
> from pathlib import Path
> BASE_DIR = Path(__file__).resolve().parent.parent.parent
> AUTH_USER_MODEL = "accounts.CustomUser"
> ```
> 

AUTH_USER_MODEL = "accounts.CustomUser” کارهای زیر را به عهده دارد:

- این خط به Django می‌گوید User اصلی پروژه چیست.
- باید قبل از اولین Migration تنظیم شود.
- بعد از Migration تغییر آن بسیار سخت می‌شود.

چرا در [base.py](http://base.py/)؟ چون این تنظیم: AUTH_USER_MODEL  در همه محیط‌ها یکسان است:

- Development
- Production
- Test

و وابسته به محیط اجرا نیست.

13- فایل قدیمی: config/settings.py را حذف کن. یا اینکه اسمش رو تغییر بده و فرمت رو txt کن تا بعدا اگه نیاز داشتی در دسترس باشه

SECRET_KEY کجا برود ؟

```python
SECRET_KEY = '...'
```

📍 بهتر است برود:  config/settings/base.py 

بعداً باید برود در:

- environment variable
- یا .env

ولی فعلاً:  config/settings/base.py  کفایت میکند.

> 13 - انتقال SECRET_KEY از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py:
> 
> ```python
> # SECURITY WARNING: keep the secret key used in production secret!
> SECRET_KEY = 'django-insecure-1r%tnk@im4n@uk5zx!q*i@wkr69darorwnglm%sa!_1ou=8#_w'
> ```
> 

DEBUG کجا برود؟ به دو آدرس می رود با این تفاوت که True برای development.py است تا خطاها را نمایش بدهد. False برای [production.py](http://production.py) است تا خطاها را نمایش ندهد

config/settings/development.py

```python
DEBUG = True
```

ALLOWED_HOSTS کجا برود؟ 

```python
ALLOWED_HOSTS = []
```

به این دو مورد منتقل می شود: config/settings/base.py

```python
config/settings/base.py
```

و override در production:

```python
ALLOWED_HOSTS = ['acronproject.com', 'www.acronproject.com', 'acronproject.com', 'www.acronproject.com', 'localhost', '127.0.0.1']
```

INSTALLED_APPS به کجا منتقل میشود ؟ config/settings/base.py  چرا ؟ چون در همه محیط ها یکی هست.

> 14 - انتقال INSTALLED_APPS  از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> # Application definition
> 
> INSTALLED_APPS = [
>     'django.contrib.admin',
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
> ]
> ```
> 

MIDDLEWARE کجا برود ؟  config/settings/base.py چرا ؟ چون در تمام محیط ها یکی هستند.

> 15 - انتقال MIDDLEWARE  از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> MIDDLEWARE = [
>     'django.middleware.security.SecurityMiddleware',
>     'django.contrib.sessions.middleware.SessionMiddleware',
>     'django.middleware.common.CommonMiddleware',
>     'django.middleware.csrf.CsrfViewMiddleware',
>     'django.contrib.auth.middleware.AuthenticationMiddleware',
>     'django.contrib.messages.middleware.MessageMiddleware',
>     'django.middleware.clickjacking.XFrameOptionsMiddleware',
> ]
> ```
> 

ROOT_URLCONF کجا منتقل بشود؟  config/settings/base.py

> 16 - انتقال ROOT_URLCONF  از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> ROOT_URLCONF = 'config.urls'
> ```
> 

TEMPLATES به کجا منتقل بشود ؟  config/settings/base.py

> 17 - انتقال ROOT_URLCONF  از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> TEMPLATES = [
>     {
>         'BACKEND': 'django.template.backends.django.DjangoTemplates',
>         'DIRS': [],
>         'APP_DIRS': True,
>         'OPTIONS': {
>             'context_processors': [
>                 'django.template.context_processors.request',
>                 'django.contrib.auth.context_processors.auth',
>                 'django.contrib.messages.context_processors.messages',
>             ],
>         },
>     },
> ]
> ```
> 

WSGI_APPLICATION به کجا منتقل می شود؟  config/settings/base.py

> 18 - انتقال WSGI_APPLICATION  از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> WSGI_APPLICATION = 'config.wsgi.application'
> ```
> 

AUTH_PASSWORD_VALIDATORS به کجا منتقل می شود؟  config/settings/base.py

> 19 - انتقال AUTH_PASSWORD_VALIDATORS  از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> # Password validation
> # https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators
> 
> AUTH_PASSWORD_VALIDATORS = [
>     {
>         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
>     },
>     {
>         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
>     },
>     {
>         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
>     },
>     {
>         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
>     },
> ]
> ```
> 

LANGUAGE / TIMEZONE به کجا منتقل می شود؟  config/settings/base.py

> 20 - انتقال LANGUAGE / TIMEZONE از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> LANGUAGE_CODE = 'en-us'
> TIME_ZONE = 'UTC'
> USE_I18N = True
> USE_TZ = True
> ```
> 

STATIC_URL به کجا منتقل می شود؟  config/settings/base.py

> 21 - انتقال STATIC_URL  از [settings.py](http://settings.py) به این آدرس:
> 
> 
> config/settings/base.py
> 
> ```python
> STATIC_URL = 'static/'
> ```
> 

🧠 جمع‌بندی نهایی

📦 base.py (مشترک همه محیط‌ها)

تمام این‌ها:

- BASE_DIR
- SECRET_KEY (فعلاً)
- ALLOWED_HOSTS (پایه)
- INSTALLED_APPS
- MIDDLEWARE
- ROOT_URLCONF
- TEMPLATES
- WSGI_APPLICATION
- DATABASES (فعلاً sqlite یا mysql اولیه)
- AUTH_PASSWORD_VALIDATORS
- LANGUAGE_CODE
- TIME_ZONE
- USE_I18N
- USE_TZ
- STATIC_URL

🧪 [development.py](http://development.py/)

- DEBUG = True
- DATABASES (اگر جدا خواستی)
- CORS settings (بعداً)
- logging level (debug)

🚀 [production.py](http://production.py/)

- DEBUG = False
- ALLOWED_HOSTS
- DATABASES (prod db)
- security settings
- logging

چه چیزهایی را با startapp بسازیم؟ 

✅ ابتدا `CustomUser` و `DATABASES` را تنظیم کن.

✅ سپس `makemigrations` و `migrate` را اجرا کن.

> 22-  این‌ها را با `startapp` بساز:
> 
> 
> ```bash
> python manage.py startapp customers
> python manage.py startapp products
> python manage.py startapp carts
> python manage.py startapp orders
> python manage.py startapp payments
> python manage.py startapp reviews
> python manage.py startapp notifications
> ```
> 

> 23- سپس همه را به داخل پوشه: apps/ منتقل کن.
> 
> 
> ```bash
> mv customers apps/
> mv products apps/
> mv carts apps/
> mv orders apps/
> mv payments apps/
> mv reviews apps/
> mv notifications apps/
> ```
> 

> 24- سپس همه را به داخل INSTALLED_APPS اضافه کن:
> 
> 
> config/settings/base.py
> 
> ```python
> INSTALLED_APPS = [
> 		...
> 		...
> 		
>     # CREATE by me
>     'apps.accounts',
>     # a فعلا این موارد رو به حالت کامنت در بیار
>     # 'apps.cart',
>     # 'apps.customers',
>     # 'apps.notifications',
>     # 'apps.orders',
>     # 'apps.payments',
>     # 'apps.products',
>     # 'apps.reviews',
> ]
> ```
> 

> 25- همه APP ها را بر اساس منطق تغییر بده:
> 

اصلاح AppConfig

- چون App را داخل `apps/` قرار داده‌ایم، Django باید مسیر کامل App را بشناسد.
- مقدار `name` باید مسیر پایتونی کامل باشد.
- در غیر این صورت Migration و Importها به مشکل می‌خورند.

مسیر فایل: apps/accounts/apps.py

```python
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'

```

به کد زیر تغییر بده

```python
from django.apps import AppConfig

class AccountsConfig(AppConfig):
		default_auto_field = 'django.db.models.BigAutoField'
		name = 'apps.accounts'
```

برای `core` من پیشنهاد می‌کنم **از `python manage.py startapp core` استفاده نکنی**.
دلیلش این است که `core` در معماری‌ای که داریم طراحی می‌کنیم، یک **Domain App** نیست.
مثلاً این‌ها Domain هستند:

- accounts
- customers
- products
- orders
- payments
- carts

اما `core` قرار نیست:

- Model داشته باشد
- Migration داشته باشد
- Admin داشته باشد
- URL داشته باشد

بلکه فقط کدهای مشترک پروژه را نگهداری می‌کند. بنابراین بهتر است به شکل یک Package ساده ساخته شود:

```python
acron/
│
├── core/
│   ├── __init__.py
│   ├── permissions.py
│   ├── pagination.py
│   ├── exceptions.py
│   ├── mixins.py
│   └── services.py
│
├── apps/
├── config/
└── manage.py
```

> 26- این ها رو تکی تکی داخل ترمینال بنویس: (در ویندوز هم فایل‌ها را دستی بساز.)
> 
> 
> ```bash
> mkdir core
> touch core/__init__.py
> touch core/permissions.py
> touch core/pagination.py
> touch core/exceptions.py
> touch core/mixins.py
> touch core/services.py
> ```
> 

> 27- محتوای اولیه config/settings/**init**.py
> 
> 
> ```python
> from .development import *
> ```
> 

📌 یعنی چه؟

یعنی:

هر چیزی که در development.py هست، به عنوان تنظیمات اصلی پروژه لود شود

🚀 بعداً در production چه می‌کنیم؟

در سرور واقعی تغییر می‌دهی به:

```python
# config/settings/__init__.py

from .production import *
```

---

> 28- محتوای اولیه config/settings/development.py
> 
> 
> ```python
> from .base import *
> ```
> 

---

> 29- محتوای اولیه config/settings/production.py
> 
> 
> ```python
> from .base import *
> ```
> 

---

🚀 نتیجه نهایی

✔ الان MySQL کاملاً درست است

✔ فقط جای درستش مهم است (development.py)

✔ base.py نباید وابسته به دیتابیس شود

> 30- تنظیمات دیتابیس در فایل  config/settings/base.py  
خالی بماند
ترجیحال فعلا حالت کامنت باشد
> 
> 
> ```python
> # config/settings/base.py
> 
> # DATABASES = {}
> ```
> 

⚠️ اشتباه رایج

❌ این کار بد است: داخل [base.py](http://base.py/)

```python
DATABASES = {
    'ENGINE': 'mysql',
}
```

چون:

- پروژه قفل به MySQL می‌شود
- تست سخت می‌شود
- migration بین محیط‌ها سخت می‌شود

---

---

> 🧪 [development.py](http://development.py/) (MySQL فعلی تو اینجاست)
> 

> 31- داخل این مسیر کد زیر رو اضافه کن:
> 
> 
> config/settings/development.py
> 
> ```python
> # ....
> 
> DATABASES = {
>     'default': {
>         'ENGINE': 'django.db.backends.mysql',
>         'NAME': 'acron',
>         'HOST': 'localhost',
>         'USER': 'root',
>         'PASSWORD': '1234',
>         'PORT': '3306',
>     }
> }
> ```
> 

🚀 production.py (بعداً)

مثلاً PostgreSQL:

```python
# config/settings/production.py

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'acron',
        'HOST': 'db',
        'USER': 'acron_user',
        'PASSWORD': 'strong_password',
        'PORT': '5432',
    }
}
```

🧠 یک نکته خیلی مهم (سطح حرفه‌ای)

اگر واقعاً بخواهی پروژه‌ات scalable باشد:

بعداً بهتر است DATABASES را ببری روی:

```python
os.environ
```

یا

```python
.env
```

مثل زیر ولی فعلا لازم نیست:

```python
DATABASE_URL=mysql://root:1234@localhost:3306/acron
```

> 32- نصب Driver مربوط به MySQL
> 
> 
> ```bash
> pipenv install mysqlclient
> ```
> 

> 33- دیتابیس را در MySQL بساز . قبل از اجرای Migration داخل MySQL Workbench:
> 
> 
> ```bash
> CREATE DATABASE acron
> CHARACTER SET utf8mb4
> COLLATE utf8mb4_unicode_ci;
> ```
> 

این‌ها هنگام ساخت دیتابیس مشخص می‌کنند که **داده‌های متنی چگونه ذخیره و مقایسه شوند:**

CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci

CHARACTER SET utf8mb4
این خط مشخص می‌کند که دیتابیس از چه Encoding برای ذخیره متن استفاده کند.

**چرا utf8mb4؟**

زیرا از تقریباً تمام کاراکترهای یونیکد پشتیبانی می‌کند:

- فارسی
- عربی
- انگلیسی
- آلمانی
- چینی
- ایموجی 😀

اگر utf8 استفاده کنیم چه می‌شود؟

> در MySQL، نام `utf8` کمی گمراه‌کننده است. 
در واقع: `utf8` فقط تا 3 بایت را پشتیبانی می‌کند. 
اما: utf8mb4  تا 4 بایت را پشتیبانی می‌کند. 
بنابراین بعضی ایموجی‌ها در `utf8` ذخیره نمی‌شوند. 
مثلاً: 😀 ممکن است خطا بدهد.  
به همین دلیل سال‌هاست توصیه می‌شود: utf8mb4 استفاده شود.
> 

COLLATE utf8mb4_unicode_ci  این قسمت نحوه مقایسه و مرتب‌سازی متن را تعیین می‌کند. 
فرض کن در دیتابیس داریم: 

```bash
Ali
ALI
ali
```

پس سؤال این است:

```bash
WHERE username = 'ali'
```

آیا هر سه را پیدا کند یا نه؟  این رفتار توسط Collation تعیین می‌شود.

ci چیست؟  ci = case insensitive  

یعنی: 

```bash
Ali
ALI
ali
```

همه برابر در نظر گرفته می‌شوند.

cs چیست؟  cs = case sensitive 

در این حالت:

```bash
Ali ≠ ali
```

> unicode چیست؟  `utf8mb4_unicode_ci` 
از قوانین استاندارد Unicode برای مرتب‌سازی استفاده می‌کند. 
مثلاً برای زبان‌های مختلف نتایج بهتری نسبت به Collationهای قدیمی MySQL دارد.
> 

مزایا:

✅ پشتیبانی کامل از فارسی

✅ پشتیبانی از ایموجی

✅ سازگاری عالی با Django

✅ جلوگیری از مشکلات Encoding در آینده

به همین دلیل تقریباً در تمام پروژه‌های جدید Django + MySQL از `utf8mb4` استفاده می‌شود.

> 34- تست اتصال قبل از Migration این دستور را بزن:
> 
> 
> ```bash
> python manage.py check
> ```
> 

ساخت Migration

> 35- ساخت فایل مایگریشن
> 
> 
> ```bash
> python manage.py makemigrations accounts
> ```
> 

خروجی باید چیزی شبیه به این باشد:

```bash
$ python manage.py makemigrations accounts
Migrations for 'accounts':
  apps\accounts\migrations\0001_initial.py
    + Create model CustomUser
```

> 36- مایگریت کردن در دیتابیس
> 
> 
> ```bash
>  python manage.py migrate
> ```
> 

خروجی باید چیزی شبیه به این باشد:

```bash
Operations to perform:
  Apply all migrations: accounts, admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying accounts.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying sessions.0001_initial... OK
```

> 37- یک اکانت superuser بساز . داخل ترمینال این رو بنویس
> 
> 
> ```bash
>  python manage.py createsuperuser
> ```
> 

خروجی باید یک چیزی شبیه به این باشد: مرحله به مرحله که می سازی باید Enter بزنی و بری خط بعدیش

```bash
Username: esme_delkhahet
Email: sina@sina.com
Password: password_delkhahet_tarjihan_tooolani___!!!
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

> 38- سرور رو داخل ترمینال فعال کن با این کامند
> 
> 
> ```bash
>  python manage.py runserver
> ```
> 

خروجی باید یک چیزی شبیه به این باشد: دکمه  Ctrl رو نگهدار و بزن روی اون لینک باید خودکار بره داخل مرورگر پیش فرضیی که برای سیستم عامل در نظر گرفتی این صفحه رو ببینی

```bash
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 24, 2026 - 02:09:34
Django version 6.0.6, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
```

![image.png](image.png)

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: [https://docs.djangoproject.com/en/6.0/howto/deployment/](https://docs.djangoproject.com/en/6.0/howto/deployment/)

این هشدار برای زمانی اهمیت دارد که میخوای پروژه رو دیپلوی کنی. الان نگرانش نباش.

What is WSGI?

WSGI is the Web Server Gateway Interface. 
It is a specification that describes how a web server communicates with web applications, and how
web applications can be chained together to process one request.

What is ASGI?
ASGI (*Asynchronous Server Gateway Interface*) is a spiritual successor to
WSGI, intended to provide a standard interface between async-capable Python
web servers, frameworks, and applications.
WSGI is a Python standard described in detail in [**PEP 3333**](https://peps.python.org/pep-3333/).

> 39- در ریشه اصلی سایت فایل .gitignore رو بساز
> 
> 
> ```
> .gitignore
> ```
> 
> این مورد رو بهش اضافه کند:
> 
> ```python
> vscode/settings.json
> ```
> 

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

یعنی:

```bash
Infrastructure
│
├── Authentication
├── Authorization
├── DRF
├── JWT
├── Pagination
└── Permissions
```

یا Django REST Framework هسته APIهای پروژه ما خواهد بود.

به جای:

```
HttpResponse()
```

از:

```
APIView
Serializer
ViewSet
Router
```

استفاده خواهیم کرد.

Authentication خودش یک فاز مستقل نیست.

زیرمجموعه Infrastructure است.

چرا Product را فعلاً نمی‌سازیم؟

چون Product API خواهد داشت.

مثلاً:

```
GET/api/products/
POST/api/products/
```

و برای این‌ها نیاز داریم:

```
Authentication
Permissions
Pagination
```

که هنوز وجود ندارند.

> 1- نصب DRF 
Django REST Framework
> 
> 
> ```bash
> pipenv install djangorestframework
> ```
> 

> 2- نصب JWT
JSON Web Token
djangorestframework-simplejwt
> 
> 
> ```bash
> pipenv install djangorestframework-simplejwt
> ```
> 

> 3- ثبت در INSTALLED_APPS
> 
> 
> ```python
> # config/settings/base.py
> INSTALLED_APPS = [
>     ...
> 
>     'rest_framework',
> 
>     'apps.accounts',
> ]
> ```
> 

> 4- تنظیم اولیه DRF
> 
> 
> ```python
> # config/settings/base.py
> REST_FRAMEWORK = {
>     'DEFAULT_AUTHENTICATION_CLASSES': (
>         'rest_framework_simplejwt.authentication.JWTAuthentication',
>     ),
> }
> ```
> 

> 5- تنظیم JWT
> 
> 
> ```python
> # config/settings/base.py
> from datetime import timedelta
> 
> SIMPLE_JWT = {
>     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
>     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
> }
> ```
> 

<aside>
📢

**ساخت API App**

</aside>

تا اینجا زیرساخت API آماده شده.

حالا می‌خواهیم APIهای مربوط به Authentication را بسازیم.

> 6- دستور زیر را داخل ترمینال بزن
> 
> 
> ```bash
> python manage.py startapp api
> ```
> 

> 7- api رو به فولدر apps منتقل کن
> 
> 
> ```bash
> mv api apps/
> ```
> 

```bash
apps/
│
├── accounts/
├── api/
```

> 8- اصلاح AppConfig
> 
> 
> ```python
> # apps/api/apps.py
> from django.apps import AppConfig
> 
> class ApiConfig(AppConfig):
>     default_auto_field = 'django.db.models.BigAutoField'
>     name = 'apps.api'
> ```
> 

> 9- ثبت App
> 
> 
> ```python
> # config/settings/base.py
> INSTALLED_APPS = [
>     ...
>     'apps.api',
> ]
> ```
> 

<aside>
📢

**ساخت urls.py برای API**

</aside>

توضیح

از همین ابتدا همه APIها را زیر مسیر می بریم

```
/api/
```

> 10- فایل [urls.py](http://urls.py/) رو داخل مسیر زیر بساز
> 
> 
> ```python
> # apps/api/urls.py
> ```
> 

> 11- داخل فایل [urls.py](http://urls.py/) این کد رو اضافه کن
> 
> 
> ```python
> # apps/api/urls.py
> from django.urls import path
> 
> urlpatterns = []
> ```
> 

> 12- اتصال API به پروژه
> 
> 
> ```python
> # config/urls.py
> from django.contrib import admin
> from django.urls import path, include
> 
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     path('api/', include('apps.api.urls')),
> ]
> ```
> 

> **✔ Django
✔ MySQL
✔ CustomUser
✔ DRF
✔ JWT
✔ API Root**
> 

> **پس از اتمام مرحله 12 خواهیم داشت:**
> 

> **نتیجه تا اینجا**
> 

یک نکته ظریف

وقتی می‌نویسی:

```
path('api/',include('apps.api.urls'))
```

در واقع Django انتظار دارد چیزی مثل این وجود داشته باشد:

```
api/login/
api/products/
api/customers/
api/token/
```

اما تو فعلاً:

```
urlpatterns= []
```

داری.

پس طبیعی است که: داخل این مسیر [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) ارور 404 بگیری. نگران نباش.

```
Page not found (404)
```

چطور تست کنیم که درست کار می‌کند؟

> 13- موقتاً این URL را اضافه کن
> 
> 
> ```python
> # apps/api/urls.py
> from django.http import HttpResponse
> from django.urls import path
> 
> def api_home(request):
>     return HttpResponse("API Root")
> 
> urlpatterns = [
>     path('', api_home),
> ]
> ```
> 

> 14- حالا برو:
> 
> 
> ```
> http://127.0.0.1:8000/api/
> ```
> 

باید ببینی:

```
API Root
```

![image.png](ecfd67bf-fb48-4b42-a337-4ea47f25183e.png)

حالا برویم سراغ JWT

این اولین API واقعی پروژه خواهد بود. 

JWT چیست؟

فرض کن کاربر Login می‌کند.

روش قدیمی Django: کاربر تازه بعد لاگین کردن به سشن دسترسی خواهد داشت.

ولی خیلی از کاربرها تمایلی ندارند که اول وارد بشوند سپس بتوانند سبد خریدشون رو پر کنند.

ترجیح می دهند تا آخرین لحظه راه فرار داشته باشند از خرید.

```
Login
↓
Session
↓
Cookie
↓
Server State
```

روش JWT:

```
Login
↓
Access Token
↓
Refresh Token
↓
Stateless Authentication
```

Access Token چیست؟

توکن کوتاه‌عمر.

مثلاً:

```
60 دقیقه
```

اعتبار دارد.

مثال:

```
eyJhbGciOiJIUzI1NiIsInR5cCI...
```

کاربر این را در Header می‌فرستد.

Refresh Token چیست؟

اگر Access Token منقضی شد:

```
Access Expired
```

به جای Login مجدد:

```
Refresh Token
↓
New Access Token
```

می‌گیریم.

چرا دو توکن داریم؟

اگر فقط یک توکن داشتیم:

```
Token Leak
↓
Attacker Forever
```

اما الان:

```
Access = کوتاه عمر
Refresh = بلند عمر
```

امن‌تر است.

> 15- حالا داخل مسیر زیر کد نوشته شده رو جایگزین کن:
> 
> 
> ```python
> # apps/api/urls.py
> from django.urls import path
> from django.http import HttpResponse
> 
> from rest_framework_simplejwt.views import (
>     TokenObtainPairView,
>     TokenRefreshView,
> )
> 
> def api_root(request):
>     return HttpResponse("API is working 🚀")
> 
> urlpatterns = [
>     path('', api_root),
> 
>     # 🔐 JWT endpoints
>     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
>     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
> ]
> ```
> 

حالا چه URLهایی داریم؟

دریافت توکن

```
POST
/api/token/
```

رفرش توکن

```
POST
/api/token/refresh/
```

> 16- حالا داخل مسیر برو و با super user که ساخته بودی پایین صفحه وارد بشو
> 
> 
> ```
> http://127.0.0.1:8000/api/token/
> ```
> 

باید این خروجی رو داخل مرورگر بگیرید:

```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept{
"refresh":"eyJhb........wrZQM",
"access":"eyJhbG........r2fG4"}
```

اولین Protected API + IsAuthenticated + request.user flow

هدف این مرحله:

✔ ساخت یک API که فقط کاربر لاگین‌شده ببینه

✔ فهم دقیق اینکه `request.user` از کجا میاد

✔ دیدن جریان واقعی JWT در DRF

🧠 اول مفهوم مهم

وقتی این کار رو می‌کنی:

```
Authorization: Bearer <access_token>
```

چرخه کامل JWT-JSON Web Token

> Login
  ↓
POST /api/token/
  ↓
access + refresh
  ↓
GET /api/me/
Authorization: Bearer access
  ↓
request.user
  ↓
Response
> 

وقتی Access منقضی شد:

> 
> 
> 
> POST /api/token/refresh/
> ↓
> new access
> ↓
> GET /api/me/
> 

DRF این کار رو انجام می‌ده:

1. توکن را از Header می‌خواند
2. توکن را decode می‌کند
3. user_id داخل آن را پیدا می‌کند
4. از دیتابیس user را می‌کشد
5. می‌گذارد داخل:

```
request.user
```

<aside>
📢

**ساخت اولین Protected API**

</aside>

> 17-0 فایلviews.py را در مسیر  apps/api/  بساز.
> 

> 17-1- در مسیر زیر فایل [views.py](http://views.py) رو بساز
> 
> 
> ```python
> # apps/api/views.py
> 
> from rest_framework.decorators import api_view, permission_classes
> from rest_framework.permissions import IsAuthenticated
> from rest_framework.response import Response
> 
> # 🔐 API محافظت‌شده
> @api_view(['GET'])
> @permission_classes([IsAuthenticated])
> def me(request):
>     return Response({
>         "id": request.user.id,
>         "username": request.user.username,
>         "email": request.user.email,
>     })
> ```
> 

<aside>
📢

اتصال به URL

</aside>

> 18- در مسیر زیر فایل urls.py رو بساز
> 
> 
> ```python
> # apps/api/urls.py
> 
> from django.urls import path
> from django.http import HttpResponse
> 
> from rest_framework_simplejwt.views import (
>     TokenObtainPairView,
>     TokenRefreshView,
> )
> 
> from .views import me
> 
> def api_root(request):
>     return HttpResponse("API is working 🚀")
> 
> urlpatterns = [
>     path('', api_root),
> 
>     # JWT
>     path('token/', TokenObtainPairView.as_view()),
>     path('token/refresh/', TokenRefreshView.as_view()),
> 
>     # 🔐 protected route
>     path('me/', me),
> ]
> ```
> 

<aside>
📢

تست با Postman

</aside>

> مطمئن شو سرور Django اجرا شده
> 
> 1. مطمئن شو SuperUser داری
> 2. باز کردن Postman
> 3. روی new کلیک کن 
> 4. روی HTTP کلیک کن
> 5. متد method POST را انتخاب کن
> 6. مسیر url رو روی [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/) قرار بده.
> 7. روی تب body برو 
> 8. روی raw کلیک کن
> 9. از منوی سمت راست JSON رو انتخاب کن
> 10. اطلاعات کاربری رو وارد کن ( همون super user )
> 
> ```python
> {
>     "username": "admin",
>     "password": "1234"
> }
> ```
> 
> 1. روی send بزن -خروجی باید مشابه زیر باشه:
> 
> ```python
> {
>     "refresh": "eyJhbGc.....",
>     "access": "eyJhbGc....."
> }
> ```
> 
> این دو مقدار چیستند؟
> 
> refresh
> 
> مثلاً:
> 
> ```
> eyJhbGciOiJIUzI1NiIsInR5cCI...
> ```
> 
> این توکن 7 روز اعتبار دارد.
> 
> access
> 
> مثلاً:
> 
> ```
> eyJhbGciOiJIUzI1NiIsInR5cCI...
> ```
> 
> این توکن 60 دقیقه اعتبار دارد.
> 
> 1. فقط مقدار access را کپی کن.
> 2. یک Request جدید باز کن.
> 3. متدش method روی حالت GET باشد.
> 4. مسیرش `http://127.0.0.1:8000/api/me/`
> 
> تنظیم Authorization دو روش داره 
> 
> 1. روی تب Authorization بزن
> 2. سپس Type رو روی حالت Bearer Token تنظیم کن.
> 3. در قسمت Token مقدار access token را که کپی کرده بودی جایگذاری کن.
>  Paste from Clipboard
> 4. روی دکمه send بزن باید نتیجه موفق زیر را دریافت کنی:
> 
> ```python
> {
>     "id": 1,
>     "username": "admin",
>     "email": "admin@test.com"
> }
> ```
> 

پشت صحنه چه اتفاقی افتاد؟

Postman این Header را ساخت و برای Django فرستاد.

```
Authorization: Bearer eyJhbGcxxxxxxxxxxxx
```

سپس DRF: را اجرا کرد. و توکن را Decode کرد.

```
JWTAuthentication
```

از داخل توکن: user_id  را استخراج کرد.  کاربر را از دیتابیس پیدا کرد. و مقدار request.user را ساخت. 

بنابراین این کد:

```
request.user.username
```

مقدار admin را برگرداند.

```
admin
```

<aside>
📢

تست خطا 

</aside>

> 20. حالا Authorization را حذف کن. مجددا send کن. نتیجه باید شبیه زیر باشد:
> 

```python
{
    "detail": "Authentication credentials were not provided."
}
```

زمانی که منقضی شده باشد ، نتیجه شبیه زیر خواهد بود:

```python
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is expired"
        }
    ]
}
```

> 21. یک کاراکتر از توکن را تغییر بده. مجددا send کن. نتیجه باید شبیه زیر باشد:
> 

```python
{
    "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Token is invalid"
        }
    ]
}
```

> 22. تست Refresh Token  :  یک Request جدید بساز.  متدش Method رو روی POST  تنظیم کن.
> 
> 
> ```python
> [http://127.0.0.1:8000/api/token/refresh/](http://127.0.0.1:8000/api/token/refresh/)
> ```
> 
> بدنه body کد زیر باشد: سپس دکمه send رو بزن
> 
> ```python
> {
>     "refresh": "توکن refresh اینجا"
> }
> ```
> 

> 19- این تنظیمات رو بررسی کن بزار داخل آدرس زیر: Base DRF Settings
> 
> 
> ```python
> # acron/config/settings/base.py
> 
> REST_FRAMEWORK = {
>     "DEFAULT_AUTHENTICATION_CLASSES": (
>         "rest_framework_simplejwt.authentication.JWTAuthentication",
>     ),
> 
>     "DEFAULT_PERMISSION_CLASSES": (
>         "rest_framework.permissions.IsAuthenticated",
>     ),
> 
>     "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
>     "PAGE_SIZE": 10,
> }
> ```
> 

مزیت:

دیگر لازم نیست روی تک‌تک Viewها بنویسی:

```
permission_classes= [IsAuthenticated]
```

**Authentication Flow کامل**

```python
Request
 ↓
Authentication
 ↓
request.user
 ↓
Permission
 ↓
View
 ↓
Serializer
 ↓
Response
```

Permission Classes

> Authentication به این سؤال جواب می‌دهد:
> 
> 
> این شخص کیست؟
> 
> Permission به این سؤال جواب می‌دهد:
> 
> این شخص چه کاری می‌تواند انجام دهد؟
> 
> مثال:
> 
> admin
> 
> احراز هویت شده است.
> 
> اما آیا می‌تواند:
> 
> DELETE /products/1/
> 
> را انجام دهد؟
> 
> این را Permission تعیین می‌کند.
> 

معماری DRF وقتی request  می آید:

```python
Request
   ↓
Authentication
   ↓
Permission
   ↓
View
   ↓
Serializer
   ↓
Response
```

Permission های آماده DRF

> AllowAny
> 
> 
> اجازه به همه
> 
> ```python
> fromrest_framework.permissionsimportAllowAny
> ```
> 
> مثال:
> 
> ```python
> @permission_classes([AllowAny])
> ```
> 
> حتی اگر Login نکرده باشد.
> 

> IsAuthenticated
> 
> 
> فقط کاربر Login شده
> 
> ```
> fromrest_framework.permissionsimportIsAuthenticated
> ```
> 
> مثال:
> 
> ```
> @permission_classes([IsAuthenticated])
> ```
> 

> IsAdminUser
> 
> 
> فقط staff
> 
> پشت صحنه:
> 
> ```
> request.user.is_staff
> ```
> 
> را چک می‌کند.
> 
> مثال:
> 
> ```
> @permission_classes([IsAdminUser])
> ```
> 

یک تست برای  permission:

این view فرضی هست نیازی نیست به طور دائمی استفاده بشه به همین خاطر داخل شماره گذاری آورده نشده:

```
# apps/api/views.py

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret_api(request):
    return Response({
        "message": "secret"
    })
```

```python
# apps/api/urls.py

from . import views
urlpatterns = [
		....
    path('secret/', views.secret_api),

]
```

بدون Token:

```
{
    "detail":"Authentication credentials were not provided."
}
```

با Access Token:

```
{
    "message":"secret"
}
```

<aside>
📢

Permission سفارشی

فقط صاحب پروفایل اجازه ویرایش داشته باشد.

</aside>

> 20- فایل [permissions.py](http://permissions.py) رو در مسیر apps/api/permissions.py بساز
> 

> 21- داخل فایل [permissions.py](http://permissions.py) این کد رو اضافه کن:
> 
> 
> ```python
> # apps/api/permissions.py
> 
> from rest_framework.permissions import BasePermission
> 
> class IsOwner(BasePermission):
> 
>     def has_object_permission(
>         self,
>         request,
>         view,
>         obj
>     ):
>         return obj.user == request.user
> ```
> 

> obj چیست؟
> 
> 
> فرض کن URL: این مسیر GET /api/customers/1/ باشد.
> 
> ویو می‌رود Customer شماره 1 را پیدا می‌کند:
> 
> ```
> customer=Customer.objects.get(id=1)
> ```
> 
> DRF آن را به Permission می‌دهد:
> 
> ```
> obj=customer
> ```
> 
> پس اینجا:
> 
> ```
> obj.user
> ```
> 
> یعنی:
> 
> ```
> customer.user
> ```
> 
> مثلاً:
> 
> ```
> obj.user
> ```
> 
> برابر است با:
> 
> ```
> admin
> ```
> 
> و:
> 
> ```
> request.user
> ```
> 
> هم از JWT آمده.
> 
> مثلاً:
> 
> ```
> admin
> ```
> 
> پس:
> 
> ```
> admin==admin
> ```
> 
> نتیجه: و اجازه صادر می‌شود.
> 
> ```
> True
> ```
> 
> اما فعلاً از آن استفاده نکن.
> 
> هدف فعلی فقط این است که بفهمی:
> 
> ```
> obj
> ```
> 
> همان آبجکتی است که View از دیتابیس گرفته و می‌خواهد روی آن عملیات انجام دهد.
> 
> وقتی در فاز 3 به Customer برسیم، آن موقع این Permission را روی یک مدل واقعی استفاده می‌کنیم.
> 

حالا کجا permission_classes را می‌نویسیم؟

بستگی به نوع View دارد.

> حالت اول: Function Based View  - اینجا بالای تابع می‌آید.
> 
> 
> ```python
> fromrest_framework.decoratorsimport (
> api_view,
> permission_classes
> )
> 
> @api_view(['GET'])
> @permission_classes([IsAuthenticated])
> defme(request):
>     ...
> ```
> 

> حالت دوم: APIView  — اینجا داخل کلاس نوشته می‌شود.
> 
> 
> ```python
> from rest_framework.views import APIView
> 
> class CustomerDetailView(APIView):
> 
>     permission_classes = [
>         IsAuthenticated
>     ]
> 
>     def get(self, request, pk):
>         ...
> ```
> 

> حالت سوم: GenericAPIView
> 
> 
> ```python
> class CustomerDetailView(RetrieveAPIView):
> 
>     queryset = Customer.objects.all()
> 
>     serializer_class = CustomerSerializer
> 
>     permission_classes = [
>         IsAuthenticated
>     ]
> ```
> 

> حالت چهارم: ViewSet
> 
> 
> ```python
> class CustomerViewSet(ModelViewSet):
> 
>     queryset = Customer.objects.all()
> 
>     serializer_class = CustomerSerializer
> 
>     permission_classes = [
>         IsAuthenticated
>     ]
> ```
> 

> حالا مشکل بزرگ
> 
> 
> اگر فقط بنویسی:
> 
> ```
> permission_classes= [
> IsAuthenticated,
> IsOwner
> ]
> ```
> 
> ممکن است IsOwner اصلاً اجرا نشود!
> 
> چرا؟  چون DRF باید یک Object داشته باشد.  مثلاً:
> 
> ```
> Customer(id=1)
> ```
> 
> اما در این View:
> 
> ```
> GET/api/customers/
> ```
> 
> هنوز Object خاصی نداریم. فقط یک QuerySet داریم. پس:
> 
> ```
> has_object_permission()
> ```
> 
> اجرا نمی‌شود. Object Permission چه زمانی اجرا می‌شود؟  معمولاً در:
> 
> ```
> GET /customers/1/
> PUT /customers/1/
> PATCH /customers/1/
> DELETE /customers/1/
> ```
> 
> نه در:
> 
> ```
> GET /customers/
> ```
> 
> سناریو 1
> 
> Login با admin
> 
> ```
> POST /api/token/
> ```
> 
> توکن admin را بگیر.
> 
> در Postman:
> 
> ```
> GET /api/customers/1/
> ```
> 
> Header:
> 
> ```
> Authorization: Bearer ADMIN_TOKEN
> ```
> 
> نتیجه:
> 
> ```
> 200 OK
> ```
> 
> سناریو 2
> 
> Login با sina
> 
> توکن sina را بگیر.
> 
> همان درخواست:
> 
> ```
> GET /api/customers/1/
> ```
> 
> Header:
> 
> ```
> Authorization: Bearer SINA_TOKEN
> ```
> 
> داخل Permission:
> 
> ```
> obj.user
> ```
> 
> می‌شود:
> 
> ```
> admin
> ```
> 
> و:
> 
> ```
> request.user
> ```
> 
> می‌شود:
> 
> ```
> sina
> ```
> 
> پس:
> 
> ```
> admin==sina
> ```
> 
> نتیجه:
> 
> ```
> False
> ```
> 
> پاسخ:
> 
> ```
> 403 Forbidden
> ```
> 
> نکته خیلی مهم
> 
> در پروژه Acron ، ما بعداً برای Customer این Permission را نمی‌نویسیم:
> 
> ```
> GET/customers/1/
> ```
> 
> بلکه چیزی شبیه:
> 
> ```
> GET /customers/me/
> ```
> 
> می‌سازیم.
> 
> چرا؟
> 
> چون:
> 
> ```
> request.user.customer
> ```
> 
> را مستقیم می‌گیریم.
> 
> و اصلاً اجازه نمی‌دهیم کاربر ID دیگران را حدس بزند.
> 
> این یکی از دلایل مهمی است که APIهای حرفه‌ای endpoint هایی مثل:
> 
> ```
> /users/me/
> /customers/me/
> /profile/
> ```
> 
> دارند.
> 

Serializer چیست؟

در Django Model داریم:

```
user.username
```

اما API باید JSON برگرداند:

```
{
    "username":"admin"
}
```

تبدیل Model ↔ JSON را Serializer انجام می‌دهد.

> 22- فایل serializers.py را در مسیر apps/api/serializers.py بساز
> 

> 23- داخل فایل serializers.py که در مسیر apps/api/serializers.py کد زیر را اضافه کن:
> 
> 
> ```python
> # apps/api/serializers.py
> 
> from rest_framework import serializers
> 
> from apps.accounts import models
> 
> class UserSerializer(serializers.ModelSerializer):
> 
>     class Meta:
>         model = models.CustomUser
> 
>         fields = ['id', 'username', 'email', 'first_name', 'last_name',]
> ```
> 

استفاده در View

```python
serializer=UserSerializer(
request.user
)
```

```
serializer.data
```

خروجی:

```
{
    "id":1,
    "username":"admin",
    "email":"admin@test.com"
}
```

ModelSerializer

۹۰٪ پروژه‌های DRF از این استفاده می‌کنند.

مزیت:

به جای:

```
id=serializers.IntegerField()
username=serializers.CharField()
email=serializers.EmailField()
```

همه را از Model می‌خواند.

Serializer معمولی

گاهی Model نداریم.

مثال:

```
classLoginSerializer(
serializers.Serializer
):
username=serializers.CharField()
password=serializers.CharField()
```

تفاوت مهم

```
serializers.ModelSerializer
```

برای Modelها

```
serializers.Serializer
```

برای داده‌های معمولی

# فاز 3: Customer Domain

مدل:

- Customer

```python
user = OneToOneField(CustomUser)
phone_number
birth_date
```

هدف:

ساخت اولین Domain واقعی پروژه.

تا الان همه چیز Infrastructure بود.

از اینجا وارد Business Domain می‌شویم.

<aside>
📢

**نتیجه این فاز راه اندازی موارد زیر است :**

</aside>

```
✔ Customer Model
✔ Customer Signal
✔ Customer Admin
✔ Customer Serializer
✔ GET /api/customers/me/
✔ PATCH /api/customers/me/
✔ JWT Protection
```

> 1- در مسیر acron/config/settings/base.py این اپ را از حالت کامنت خارج کن
> 
> 
> ```python
> #  acron/config/settings/base.p 
> INSTALLED_APPS = [
>     # CREATE by me
>     ...
>     'apps.customers',
> ]
> ```
> 

الان دقیقاً در جایی هستیم که باید **تصمیمات معماری** را بگیریم، نه اینکه صرفاً کد بنویسیم.

قبل از اینکه `Customer` را بسازیم، باید تکلیف این سؤالات را مشخص کنیم.

<aside>
📢

**1- چرا OneToOneField استفاده کنیم ؟**

</aside>

> **مدل فعلی**
> 
> 
> ```python
> user=models.OneToOneField(
> settings.AUTH_USER_MODEL,
> on_delete=models.PROTECT,
> )
> ```
> 
> معنی:
> 
> ```
> هر User
>     ↓
> دقیقاً یک Customer
> 
> هر Customer
>     ↓
> دقیقاً یک User
> ```
> 
> اگر از ForeignKey استفاده می‌کردیم:
> 
> ```
> user=models.ForeignKey(...)
> ```
> 
> امکان داشت:
> 
> ```
> User 1
>  ├── Customer 1
>  ├── Customer 2
>  └── Customer 3
> ```
> 
> که برای فروشگاه اشتباه است.
> 
> ما می‌خواهیم:
> 
> ```
> User 1
>    ↓
> Customer 1
> ```
> 
> بنابراین:
> 
> ```
> OneToOneField
> ```
> 
> کاملاً تصمیم درستی است.
> 

<aside>
📢

**2- چرا PROTECT ؟**

</aside>

> این قسمت مهم‌تر از چیزی است که به نظر می‌رسد.
> 
> 
> فرض کن:
> 
> ```
> User(id=1)
> ```
> 
> و
> 
> ```
> Customer(id=1)
> ```
> 
> به هم متصل هستند.
> 
> اگر بنویسیم:
> 
> ```
> on_delete=models.CASCADE
> ```
> 
> و ادمین User را حذف کند:
> 
> ```
> User.delete()
> ```
> 
> اتفاق می‌افتد:
> 
> ```
> Customer هم حذف می‌شود
> ```
> 
> اگر بنویسیم:
> 
> ```
> on_delete=models.PROTECT
> ```
> 
> و ادمین بخواهد User را حذف کند:
> 
> ```
> ProtectedError
> ```
> 
> دریافت می‌کند.
> 
> برای فروشگاه:
> 
> من PROTECT را ترجیح می‌دهم.
> 
> چون Customer بخشی از داده‌های کسب‌وکار است.
> 

<aside>
📢

**3- آیا phone_number باید unique باشد؟**

</aside>

> سؤال مهمی است.
> 
> 
> سناریو اول:
> 
> ```
> phone_number=models.CharField(
> max_length=20,
> unique=True
> )
> ```
> 
> مزیت:
> 
> ```
> هر شماره فقط برای یک Customer
> ```
> 
> عیب:
> 
> برخی خانواده‌ها یک شماره مشترک دارند.
> 
> سناریو دوم:
> 
> ```
> phone_number=models.CharField(
> max_length=20
> )
> ```
> 
> مزیت:
> 
> انعطاف بیشتر.
> 
> برای پروژه Acron پیشنهاد اینجانب (سینا):
> 
> ```
> unique=False
> ```
> 
> فعلاً.
> 
> بعداً اگر OTP واقعی اضافه شد، دوباره تصمیم می‌گیریم.
> 

<aside>
📢

**4-**  آیا birth_date باید null باشد؟

</aside>

> پاسخ:
> 
> 
> بله.
> 
> چون موقع ثبت‌نام معمولاً این اطلاعات را نداریم.
> 
> پس:
> 
> ```
> birth_date=models.DateField(
> null=True,
> blank=True
> )
> ```
> 
> این اجازه می‌دهد:
> 
> ```
> Customer ایجاد شود
> ```
> 
> حتی اگر تاریخ تولد مشخص نباشد.
> 

<aside>
📢

**5- آیا Customer باید UUID داشته باشد؟**

</aside>

> اگر فقط داشته باشیم:
> 
> 
> ```
> id
> ```
> 
> URLها می‌شوند:
> 
> ```
> /customers/1/
> /customers/2/
> /customers/3/
> ```
> 
> مشکل:
> 
> قابل حدس زدن هستند.
> 
> راه بهتر:
> 
> ```
> uuid=models.UUIDField(...)
> ```
> 
> مثال:
> 
> ```
> /customers/8a98cf39-cdd5-44d0...
> ```
> 
> برای پروژه‌ای که قرار است Product و Order و Payment داشته باشد:
> 
> من شدیداً پیشنهاد می‌کنم UUID داشته باشیم.
> 

<aside>
📢

6- آیا BaseModel لازم داریم؟

</aside>

الان نه.

خیلی از افراد از روز اول می‌نویسند:

```
classBaseModel(...)
```

در حالی که هنوز نمی‌دانند چه چیزی مشترک خواهد بود.

من پیشنهاد می‌کنم:

فعلاً Customer را ساده بسازیم.

بعد از Product و Order متوجه می‌شویم چه فیلدهایی واقعاً مشترک هستند.

نتیجه معماری:

```python

```

درباره معماری Signal بر اساس جریان زیر است:

```python
accounts
    ↓
User Created
    ↓
Signal
    ↓
customers
    ↓
Customer Created
```

مزیت بزرگ:

app accounts هیچ وابستگی مستقیمی به customers ندارد. یعنی:

```
accounts
```

نمی‌داند Customer چیست. اما:

```
customers
```

به رویداد ثبت User گوش می‌دهد.

این دقیقاً نزدیک به Event Driven Design است و برای Acron انتخاب خوبی است.

بنابراین در این مرحله:

✅ ساخت app `customers`

✅ ساخت `Customer` model

✅ ثبت در admin

✅ migration

را می‌توانیم انجام دهیم.

اما:

❌ هنوز Signal را نسازیم.

چون قبل از ساخت Signal باید مشخص کنیم:

- User Registration API کجاست؟
- User از Admin هم ساخته می‌شود؟
- User از Shell هم ساخته می‌شود؟
- User از API هم ساخته می‌شود؟

تا بعداً Signal را یک بار و درست طراحی کنیم، نه اینکه چند بار بازنویسی شود.

ساخت Customer Model

```python
# apps/customers/models.py
from django.db import models

import uuid

from django.conf import settings

# Create your models here.
class Customer(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='customer'
    )

    phone_number = models.CharField(
        max_length=255,
        blank=True
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    def __str__(self):
        return self.user.username
```

<aside>
📢

چرا related_name='customer' گذاشتیم؟

</aside>

اگر نگذاریم:

```
customer.user
```

کار می‌کند. اما از سمت User:

```
user.customer
```

ممکن است نام پیش‌فرض جنگو را بگیریم. با این تنظیم:

```
user.customer
```

مستقیم کار می‌کند. مثال:

```
user=CustomUser.objects.get(id=1)

customer=user.customer
```

این بعداً در API بسیار استفاده خواهد شد.

ثبت در Admin

> 2- در مسیر acron/apps/customers/admin.py این  قطعه کد را اضافه کند
> 
> 
> ```python
> #  acron/config/settings/admin.p 
> 
> from django.contrib import admin
> 
> from .models import Customer
> 
> @admin.register(Customer)
> class CustomerAdmin(admin.ModelAdmin):
> 
>     list_display = [
>         'id',
>         'user',
>         'phone_number',
>         'birth_date',
>     ]
> 
>     search_fields = [
>         'user__username',
>         'phone_number',
>     ]
> ```
> 

<aside>
📢

ساخت Migration

</aside>

حالا اولین Migration مربوط به Customer را می‌سازیم.

> 3- این دستور را در ترمینال بزنید:
> 
> 
> ```
> python manage.py makemigrations customers
> ```
> 
> باید چیزی شبیه این ببینی:
> 
> ```
> Migrations for 'customers':
>   apps\customers\migrations\0001_initial.py
>     + Create model Customer
> ```
> 

> 4- سپس این دستور را در ترمینال بزنید:
> 
> 
> سپس:
> 
> ```
> python manage.py migrate
> ```
> 
> باید چیزی شبیه نتیجه زیر باشد:
> 
> ```python
> Operations to perform:
>   Apply all migrations: accounts, admin, auth, contenttypes, customers, sessions
> Running migrations:
>   Applying customers.0001_initial... OK
> ```
> 

> 5- تست داخل این پنل ادمین:
> 
> 
> سرور را اجرا کن:
> 
> ```
> python manage.py runserver
> ```
> 
> و وارد مسیر زیر شو:
> 
> ```
> http://127.0.0.1:8000/admin/
> ```
> 
> شو.
> 
> باید بخش جدیدی ببینی: 
> 
> ```
> Customers
> ```
> 
> واردش که بشی هیچ رکوردی ندارد. طبیعی است. 
> 
> چون هنوز Signal نساختیم.
> 

<aside>
📢

ساخت Serializer

</aside>

الان وارد DRF می‌شویم.

> 6- در این مسیر فایل [serializers.py](http://serializers.py) رو بساز
> 
> 
> ```bash
> apps/customers/serializers.py
> ```
> 

> 7- در این مسیر apps/customers/serializers.py کد زیر را بنویس
> 
> 
> ```python
> # apps/customers/serializers.py
> 
> from rest_framework import serializers
> 
> from .models import Customer
> 
> class CustomerSerializer(serializers.ModelSerializer):
> 
>     class Meta:
> 
>         model = Customer
> 
>         fields = [
>             'id',
>             'uuid',
>             'phone_number',
>             'birth_date',
>         ]
> ```
> 

<aside>
📢

چرا user را فعلاً برنگرداندیم؟ 

</aside>

> چون API اولیه ما: مسیر زیر خواهد بود.
> 
> 
> ```
> /api/customers/me/
> ```
> 
> در نتیجه ،  کاربر خودش را می‌بیند. پس نیازی نیست: user را داخل خروجی برگردانیم.
> 
> اگر user را اضافه می‌کردیم
> 
> مثلاً:
> 
> ```python
> classCustomerSerializer(serializers.ModelSerializer):
> 
> classMeta:
> model=Customer
> 
> fields= [
> 'id',
> 'uuid',
> 'user',
> 'phone_number',
> 'birth_date',
>         ]
> ```
> 
> و فرض کن Customer ما این باشد:
> 
> ```
> customer.id=1
> customer.user.id=5
> ```
> 
> خروجی API می‌شد:
> 
> ```
> {
>     "id":1,
>     "uuid":"a1b2c3...",
>     "user":5,
>     "phone_number":"0912...",
>     "birth_date":"1990-01-01"
> }
> ```
> 
> Serializer چه چیزی را برمی‌گرداند؟
> 
> وقتی می‌نویسی:
> 
> ```
> serializer.data
> ```
> 
> DRF یک دیکشنری JSON-ready تولید می‌کند.
> 
> مثلاً:
> 
> ```
> serializer=CustomerSerializer(customer)
> ```
> 
> ↓
> 
> ```
> serializer.data
> ```
> 
> ↓
> 
> ```
> {
>     "id":1,
>     "uuid":"...",
>     "phone_number":"...",
>     "birth_date":"..."
> }
> ```
> 
> به این می‌گوییم:
> 
> Serializer این فیلدها را "برگردانده" است.
> 
> چرا user را فعلاً برنگرداندیم؟
> 
> چون endpoint ما این است:
> 
> ```
> GET /api/customers/me/
> ```
> 
> این endpoint یعنی:
> 
> ```
> **پروفایل خودم را بده**
> ```
> 
> کاربر با JWT لاگین کرده است.
> 
> پس:
> 
> ```
> request.user
> ```
> 
> از قبل مشخص است.
> 
> بنابراین این خروجی:
> 
> ```
> {
>     "id":1,
>     "uuid":"...",
>     "phone_number":"0912..."
> }
> ```
> 
> کافی است.
> 
> اما در پروژه واقعی چه کار می‌کنیم؟
> 
> اطلاعات مهم User را Nested برمی‌گردانیم.
> 
> مثلاً:
> 
> ```
> {
>     "uuid":"...",
>     "phone_number":"0912...",
>     "user": {
>         "id":5,
>         "username":"sina",
>         "email":"sina@test.com"
>     }
> }
> ```
> 
> این حالت حرفه‌ای‌تر است.
> 
> ولی هنوز به Nested Serializer نرسیده‌ایم.
> 

> نکته مهم‌تر
> 
> 
> وقتی گفتم:
> 
> فعلاً user را برنگرداندیم
> 
> منظورم فقط خروجی API بود.
> 
> منظورم این نبود که:
> 
> ```
> Customer.user
> ```
> 
> در مدل وجود ندارد.
> 
> مدل هنوز این را دارد: و این بخش کاملاً ضروری است. :
> 
> ```
> user=models.OneToOneField(
> settings.AUTH_USER_MODEL,
> on_delete=models.PROTECT,
> related_name='customer'
> )
> ```
> 

<aside>
📢

اولین Customer API

</aside>

هدف:

```
GET /api/customers/me/
```

این endpoint یکی از رایج‌ترین endpointهای پروژه‌های واقعی است.

> 8- در مسیر apps/customers/views.py این کد رو بنویس:
> 
> 
> ```python
> # apps/customers/views.py
> from rest_framework.response import Response
> from rest_framework.views import APIView
> from rest_framework.permissions import IsAuthenticated
> 
> from .serializers import CustomerSerializer
> 
> class CustomerMeView(APIView):
> 
>     permission_classes = [
>         IsAuthenticated
>     ]
> 
>     def get(self, request):
> 
>         serializer = CustomerSerializer(
>             request.user.customer
>         )
> 
>         return Response(
>             serializer.data
>         )
> ```
> 

این خط بسیار مهم است

```
request.user.customer
```

چرا مهم است؟ به خاطر:

```
related_name='customer'
```

که در Model تعریف کردیم. پشت صحنه:

```
Customer.objects.get(
user=request.user
)
```

انجام می‌شود.

<aside>
📢

URLهای Customer

</aside>

> 9- فایل [urls.py](http://urls.py) در مسیر apps/customers/urls.py بساز:
> 
> 
> ```python
> apps/customers/urls.py
> ```
> 

> 10- در مسیر apps/customers/urls.py کد زیر را بنویس :
> 
> 
> ```python
> # apps/customers/urls.py
> 
> from django.urls import path
> 
> from .views import CustomerMeView
> 
> urlpatterns = [
> 
>     path(
>         'me/',
>         CustomerMeView.as_view(),
>         name='customer-me'
>     ),
> 
> ]
> 
> ```
> 

<aside>
📢

اتصال به API اصلی

</aside>

در اینجا یک تصمیم معماری مهم داریم.  پیشنهادم اینکه customers مسیر جداگانه داشته باشد. :

```
/api/customers/
```

> 11- در مسیر apps/api/urls.py این کد رو اضافه کن:
> 
> 
> ```python
> # apps/api/urls.py
> ```
> 

نتیجه

الان URL نهایی:

```
/api/customers/me/
```

خواهد بود. 

اما یک مشکل داریم 🚨

اگر الان با postman  تست کنی: + access token هم از قسمت Authorization از قسمت Auth Type روی گزینه Bearer Token تنظیم کن و مقدارش رو سمت راستش اضافه کن.

```
GET /api/customers/me/
```

احتمال زیاد این خطا را می‌گیری:

```
Customer matching query does not exist
```

چرا؟

چون هنوز هیچ Customer برای User ساخته نشده.

این دقیقاً جایی است که وارد مرحله بعدی می‌شویم

اینجا باید تصمیم بگیریم:

راه 1

Customer را دستی بسازیم.

راه 2

هنگام ثبت User:

```
User Created
      ↓
Signal
      ↓
Customer Created
```

اینجانب راه دوم را انتخاب کردم. 
مرحله بعدی طراحی **Signal Architecture** خواهد بود تا هر زمان User ساخته شد، Customer متناظر هم به صورت خودکار ایجاد شود.

چرا Signal؟

بدون Signal معمولاً این اتفاق می‌افتد:

```
user=CustomUser.objects.create_user(...)
```

و برنامه‌نویس باید یادش باشد:

```
Customer.objects.create(user=user)
```

را هم بنویسد.

مشکل چیست؟

اگر فردا:

- از Admin کاربر بسازی
- از Shell کاربر بسازی
- از API کاربر بسازی
- از Import Script کاربر بسازی

ممکن است جایی فراموش شود Customer ساخته شود.

Signal این مشکل را حل می‌کند.

قبل از نوشتن کد

باید تصمیم معماری بگیریم:

Signal داخل کدام App باشد؟

گزینه اول (اشتباه)

داخل accounts

```
accounts/
├── signals.py
```

و:

```
fromapps.customers.modelsimportCustomer
```

مشکل:

```
accounts
   ↓
customers
```

وابستگی مستقیم پیدا می‌کند.

بعداً اگر Customer را حذف کنیم:

```
accounts
```

خراب می‌شود.

گزینه دوم (صحیح)

Signal داخل customers

```
customers/
├── signals.py
```

چون:

```
accounts
```

نباید بداند Customer چیست.

اما:

```
customers
```

می‌تواند به رویدادهای User گوش دهد.

> 12- ساخت [signals.py](http://signals.py/) در مسیر زیر انجام شود
> 
> 
> ```python
> # apps/customers/signals.py
> ```
> 

> 13- داخل مسیر apps/customers/signals.py کد زیر را اضافه کن در ادامه توضیح داده میشود:
> 
> 
> ```python
> # apps/customers/signals.py
> from django.db.models.signals import post_save
> from django.dispatch import receiver
> 
> from apps.accounts.models import CustomUser
> from .models import Customer
> 
> @receiver(
>     post_save,
>     sender=CustomUser
> )
> def create_customer(
>     sender,
>     instance,
>     created,
>     **kwargs
> ):
>     if created:
> 
>         Customer.objects.create(
>             user=instance
>         )
> ```
> 

post_save چیست؟

هر وقت:

```
obj.save()
```

اجرا شود،

جنگو یک Signal منتشر می‌کند.

برای مثال:

```
user=CustomUser.objects.create_user(
username='sina'
)
```

پشت صحنه:

```
user.save()
```

اجرا می‌شود.

بعد از save:

```
post_save
```

منتشر می‌شود.

پارامترها را بشناسیم:

sender

مدلی که Signal را فرستاده

اینجا:

```
CustomUser
```

instance

آبجکت ذخیره شده

مثلاً:

```
user=CustomUser(...)
```

پس:

```
instance==user
```

created

مهم‌ترین پارامتر

اگر User جدید باشد:

```
True
```

اگر User قبلاً وجود داشته باشد و فقط ویرایش شود:

```
False
```

مثال:

```
user.first_name='Sina'
user.save()
```

اینجا:

```
created=False
```

این یعنی:

```
New User
     ↓
Customer.objects.create(...)
```

اما هنوز کار نمی‌کند!

تو فایل را ساختی:

```
customers/signals.py
```

اما Django آن را Import نمی‌کند. پس Receiver ثبت نمی‌شود.

پس همیشه بعد از طراحی و توسعه signal اون رو باید داخل پروژه جنگو ثبت کنی.

<aside>
📢

**ثبت Signal**

</aside>

> 14- این اپ رو [apps.py](http://apps.py/) در مسیر زیر بررسی کن:
> 
> 
> ```python
> # apps/customers/apps.py
> ```
> 

نسخه فعلی:

```python
fromdjango.appsimportAppConfig

classCustomersConfig(AppConfig):

default_auto_field='django.db.models.BigAutoField'
name='apps.customers'
```

> 15- تابع داخل مسیر زیر را بروزرسانی کن:
> 
> 
> ```python
> # apps/customers/apps.py
> from django.apps import AppConfig
> 
> class CustomersConfig(AppConfig):
> 
>     default_auto_field = 'django.db.models.BigAutoField'
>     name = 'apps.customers'
> 
>     def ready(self):
> 
>     from . import signals
> ```
> 

<aside>
📢

ready() کی اجرا می‌شود؟

</aside>

هنگام بالا آمدن Django:

```
Run Server
Migration
Shell
Admin
```

در نتیجه:

```
importapps.customers.signals
```

اجرا می‌شود.

و Receiver ثبت می‌شود.

<aside>
📢

تست Signal

</aside>

اول سرور را ریستارت کن.

وارد Admin شو.

کاربر جدید بساز:

```
username: ali
password: 1234
```

Save کن

برو:

```
Admin → Customers
```

باید ببینی:

```
Customer
    ↓
user = ali
```

خودکار ساخته شده. اگر ساخته نشده برگرد چند قدم عقب تر خط به خط کدهایی که نوشته بودی رو چک کن. شاید قطعه کدی از دستت در رفته باشه

<aside>
📢

**تست در Shell**

</aside>

> 15- زمانی که  Python virtualenv  فعال است داخل ترمینال این رو بنویس
> 
> 
> ```bash
> python manage.py shell
> ```
> 

> 16- بعد از وارد شدن داخل shell
> 
> 
> ```bash
> **from apps.accounts.models import CustomUser
> 
> user = CustomUser.objects.create_user(
>     username='test_user',
>     password='1234'
> )**
> ```
> 

> 17- وقتی مینویسی
> 
> 
> ```bash
> **user.customer**
> ```
> 

> 18- باید این رو برگرداند
> 
> 
> ```bash
> **<Customer: test_user>**
> ```
> 

```bash
>>> from apps.accounts.models import CustomUser
>>> user = CustomUser.objects.create_user(
...     username='test_user',
...     password='1234'
... )
>>> user.customer
<Customer: test_user>
>>>

```

<aside>
📢

بهبود مهم انجام شد

</aside>

الان Customer این شکلی ساخته می‌شود:

```
Customer.objects.create(
user=instance
)
```

و فیلدهای زیر خالی هستند:

```
phone_number
birth_date
```

این مشکلی ندارد.

چون ما قبلاً تصمیم گرفتیم:

```
blank=True
null=True
```

داشته باشند.

<aside>
📢

نتیجه تا اینجا

</aside>

الان معماری Accounts ↔ Customers کامل شده است:

```
accounts
    ↓
CustomUser
    ↓ post_save
customers
    ↓
Customer
```

و مهم‌تر:

```
accounts
```

هیچ Import مستقیمی از:

```
customers
```

ندارد.

این یک جداسازی (Decoupling) بسیار تمیز برای ادامه فاز 3 و بعداً Product Domain است.

<aside>
📢

**ساخت APIهای Customer**

</aside>

از جمله:

```
GET    /api/customers/me/
PATCH  /api/customers/me/
```

تا کاربر بتواند پروفایل Customer خودش را مشاهده و ویرایش کند.

<aside>
📢

GET /api/customers/me/

</aside>

هدف:

کاربر لاگین کرده بتواند پروفایل خودش را ببیند و ویرایش کند.

<aside>
📢

**ساخت PATCH API**

</aside>

```
phone_number
birth_date
```

> 19- یک متد جدید برای کلاس `class CustomerMeView(APIView):` بساز :
> 
> 
> ```python
> # apps/customers/views.py
> class CustomerMeView(APIView):
> 		...
> 		...
>     def patch(self, request):
>         serializer = CustomerSerializer(request.user.customer,data=request.data,partial=True)
>         serializer.is_valid(raise_exception=True)
>         serializer.save()
>         return Response(serializer.data)
> 				
> ```
> 

<aside>
📢

**partial=True چیست؟**

</aside>

اگر نگذاریم: به صورت پیشفرض حالت زیر می باشد.

```
partial=False
```

یعنی: همه فیلدها باید ارسال شوند

اما PATCH یعنی:  فقط بخشی از فیلدها

مثال:

```
{
    "phone_number":"09120000000"
}
```

پس حالت زیر ضروری است:

```
partial=True
```

<aside>
📢

تست GET در Postman

</aside>

Login

```
POST /api/token/
```

Body:

```
{
    "username":"sina",
    "password":"1234"
}
```

پاسخ:

```
{
    "access":"...",
    "refresh":"..."
}
```

Access را کپی کن.

<aside>
📢

درخواست GET

</aside>

```
GET /api/customers/me/
```

Authorization:

```
Bearer Token
```

Token:

```
ACCESS_TOKEN
```

Send

پاسخ:

```
{
    "id":1,
    "uuid":"...",
    "phone_number":"",
    "birth_date":null
}
```

<aside>
📢

تست PATCH در Postman

</aside>

Method:

```
PATCH
```

URL:

```
http://127.0.0.1:8000/api/customers/me/
```

Authorization:

```
Bearer Token
```

Body → raw → JSON

```
{
    "phone_number":"09121234567"
}
```

Send

پاسخ:

```
{
    "id":1,
    "uuid":"...",
    "phone_number":"09121234567",
    "birth_date":null
}
```

اگر ارور زیر را گرفتی تنها کافیه آخر url نرم افزار postman یک اسلش اضافه کنی:

> RuntimeError at /api/customers/meYou called this URL via PATCH, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining PATCH data. Change your form to point to 127.0.0.1:8000/api/customers/me/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.
> 

<aside>
📢

چرا GET کار می‌کند ولی PATCH خطا می‌دهد؟

</aside>

Django به صورت پیش‌فرض این تنظیم را دارد:

```
APPEND_SLASH=True
```

وقتی درخواست:

```
GET /api/customers/me
```

بیاید،

Django می‌تواند به صورت خودکار ریدایرکت کند به:

```
GET /api/customers/me/
```

و هیچ اطلاعاتی از دست نمی‌رود.

<aside>
📢

اما برای PATCH:

</aside>

```
PATCH /api/customers/me
```

اگر Django بخواهد ریدایرکت کند به:

```
PATCH /api/customers/me/
```

ممکن است Body درخواست از بین برود.

مثلاً:

```
{
    "phone_number":"09121234567"
}
```

بنابراین Django برای جلوگیری از از دست رفتن داده‌ها خطا می‌دهد.

<aside>
📢

راه حل

</aside>

در Postman آدرس را اینگونه بنویس:

```
http://127.0.0.1:8000/api/customers/me/
```

دقت کن:

```
/
```

آخر URL وجود داشته باشد.

<aside>
📢

آیا APPEND_SLASH=False بگذاریم؟

</aside>

فعلاً نه.

در پروژه‌های Django معمولاً URLها را با اسلش انتهایی تعریف می‌کنند:

```
path('me/', ...)
path('products/', ...)
path('customers/', ...)
```

و درخواست‌ها هم با اسلش ارسال می‌شوند:

```
/api/customers/me/
/api/products/
/api/orders/
```

بنابراین در این پروژه فعلاً:

```
APPEND_SLASH=True
```

را دست نزن.

فقط در Postman و مرورگر عادت کن همیشه URLها را دقیقاً مطابق `urls.py` بنویسی.

<aside>
📢

یک نکته آموزشی مهم:

</aside>

اگر الان این دستور را در Shell اجرا کنی:

```
fromdjango.urlsimportreverse

reverse('customer-me')
```

خروجی خواهد بود:

```
http://127.0.0.1:8000/api/customers/me/
```

و همین نشان می‌دهد که URL رسمی پروژه با `/` انتهایی تعریف شده است.

<aside>
📢

Nested Serializer

</aside>

<aside>
📢

# پایان Part-1

</aside>
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-2.md`
```md
# ACRON Methodology Part-2

# فاز 3: Customer Domain

<aside>
📢

**در Part-1 ، فاز 3 تا قدم 19 پیش رفت.**

</aside>

<aside>
📢

Nested Serializer

</aside>

یعنی خروجی:

```
{
  "uuid":"...",
  "phone_number":"0912...",
  "birth_date":"1995-01-20",
  "user": {
    "id":1,
    "username":"sina",
    "email":"sina@example.com"
  }
}
```

تا API پروفایل کاربر به شکل حرفه‌ای و نزدیک به پروژه‌های واقعی فروشگاهی دربیاید.

<aside>
📢

ساخت User Serializer

</aside>

> 20- در ابتدای فایل زیر این خط رو اضافه کن:
> 
> 
> ```python
> # apps/customers/serializers.py
> from apps.accounts import models as accounts_models
> ```
> 

> 21- در ادامه ی فایل زیر این قطعه کد رو اضافه کن:
> 
> 
> ```python
> # apps/customers/serializers.py
> class UserSerializer(serializers.ModelSerializer):
> 
>     class Meta:
>         model = CustomUser
> 
>         fields = [
>             'id',
>             'username',
>             'email',
>         ]
> ```
> 

> 21- در ادامه ی فایل زیر این قطعه کد رو اضافه کن:
Nested کردن داخل CustomerSerializer
> 
> 
> ```python
> # apps/customers/serializers.py
> class CustomerSerializer(serializers.ModelSerializer):
> 
>     user = UserSerializer(read_only=True)
> 
>     class Meta:
>         model = Customer
> 
>         fields = [
>             'id',
>             'uuid',
>             'phone_number',
>             'birth_date',
>             'user',
>         ]
> ```
> 

<aside>
📢

خروجی جدید API

</aside>

اکنون:

```
GET /api/customers/me/
```

خروجی:

```
{
  "id":1,
  "uuid":"a57aab0c-8d4d-4c3e-b20e-7a8e6c6c2d99",
  "phone_number":"09121234567",
  "birth_date":"1995-01-20",
  "user": {
    "id":1,
    "username":"sina",
    "email":"sina@example.com"
  }
}
```

این ساختار بسیار نزدیک‌تر به APIهای حرفه‌ای فروشگاهی است.

<aside>
📢

⚠️ مورد اصلاحی — طول phone_number

</aside>

الان:

```python
phone_number=models.CharField(
max_length=255,
blank=True
)
```

برای شماره تلفن 255 زیاد است.

> 22- پیشنهاد:
> 
> 
> ```python
> phone_number=models.CharField(
> max_length=20,
> blank=True
> )
> ```
> 

چون:

```
+44xxxxxxxxxx
09121234567
+989121234567
```

همگی زیر 20 کاراکتر هستند.

```bash
python manage.py makemigrations customers
```

خروجی اینچنین خواهد شد:

```python
Migrations for 'customers':
  apps\customers\migrations\0002_alter_customer_phone_number.py
    ~ Alter field phone_number on customer
```

سپس migrate 

```python
python manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, auth, contenttypes, customers, sessions
Running migrations:
  Applying customers.0002_alter_customer_phone_number... OK

```

<aside>
📢

⚠️ مورد اصلاحی — محافظت از user

</aside>

الان:

```python
user=UserSerializer(read_only=True)
```

خوب است.

اما بهتر است صریح‌تر باشیم:

```python
read_only_fields= [
'id',
'uuid',
'user',
]
```

داخل Meta

یعنی:

```python
classMeta:
model=Customer

fields= [
'id',
'uuid',
'phone_number',
'birth_date',
'user',
    ]

read_only_fields= [
'id',
'uuid',
'user',
    ]
```

این باعث می‌شود هیچ‌کس نتواند از طریق PATCH این فیلدها را تغییر دهد.

<aside>
📢

⚠️ مورد اصلاحی — جلوگیری از ساخت Customer تکراری

</aside>

فعلاً:

```python
ifcreated:
Customer.objects.create(
user=instance
    )
```

مشکلی ندارد.

اما نسخه مقاوم‌تر:

```python
ifcreated:
Customer.objects.get_or_create(
user=instance
    )
```

مزیت:

اگر به هر دلیلی سیگنال دوبار اجرا شد:

```bash
IntegrityError
```

نمی‌گیری.

<aside>
📢

**Validation شماره موبایل**

</aside>

داخل CustomerSerializer:

```python
def validate_phone_number(self,value):

	if value and len(value)<10:
			raise serializers.ValidationError(
			"Phone number is too short."
		        )
	
	return value
```

وقتی فیلدی به اسم:

```
phone_number
```

را در Serializer پیدا می‌کند، دنبال متدی با این نام می‌گردد:

```
validate_phone_number
```

یعنی:

```
validate_<field_name>
```

---

پشت صحنه تقریباً چیزی شبیه این اتفاق می‌افتد:

```python
for field in serializer.fields:

		method_name = f"validate_{field}"
		
		if hasattr(serializer,method_name):
				validator=getattr(serializer,method_name)
				
				validator(value)
```

البته کد واقعی DRF پیچیده‌تر است، ولی مفهوم همین است.

<aside>
📢

**Validation تاریخ تولد**

</aside>

```python
from datetime import date
```

```python
def validate_birth_date(self, value):

    if value and value > date.today():
        raise serializers.ValidationError(
            "Birth date cannot be in future."
        )

    return value
```

فرض کن بخواهی رابطه بین چند فیلد را بررسی کنی:

```python
def validate(self,attrs):

		phone=attrs.get("phone_number")
		birth=attrs.get("birth_date")
		
		    ...
		
		return attrs
```

اینجا دیگر Validation مربوط به یک فیلد خاص نیست.

بلکه Validation کل آبجکت است.

پس به طور خلاصه:

| نام متد | چه زمانی اجرا می‌شود |
| --- | --- |
| `validate_phone_number()` | فقط برای فیلد phone_number |
| `validate_birth_date()` | فقط برای فیلد birth_date |
| `validate_email()` | فقط برای فیلد email |
| `validate()` | برای کل Serializer |

همه این‌ها زمانی اجرا می‌شوند که این خط را بزنی:

```
serializer.is_valid()
```

<aside>
📢

# پایان Part-2

</aside>
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-3.md`
```md
# ACRON Methodology Part-3

# فاز 3: Customer Domain

<aside>
📢

در Part-2 ، فاز 3 تا قدم 22 پیش رفت

</aside>

این قسمت برای گیت هاب است و اختیاری می باشد برای همین داخل قدم ها نیاوردم:

این کد رو داخل ترمینال بزن و سپس داخل گیت هاب push : 

اگر از pipenv استفاده میکنی:

```python
pipenv requirements > requirements.tx
```

اگر از pip venv استفاده میکنی:

```python
pip freeze > requirements.txt
```

نتیجه چیزی شبیه به این خواهد بود:

```python
-i https://pypi.org/simple
asgiref==3.11.1; python_version >= '3.9'
django==6.0.6; python_version >= '3.12'
djangorestframework==3.17.1; python_version >= '3.10'
djangorestframework-simplejwt==5.5.1; python_version >= '3.9'
mysqlclient==2.2.8; python_version >= '3.10'
pyjwt==2.13.0; python_version >= '3.9'
sqlparse==0.5.5; python_version >= '3.8'
tzdata==2026.2; python_version >= '2'
```

این فایل رو داخل گیت هاب بساز:

```python
project/.github/workflows/django.yml
```

```python
name: Django CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    # ۱. راه‌اندازی دیتابیس موقت MySQL روی سرور گیت‌هاب
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: '1234' # دقیقاً مطابق پسورد شما در development.py
          MYSQL_DATABASE: 'acron'      # دقیقاً مطابق نام دیتابیس شما
        ports:
          - 3306:3306
        options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=3

    strategy:
      matrix:
        # ۲. هماهنگی باrequirements: جنگو ۶ حداقل به پایتون ۳.۱۲ نیاز دارد
        python-version: ["3.12", "3.13"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'

    # ۳. نصب ابزارهای لینوکسی مورد نیاز برای کامپایل کتابخانه mysqlclient
    - name: Install Linux Dependencies for MySQL
      run: |
        sudo apt-get update
        sudo apt-get install -y default-libmysqlclient-dev pkg-config build-essential

    - name: Install Python Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # ۴. اجرای تست‌ها با معرفی آدرس جدید فایل تنظیمات
    - name: Run Tests
      env:
        DJANGO_SETTINGS_MODULE: config.settings.development
      run: |
        python manage.py test
```

جزییات موفق شدن یا شکست خوردن این قسمت رو بعدا انجام میدهیم نگران نباشید که

<aside>
📢

تست CustomerModelTest

</aside>

> 23- این فایل ها برای معماری تست نویسی ساخته شود:
> 
> 
> apps/
> ├── customers/
> │   ├── tests/
> │   │   ├── **init**.py
> │   │   ├── test_models.py
> │   │   ├── test_signals.py
> │   │   ├── test_serializers.py
> │   │   └── test_api.py
> 

<aside>
📢

**CustomerModelTest**

</aside>

> 24- فایل زیر را بساز
> 
> 
> apps/customers/tests/test_models.py
> 

> 25- داخل فایلی که ساختی این رو بنویس
> 
> 
> ```python
> # apps/customers/tests/test_models.py
> from django.test import TestCase
> 
> from apps.accounts.models import CustomUser
> from apps.customers.models import Customer
> 
> class CustomerModelTest(TestCase):
> 
>     def setUp(self):
>         self.user = CustomUser.objects.create_user(
>             username='sina',
>             email='sina@test.com',
>             password='12345678'
>         )
> 
>     def test_customer_created_by_signal(self):
>         self.assertTrue(
>             Customer.objects.filter(
>                 user=self.user
>             ).exists()
>         )
> 
>     def test_customer_has_uuid(self):
>         customer = self.user.customer
> 
>         self.assertIsNotNone(
>             customer.uuid
>         )
> 
>     def test_customer_str(self):
>         customer = self.user.customer
> 
>         self.assertEqual(
>             str(customer),
>             self.user.username
>         )
> ```
> 

<aside>
📢

CustomerSignalTest

</aside>

> 26- فایل زیر را بساز
> 
> 
> apps/customers/tests/test_signals.py
> 

> 27- داخل فایلی که ساختی این رو بنویس
> 
> 
> ```python
> from django.test import TestCase
> 
> from apps.accounts.models import CustomUser
> from apps.customers.models import Customer
> 
> class CustomerSignalTest(TestCase):
> 
>     def test_signal_creates_customer(self):
> 
>         user = CustomUser.objects.create_user(
>             username='signal_user',
>             email='signal@test.com',
>             password='12345678'
>         )
> 
>         self.assertTrue(
>             Customer.objects.filter(
>                 user=user
>             ).exists()
>         )
> 
>     def test_only_one_customer_created(self):
> 
>         user = CustomUser.objects.create_user(
>             username='signal_user2',
>             email='signal2@test.com',
>             password='12345678'
>         )
> 
>         self.assertEqual(
>             Customer.objects.filter(
>                 user=user
>             ).count(),
>             1
>         )
> ```
> 

اجرای تست و نتیجه ی تست در ترمینال باید شبیه به زیر باشد:

```bash
$ python manage.py test apps/customers/tests/
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 19.088s

OK
Destroying test database for alias 'default'...

```

<aside>
📢

CustomerSerializerTest

</aside>

> 28- فایل زیر را بساز
> 
> 
> apps/customers/tests/test_serializers.py
> 

> 29- داخل فایلی که ساختی این رو بنویس
> 
> 
> ```python
> from django.test import TestCase
> 
> from apps.accounts.models import CustomUser
> from apps.customers.serializers import CustomerSerializer
> 
> class CustomerSerializerTest(TestCase):
> 
>     def setUp(self):
>         self.user = CustomUser.objects.create_user(
>             username='serializer_user',
>             email='serializer@test.com',
>             password='12345678'
>         )
> 
>         self.customer = self.user.customer
> 
>     def test_serializer_contains_expected_fields(self):
> 
>         serializer = CustomerSerializer(
>             self.customer
>         )
> 
>         data = serializer.data
> 
>         self.assertIn('id', data)
>         self.assertIn('uuid', data)
>         self.assertIn('phone_number', data)
>         self.assertIn('birth_date', data)
>         self.assertIn('user', data)
> 
>     def test_nested_user_serializer(self):
> 
>         serializer = CustomerSerializer(
>             self.customer
>         )
> 
>         user_data = serializer.data['user']
> 
>         self.assertEqual(
>             user_data['username'],
>             self.user.username
>         )
> 
>         self.assertEqual(
>             user_data['email'],
>             self.user.email
>         )
> ```
> 

اجرای تست و نتیجه ی تست در ترمینال باید شبیه به زیر باشد:

```bash
$ python manage.py test apps/customers/tests/
Found 7 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 26.793s

OK
Destroying test database for alias 'default'...

```

<aside>
📢

CustomerMeApiTest

</aside>

> 30- فایل زیر را بساز
> 
> 
> apps/customers/tests/test_api.py
> 

> 31- داخل فایلی که ساختی این رو بنویس
> 
> 
> ```python
> from rest_framework.test import APITestCase
> from rest_framework import status
> 
> from apps.accounts.models import CustomUser
> 
> class CustomerMeApiTest(APITestCase):
> 
>     def setUp(self):
> 
>         self.user = CustomUser.objects.create_user(
>             username='api_user',
>             email='api@test.com',
>             password='12345678'
>         )
> 
>     def test_authentication_required(self):
> 
>         response = self.client.get(
>             '/api/customers/me/'
>         )
> 
>         self.assertEqual(
>             response.status_code,
>             status.HTTP_401_UNAUTHORIZED
>         )
> 
>     def test_get_customer_profile(self):
> 
>         self.client.force_authenticate(
>             user=self.user
>         )
> 
>         response = self.client.get(
>             '/api/customers/me/'
>         )
> 
>         self.assertEqual(
>             response.status_code,
>             status.HTTP_200_OK
>         )
> 
>         self.assertEqual(
>             response.data['user']['username'],
>             self.user.username
>         )
> 
>     def test_patch_customer_profile(self):
> 
>         self.client.force_authenticate(
>             user=self.user
>         )
> 
>         response = self.client.patch(
>             '/api/customers/me/',
>             {
>                 'phone_number': '09121234567'
>             },
>             format='json'
>         )
> 
>         self.assertEqual(
>             response.status_code,
>             status.HTTP_200_OK
>         )
> 
>         self.assertEqual(
>             response.data['phone_number'],
>             '09121234567'
>         )
> ```
> 

اجرای تست و نتیجه ی تست در ترمینال باید شبیه به زیر باشد:

```bash
$ python manage.py test apps/customers/tests/
Found 10 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 46.933s

OK
```

اجرای تست‌ها

اجرای فقط تست‌های Customer در ترمینال در دایرکتوری پروژه + pipenv فعال باشه:

```bash
$ python manage.py test apps/customers/tests/
Found 10 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 46.933s

OK
```

<aside>
📢

توجه کن

</aside>

الان تست‌های بالا حدود 80٪ دامنه Customer را پوشش می‌دهند:

| بخش | پوشش |
| --- | --- |
| Model | ✅ |
| Signal | ✅ |
| Serializer | ✅ |
| GET API | ✅ |
| PATCH API | ✅ |
| Authentication | ✅ |
| Validation | ❌ هنوز تست نشده |

هر خط را توضیح می‌دهم:

- چرا نوشته شده؟
- چه کاری انجام می‌دهد؟
- Django پشت صحنه چه می‌کند؟
- اگر حذفش کنیم چه اتفاقی می‌افتد؟
- چرا این روش را انتخاب کردیم؟

<aside>
📢

اول: Test چیست؟

</aside>

فرض کن این کد را داری:

```
customer=Customer.objects.create(...)
```

از کجا مطمئن هستی که درست کار می‌کند؟

راه سنتی:

```
pythonmanage.pyshell
```

بعد دستی تست می‌کنی.

اما راه حرفه‌ای:

```
pythonmanage.pytest
```

خود جنگو تمام تست‌ها را اجرا می‌کند.

<aside>
📢

اولین تست

</aside>

مثلاً:

```
fromdjango.testimportTestCase
```

سؤال:

TestCase چیست؟ پاسخ: یک کلاس مخصوص Django برای تست است.

مثلاً:

```
classCustomerModelTest(TestCase):
pass
```

یعنی:

```
این کلاس شامل تست‌های Customer است
```

<aside>
📢

متد setUp

</aside>

مثلاً:

```
defsetUp(self):
```

این متد قبل از هر تست اجرا می‌شود.

فرض کن ۵ تست داری:

```
test_a()
test_b()
test_c()
test_d()
test_e()
```

قبل از هر کدام:

```
setUp()
```

اجرا می‌شود.

مثال:

```python
def setUp(self):

    self.user = CustomUser.objects.create_user(
        username='sina',
        email='sina@test.com',
        password='12345678'
    )
```

پشت صحنه:

```
**قبل از هر تست

یک User جدید بساز**
```

<aside>
📢

self چیست؟

</aside>

این سؤال خیلی مهم است.

وقتی می‌نویسی:

```
self.user
```

یعنی:

```
این متغیر متعلق به همین کلاس است
```

بعداً در هر تست می‌توانی استفاده کنی:

```
self.user
```

<aside>
📢

تست اول

</aside>

```
deftest_customer_created_by_signal(self):
```

چرا اسمش با test شروع شده؟

چون Django فقط متدهایی را اجرا می‌کند که با:

```
test_
```

شروع شوند.

اگر بنویسی:

```
defcustomer_created(self):
```

اصلاً اجرا نمی‌شود.

<aside>
📢

assert چیست؟

</aside>

مثلاً:

```python
self.assertTrue(
    Customer.objects.filter(
        user=self.user
    ).exists()
)
```

قسمت اول:

```python
Customer.objects.filter(
    user=self.user
)
```

یعنی:

```sql
SELECT*
FROM customers_customer
WHERE user_id= self.user.id
```

سپس:

```python
.exists()
```

یعنی: 

آیا حداقل یک رکورد پیدا شد؟

خروجی:

```
True
```

یا

```
False
```

حالا:

```
assertTrue(...)
```

یعنی:

من انتظار دارم نتیجه True باشد

اگر:

```
True
```

باشد:

تست پاس می‌شود.

اگر:

```
False
```

باشد:

تست Fail می‌شود.

چرا این تست مهم است؟

چون می‌خواهیم مطمئن شویم Signal کار می‌کند.

جریان:

```
User Created
    ↓
Signal
    ↓
Customer Created
```

اگر سیگنال خراب شود:

```
False
```

می‌گیریم.

<aside>
📢

تست UUID

</aside>

کد:

```
customer=self.user.customer
```

پشت صحنه:

```python
Customer.objects.get(
		user=self.user
	)
```

اجرا می‌شود.

به خاطر:

```
related_name='customer'
```

سپس:

```
self.assertIsNotNone(
	customer.uuid
	)
```

یعنی:

```
بررسی کن uuid خالی نباشد
```

اگر:

```
customer.uuid
```

برابر باشد با:

```
None
```

تست Fail می‌شود.

<aside>
📢

تست **str**

</aside>

```python
self.assertEqual(
    str(customer),
    self.user.username
)
```

یعنی:

```
خروجی str(customer)
باید برابر username باشد
```

چرا؟

چون در مدل نوشتیم:

```
def__str__(self):
		returnself.user.username
```

---

```python
Customer.objects.filter(
    user=self.user
).exists()
```

آیا Customer ای وجود دارد که
فیلد user آن برابر self.user باشد؟
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-4.md`
```md
# ACRON Methodology Part-4

# فاز 3: Customer Domain

<aside>
📢

در Part-3 ، فاز 3 تا قدم 31 پیش رفت

</aside>

> 32- فایل `apps/customers/tests/test_api.py` را باز کنید و در بالای فایل، ماژول `datetime` را اضافه کنید:
> 
> 
> ```python
> from rest_framework.test import APITestCase
> from rest_framework import status
> import datetime # این خط اضافه شود
> 
> from apps.accounts.models import CustomUser
> ```
> 

> **33- این دو متد جدید را به انتهای کلاس `CustomerMeApiTest` اضافه کنید:**
> 
> 
> ```python
> def test_patch_invalid_phone_number(self):
>         # ۱. احراز هویت کاربر
>         self.client.force_authenticate(user=self.user)
>         
>         # ۲. ارسال درخواست ویرایش با شماره تلفن غلط (کمتر از 10 کاراکتر)
>         response = self.client.patch(
>             '/api/customers/me/',
>             {
>                 'phone_number': '123' 
>             },
>             format='json'
>         )
> 
>         # ۳. بررسی اینکه آیا سیستم خطای 400 (Bad Request) داده است؟
>         self.assertEqual(
>             response.status_code,
>             status.HTTP_400_BAD_REQUEST
>         )
> 
>         # ۴. بررسی اینکه آیا خطا دقیقاً مربوط به فیلد phone_number است؟
>         self.assertIn('phone_number', response.data)
> 
>     def test_patch_future_birth_date(self):
>         self.client.force_authenticate(user=self.user)
>         
>         # ۱. ساخت یک تاریخ در آینده (مثلاً 10 روز بعد از امروز)
>         future_date = (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
>         
>         # ۲. ارسال تاریخ آینده به سرور
>         response = self.client.patch(
>             '/api/customers/me/',
>             {
>                 'birth_date': future_date
>             },
>             format='json'
>         )
> 
>         # ۳. بررسی اینکه آیا سیستم خطای 400 داده است؟
>         self.assertEqual(
>             response.status_code,
>             status.HTTP_400_BAD_REQUEST
>         )
>         
>         # ۴. بررسی اینکه آیا خطا مربوط به فیلد birth_date است؟
>         self.assertIn('birth_date', response.data)
> ```
> 

نتیجه شبیه به این خواهد بود:

```python
$ python manage.py test apps/customers/tests/
Found 12 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............
----------------------------------------------------------------------
Ran 12 tests in 63.191s

OK
Destroying test database for alias 'default'...
```

**کالبدشکافی سریع کد (چرا اینطور نوشتیم؟):**

- **`status.HTTP_400_BAD_REQUEST`:** در معماری REST، وقتی کلاینت (فرانت‌اند یا موبایل) دیتای نامعتبری می‌فرستد، سرور باید کد 400 را برگرداند. متد `.is_valid()` در DRF این کار را به صورت خودکار انجام می‌دهد.
- **`self.assertIn('phone_number', response.data)`:** ما فقط نمی‌خواهیم بدانیم که سیستم خطا داده است، بلکه می‌خواهیم مطمئن شویم سیستم دقیقاً فهمیده است که مشکل از *کدام فیلد* است. خروجی خطای DRF در این حالت شبیه این است: `{"phone_number": ["Phone number is too short."]}`. دستور `assertIn` چک می‌کند که کلید `phone_number` داخل پاسخ سرور وجود داشته باشد.

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

مدل‌هایی که باید طراحی کنیم:

- `Category` (دسته‌بندی‌ها)
- `Brand` (برندها)
- `Product` (محصولات)
- `ProductImage` (گالری تصاویر)

مفاهیم کلیدی که با آن‌ها درگیر می‌شویم:

- **Slug:** برای ایجاد URLهای زیبا (SEO Friendly).
- **تصاویر:** آپلود و مدیریت فایل‌های مدیا (Pillow).
- **Inventory (موجودی):** مدیریت موجودی کالا.
- **Optimization (بهینه‌سازی دیتابیس):** جلوگیری از مشکل N+1 (ارسال ده‌ها کوئری اضافی به دیتابیس).

<aside>
📢

تصمیمات معماری برای Category (دسته‌بندی) و Brand (برند)

</aside>

**۱. مفهوم Slug (اسلاگ) چیست و چرا واجب است؟**
در فازهای قبلی (مثل Customer) ما با ID یا UUID کار می‌کردیم. مثلاً `api/customers/1/`.
اما برای محصولات و دسته‌بندی‌ها، URL باید برای موتورهای جستجو (SEO) و انسان‌ها خوانا باشد.
به جای: `acron.com/category/12/`
ما این را می‌خواهیم: `acron.com/category/smart-phones/`
به کلمه `smart-phones` می‌گویند **Slug**. ما در تمام مدل‌های این فاز به فیلد Slug نیاز داریم.

**۲. دسته‌بندی‌های تو در تو (Nested Categories)**
در یک فروشگاه واقعی، ما "کالای دیجیتال" داریم، زیرمجموعه آن "موبایل" است و زیرمجموعه آن "گوشی اپل".
برای پیاده‌سازی این ساختار درختی، مدل `Category` باید بتواند به **خودش** اشاره کند (Self-referential ForeignKey).

**۳. نیاز به تصاویر**
چون دسته‌بندی‌ها، برندها و محصولات نیاز به عکس دارند، جنگو برای فیلد تصویر (`ImageField`) به یک کتابخانه پردازش تصویر در پایتون به نام `Pillow` نیاز دارد.

<aside>
📢

شروع کدنویسی فاز ۴

</aside>

> **35- نصب کتابخانه مدیریت تصاویر (Pillow):**
در ترمینال (در حالی که محیط مجازی فعال است) دستور زیر را وارد کنید:
> 
> 
> ```python
> pipenv install pillow
> ```
> 

*چرا این کار را کردیم؟* 

جنگو بدون این کتابخانه اجازه استفاده از `models.ImageField` را نمی‌دهد و خطا پرتاب می‌کند، زیرا برای اعتبارسنجی اینکه آیا فایل آپلود شده واقعاً یک عکس است یا یک فایل مخرب، به موتور پردازشی `Pillow` متکی است.

> **36- فعال‌سازی اپلیکیشن در `base.py`:**
فایل `config/settings/base.py` را باز کنید و اپلیکیشن `products` را از کامنت خارج کنید:
> 
> 
> ```python
> INSTALLED_APPS = [
>     # ...
>     'apps.accounts',
>     'apps.customers',
>     'apps.products', # **این خط از کامنت خارج شود**
> ]
> ```
> 

> **37-** ساخت مدل‌های `Category` و `Brand`:
> 
> 
> فایل apps/products/models.py
> 
> را باز کنید و کدهای زیر را بادقت بنویسید (خط به خط را در ادامه کالبدشکافی می‌کنیم):
> 
> ```python
> from django.db import models
> 
> class Category(models.Model):
>     # دسته‌بندی والد (برای ساختار درختی)
>     parent = models.ForeignKey(
>         'self', 
>         on_delete=models.PROTECT, 
>         null=True, 
>         blank=True, 
>         related_name='children'
>     )
>     
>     name = models.CharField(max_length=255)
>     
>     # اسلاگ برای URLهای سئو-محور
>     slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
>     
>     description = models.TextField(blank=True)
>     
>     # تصویر دسته‌بندی
>     image = models.ImageField(upload_to='categories/%Y/%m/', blank=True, null=True)
> 
>     class Meta:
>         verbose_name_plural = 'Categories'
> 
>     def __str__(self):
>         return self.name
> 
> class Brand(models.Model):
>     name = models.CharField(max_length=255)
>     slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
>     image = models.ImageField(upload_to='brands/%Y/%m/', blank=True, null=True)
> 
>     **def __str__(self):**
>         return self.name
> ```
> 

<aside>
📢

کالبدشکافی دقیق کدها (بدون Vibe Coding)

</aside>

- **`parent = models.ForeignKey('self', ...)`:**
کلمه `'self'` به جنگو می‌گوید که این دسته‌بندی به یک دسته‌بندی دیگر در **همین جدول** متصل است. `null=True, blank=True` یعنی اگر دسته‌بندی والد نداشت (مثل خود "کالای دیجیتال" که بالاترین سطح است)، می‌تواند خالی بماند.
- **`on_delete=models.PROTECT` در parent:**
چرا CASCADE نگذاشتیم؟ اگر CASCADE بود، ادمین با حذف کردن دسته‌بندی "کالای دیجیتال"، اشتباهاً تمام زیرمجموعه‌های آن (موبایل، لپ‌تاپ و...) را هم پودر می‌کرد! `PROTECT` باعث می‌شود جنگو بگوید: "تا زمانی که این دسته، زیرمجموعه دارد، اجازه حذف آن را ندارید."
- **`related_name='children'`:**
این یعنی اگر من یک دسته والد باشم (مثلاً موبایل)، با دستور `category.children.all()` می‌توانم تمام زیرمجموعه‌هایم (سامسونگ، اپل، شیائومی) را استخراج کنم.
- **`allow_unicode=True` در SlugField:**
بسیار مهم برای سایت‌های ایرانی! به صورت پیش‌فرض، SlugField فقط حروف انگلیسی را قبول می‌کند. وقتی این پارامتر را می‌دهیم، می‌توانیم اسلاگ فارسی داشته باشیم (مثلاً: `acron.com/category/گوشی-موبایل/`).
- **`upload_to='categories/%Y/%m/'`:**
وقتی عکسی آپلود می‌شود، جنگو همه را در یک پوشه نمی‌ریزد. این پارامتر به جنگو می‌گوید بر اساس سال (`%Y`) و ماه (`%m`) پوشه‌بندی کند (مثلاً `categories/2026/07/`). این کار باعث می‌شود در آینده که هزاران عکس داشتید، سرور لینوکس شما در پیدا کردن فایل‌ها کُند نشود.
- **`verbose_name_plural = 'Categories'`:**
جنگو به صورت پیش‌فرض یک `s` به انتهای نام مدل‌ها در پنل ادمین اضافه می‌کند. اگر این خط را ننویسیم، در پنل ادمین می‌نویسد `Categorys` که از نظر املای انگلیسی غلط است. با این خط آن را اصلاح کردیم.

---

حالا که کدهای مدل `Category` و `Brand` را نوشتیم، دیتابیس ما هنوز از وجود این جداول بی‌خبر است. 

قدم بعدی ما دو بخش دارد: 

ابتدا این تغییرات را به دیتابیس MySQL تزریق می‌کنیم و سپس آن‌ها را به پنل ادمین جنگو متصل می‌کنیم تا بتوانیم اولین دسته‌بندی‌ها و برندها را بسازیم.

<aside>
📢

قدم اول: انتقال مدل‌ها به دیتابیس (Migration Lifecycle)

</aside>

زمانی که ما یک مدل پایتونی می‌نویسیم، دیتابیس (MySQL) مستقیماً آن را نمی‌فهمد. ما باید از سیستم اسمارتِ Migration در جنگو استفاده کنیم تا این کدهای پایتون را به دستورات SQL (مثل `CREATE TABLE`) تبدیل کند.

> **38- اجرای کامندهای ساخت و اعمال ترنزکشن‌ها در ترمینال:**
> 
> 
> ابتدا مطمئن شوید در محیط مجازی (`pipenv shell`) هستید، سپس دستور زیر را بزنید:
> 
> ```bash
> python manage.py makemigrations products
> ```
> 

نتیجه شبیه زیر در ترمینال خواهد بود

```bash
$ python manage.py makemigrations products
Migrations for 'products':
  apps\products\migrations\0001_initial.py
    + Create model Brand
    + Create model Category
```

<aside>
📢

**پشت صحنه چه رخ داد؟** 

</aside>

جنگو مدل‌های اپلیکیشن `products` را بررسی کرد و یک فایل جدید به نام `0001_initial.py` در پوشه `apps/products/migrations/` ساخت. 

این فایل صرفاً یک «نقشه ساخت» یا Blueprint به زبان پایتون است و هنوز تاثیری روی دیتابیس نگذاشته است.

> 39- حالا برای اعمال واقعی این نقشه روی MySQL، دستور زیر را اجرا کنید:
> 
> 
> ```python
> python manage.py migrate
> ```
> 

نتیجه شبیه زیر خواهد بود:

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, auth, contenttypes, customers, products, sessions
Running migrations:
  Applying products.0001_initial... OK
```

**پشت صحنه چه رخ داد؟** جنگو نقشه پایتونی را خواند، آن را به دستورات SQL تبدیل کرد و جداول `products_category` و `products_brand` را در دیتابیس `acron` ایجاد کرد. اگر خروجی `Applying products.0001_initial... OK` را دیدید، یعنی همه چیز با موفقیت انجام شده است.

<aside>
📢

این قسمت اختیاری است و مخصوص تست های خودکار گیت هاب است

</aside>

> 40- مجددا داخل ترمینال این دستور رو بزن و داخل گیت هاب ارسال کن
> 
> 
> ```python
> pipenv requirements > requirements.txt
> ```
> 
> نتیجه تا اینجا شبیه زیر خواهد بود: requirements.txt
> 
> ```python
> -i https://pypi.org/simple
> asgiref==3.11.1; python_version >= '3.9'
> django==6.0.6; python_version >= '3.12'
> djangorestframework==3.17.1; python_version >= '3.10'
> djangorestframework-simplejwt==5.5.1; python_version >= '3.9'
> mysqlclient==2.2.8; python_version >= '3.10'
> pillow==12.3.0; python_version >= '3.10'
> pyjwt==2.13.0; python_version >= '3.9'
> sqlparse==0.5.5; python_version >= '3.8'
> tzdata==2026.2; python_version >= '2'
> ```
> 

<aside>
📢

قدم دوم: مدیریت در پنل ادمین و جادوی خودکارسازی اسلاگ (Slug)

</aside>

اگر الان به پنل ادمین جنگو (`/admin/`) بروید، اثری از دسته‌بندی‌ها و برندها نمی‌بینید. 
باید آن‌ها را ریجستر (ثبت) کنیم. 
اما می‌خواهیم یک کار حرفه‌ای انجام دهیم؛ 
ادمین سایت نباید مجبور باشد خودش دستی اسلاگ بنویسد! 
ما کاری می‌کنیم که وقتی ادمین نام دسته‌بندی را تایپ می‌کند، جنگو به صورت خودکار اسلاگ آن را بسازد.

> 41- **فایل `apps/products/admin.py` را باز کنید و کدهای زیر را بنویسید:**
> 
> 
> Python
> 
> ```python
> from django.contrib import admin
> from .models import Category, Brand
> 
> @admin.register(Category)
> class CategoryAdmin(admin.ModelAdmin):
>     # ۱. مشخص کردن ستون‌هایی که در لیست ادمین نمایش داده می‌شوند
>     list_display = ['name', 'slug', 'parent']
> 
>     # ۲. جادوی پر شدن خودکار اسلاگ بر اساس نام
>     prepopulated_fields = {'slug': ('name',)}
> 
> @admin.register(Brand)
> class BrandAdmin(admin.ModelAdmin):
>     list_display = ['name', 'slug']
>     prepopulated_fields = {'slug': ('name',)}
> ```
> 

<aside>
📢

کالبدشکافی دقیق کدهای ادمین (بدون Vibe Coding)

</aside>

- **`@admin.register(Category)`**:
این یک دکوراتور (Decorator) پایتونی است. به زبان ساده به جنگو می‌گوید: «کلاس `CategoryAdmin` را به عنوان تنظیمات مدیریتیِ مدل `Category` در نظر بگیر و آن را در ادمین ثبت کن.»
- **`list_display`**:
به صورت پیش‌فرض، جنگو در لیست مدل‌ها فقط خروجی متد `__str__` را نشان می‌دهد. با این آپشن، ما یک جدول منظم می‌سازیم که ستون‌های نام، اسلاگ و والد را مجزا نمایش دهد تا پنل ادمین خواناتر شود.
- **`prepopulated_fields = {'slug': ('name',)}`**:
این مهم‌ترین بخش است! این تاپل به جنگو دستور می‌دهد که در صفحه ساختِ دسته‌بندی یا برند، یک جاوااسکریپت (JS) پشت صحنه اجرا کند. وقتی ادمین در فیلد `name` می‌نویسد "کالای دیجیتال"، جنگو به صورت خودکار و زنده فیلد `slug` را با متن "کالای-دیجیتال" پر می‌کند. از آنجا که ما در مدل قبلی `allow_unicode=True` گذاشته بودیم، این قابلیت به شکل بی‌نظیری با کلمات فارسی هم کار خواهد کرد.

<aside>
📢

تست و مشاهده نتیجه

</aside>

حالا سرور پروژه را روشن کنید:

```bash
python manage.py runserver
```

به آدرس `http://127.0.0.1:8000/admin/` بروید و با سوپریوزری که در فاز ۱ ساختید وارد شوید.
وارد بخش **Categories** شوید و روی **Add Category** کلیک کنید.

تلاش کنید یک دسته‌بندی فارسی (مثلاً: لپ تاپ و تبلت) بسازید و ببینید چطور فیلد اسلاگ به صورت خودکار پر می‌شود. 
یک بار هم یک دسته‌بندی والد بسازید و در دکمه بعدی، دسته‌بندی جدیدی بسازید و والد آن را روی دسته‌بندی قبلی تنظیم کنید تا ساختار درختی را به چشم ببینید.

<aside>
📢

**ساخت Product Model**

</aside>

<aside>
📢

بررسی و تصمیمات معماری (Architecture Design)

</aside>

1. **تصویر اصلی محصول:** چون هر محصول **دقیقاً یک** تصویر اصلی دارد، منطقی‌ترین کار این است که فیلد `main_image` را مستقیماً داخل خود مدل `Product` قرار دهیم.
2.  **۱۰ تصویر/ویدیوی فرعی (گالری مالتی‌مدیا):** از آنجایی که تعداد این فایل‌ها متغیر است (بین ۰ تا ۱۰ عدد) و هر فایل می‌تواند تصویر یا ویدیو باشد، نباید ۱۰ فیلد مجزا در مدل محصول بسازیم (این یک اشتباه رایج و ضد الگو است). راهکار اصولی، ایجاد یک مدل مجزا به نام `ProductMedia` است که با یک رابطه یک‌به‌چند (`ForeignKey`) به محصول متصل می‌شود.
3.  **تشخیص طول زمان ویدیو:** برای اینکه بفهمیم ویدیو چند ثانیه است، پایتون به صورت پیش‌فرض ابزاری ندارد. ما باید یک کتابخانه سبک برای پردازش ویدیو به نام `opencv-python` نصب کنیم تا بتواند متا‌دیتای ویدیو را بخواند و مدت زمان آن را به ثانیه به ما بدهد.

<aside>
📢

قدم اول: نصب ابزار پردازش ویدیو

</aside>

> 42- در ترمینال خود دستور زیر را وارد کنید تا کتابخانه مورد نیاز برای سنجش زمان ویدیو نصب شود:
> 
> 
> ```
> pipenv install opencv-python
> ```
> 

<aside>
📢

قدم دوم: نوشتن ولیدیتورها و مدل‌ها

</aside>

> 43- فایل `apps/products/models.py` را باز کنید. 
کدهای زیر را جایگزین کنید تا قدم به قدم آن‌ها را کالبدشکافی کنیم:
> 
> 
> ```bash
> import cv2
> from django.db import models
> from django.core.exceptions import ValidationError
> 
> # ۱. ساخت ولیدیتور سفارشی برای فایل‌های فرعی (حجم و زمان ویدیو)
> def validate_media_file(file):
>     # الف) بررسی حجم فایل (400 مگابایت به بایت)
>     max_size_mb = 400
>     max_size_bytes = max_size_mb * 1024 * 1024
>     if file.size > max_size_bytes:
>         raise ValidationError(f"حجم فایل نمی‌تواند بیشتر از {max_size_mb} مگابایت باشد.")
> 
>     # ب) بررسی مدت زمان ویدیو (اگر فایل ویدیو بود)
>     file_name = file.name.lower()
>     if file_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):
>         # باز کردن موقت فایل ویدیو با OpenCV برای خواندن فریم‌ها
>         video = cv2.VideoCapture(file.temporary_file_path())
>         
>         # به دست آوردن تعداد کل فریم‌ها و نرخ فریم (FPS)
>         frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
>         fps = video.get(cv2.CAP_PROP_FPS)
>         
>         # محاسبه زمان به ثانیه (اگر fps صفر نباشد)
>         if fps > 0:
>             duration_seconds = frames / fps
>             if duration_seconds > 120: # 2 دقیقه = 120 ثانیه
>                 raise ValidationError("مدت زمان ویدیو نمی‌تواند بیشتر از ۲ دقیقه باشد.")
>         video.release()
> 
> class Category(models.Model):
>     # کدهای قبلی دسته‌بندی بدون تغییر اینجا بمانند
>     parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
>     name = models.CharField(max_length=255)
>     slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
>     description = models.TextField(blank=True)
>     image = models.ImageField(upload_to='categories/%Y/%m/', blank=True, null=True)
> 
>     class Meta:
>         verbose_name_plural = 'Categories'
> 
>     def __str__(self):
>         return self.name
> 
> class Brand(models.Model):
>     # کدهای قبلی برند بدون تغییر اینجا بمانند
>     name = models.CharField(max_length=255)
>     slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
>     image = models.ImageField(upload_to='brands/%Y/%m/', blank=True, null=True)
> 
>     def __str__(self):
>         return self.name
> 
> # ۲. ساخت مدل اصلی محصول (Product)
> class Product(models.Model):
>     category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
>     brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
>     name = models.CharField(max_length=255)
>     slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
>     description = models.TextField()
>     price = models.DecimalField(max_digits=10, decimal_places=2) # استفاده از Decimal برای قیمت‌ها الزامی است
>     inventory = models.PositiveIntegerField(default=0) # موجودی کالا نباید منفی باشد
>     
>     # تصویر اصلی محصول (اجباری)
>     main_image = models.ImageField(upload_to='products/main/%Y/%m/')
>     
>     created_at = models.DateTimeField(auto_now_add=True)
>     updated_at = models.DateTimeField(auto_now=True)
> 
>     def __str__(self):
>         return self.name
> 
> # ۳. ساخت مدل گالری فرعی (تصاویر و ویدیوها)
> class ProductMedia(models.Model):
>     MEDIA_TYPES = (
>         ('image', 'Image'),
>         ('video', 'Video'),
>     )
> 
>     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media_gallery')
>     media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
>     
>     # استفاده از FileField چون هم عکس را قبول می‌کند و هم ویدیو را
>     file = models.FileField(upload_to='products/gallery/%Y/%m/', validators=[validate_media_file])
> 
>     # متد clean برای محدود کردن تعداد کل مدیاهای یک محصول به حداکثر ۱۰ عدد
>     def clean(self):
>         super().clean()
>         # شمارش مدیاهای فعلی این محصول در دیتابیس (بدون احتساب رکوردی که الان دارد ذخیره می‌شود)
>         if self.product_id:
>             existing_media_count = ProductMedia.objects.filter(product=self.product).exclude(pk=self.pk).count()
>             if existing_media_count >= 10:
>                 raise ValidationError("شما نمی‌توانید بیشتر از ۱۰ فایل فرعی (تصویر/ویدیو) برای یک محصول آپلود کنید.")
> 
>     def save(self, *args, **kwargs):
>         # قبل از ذخیره نهایی در دیتابیس، حتماً متد clean را صدا می‌زنیم تا ولیدیشن‌ها اجرا شوند
>         self.full_clean()
>         super().save(*args, **kwargs)
> ```
> 

<aside>
📢

کالبدشکافی خط به خط کدهای جدید (بدون Vibe Coding)

</aside>

- **تابع `validate_media_file`:**
جنگو به ما اجازه می‌دهد توابعی بنویسیم که فایل ورودی را قبل از ذخیره شدن بازرسی کنند.
    - `file.size` حجم فایل را به بایت برمی‌گرداند. با ضرب کردن `400 * 1024 * 1024` آن را به بایت تبدیل کردیم تا با حجم واقعی فایل مقایسه شود.
    - `file.temporary_file_path()`: وقتی فایلی در جنگو آپلود می‌شود و حجمش زیاد است، جنگو آن را در پوشه موقت سیستم‌عامل (مثل `/tmp`) ذخیره می‌کند. ما با این متد، آدرس فیزیکی فایل را به کتابخانه `cv2` (OpenCV) می‌دهیم.
    - فرمول `frames / fps`: ویدیوها مجموعه‌ای از تصاویر پشت سر هم (فریم) هستند. اگر تعداد کل فریم‌ها را بر تعداد فریم در ثانیه (FPS) تقسیم کنیم، مدت زمان دقیق ویدیو به ثانیه به دست می‌آید. ما چک کردیم که این عدد بزرگتر از ۱۲۰ ثانیه (۲ دقیقه) نباشد.
- **فیلد `price = models.DecimalField(...)`:**
توسعه‌دهندگان تازه‌کار برای قیمت از `FloatField` استفاده می‌کنند که اشتباه است. فلوت‌ها در محاسبات ریاضی دیتابیس دچار خطای گردکردن اعشار (Rounding Errors) می‌شوند. برای سیستم‌های مالی و فروشگاهی، همیشه باید از `DecimalField` استفاده کرد.
- **مدل `ProductMedia` و فیلد `file`:**
چون قرار است هم عکس آپلود شود هم ویدیو، نمی‌توانستیم از `ImageField` استفاده کنیم، زیرا اِمیج‌فیلد ساختار ویدیو را بلاک می‌کند. بنابراین از `models.FileField` استفاده کردیم و آرگومان `validators=[validate_media_file]` را به آن پاس دادیم تا قوانین حجم و زمان روی آن اعمال شود.
- **متد `clean` در `ProductMedia`:**
این یک متد داخلی جنگو است که برای اعتبارسنجی‌های چند فیلدی یا منطقی استفاده می‌شود. ما با دستور `ProductMedia.objects.filter(product=self.product).count()` بررسی می‌کنیم که این محصول در حال حاضر چند عکس یا ویدیوی فرعی دارد. اگر تعداد ۱۰ یا بیشتر بود، با پرتاب `ValidationError` جلوی ذخیره‌سازی را می‌گیریم. دستور `.exclude(pk=self.pk)` برای این است که اگر ادمین خواست یک عکسِ از قبل آپلود شده را ویرایش کند، خودش را جزو آن ۱۰ تا حساب نکند و خطا ندهد.
- **متد `save` و دستور `self.full_clean()`:**
در جنگو، وقتی رکوردی از طریق پنل ادمین ثبت می‌شود، متد `clean` خودبه‌خود اجرا می‌شود. اما اگر بعداً کدی بنویسیم که از طریق API (مثلاً DRF) دیتا ذخیره کند، جنگو متد `clean` مدل را به صورت خودکار اجرا نمی‌کند! برای حل این گپ امنیتی، متد `save` را اورراید کردیم و داخلش `self.full_clean()` را صدا زدیم تا مطمئن شویم تحت هر شرایطی (چه ادمین، چه API) این ولیدیشن‌ها اجرا می‌شوند.

<aside>
📢

چرا از OneToOneField استفاده نکردیم؟

</aside>

بیایید این چالش را کاملاً کالبدشکافی کنیم تا تفاوت عمیق بین `OneToOneField` و `ForeignKey` را متوجه شوید و ببینید چرا استفاده از `OneToOneField` در اینجا باعث **خراب شدن سیستم گالری** می‌شد.
****

<aside>
📢

**تفاوت ساختاری در دیتابیس (SQL چیست؟)**

</aside>

وقتی ما در جنگو مدل می‌نویسیم، این مدل‌ها به جداول دیتابیس تبدیل می‌شوند. تفاوت این دو فیلد در سطح دیتابیس به این صورت است:

1. **اگر از `OneToOneField` استفاده می‌کردیم (رابطه یک‌به‌یک):**
در دیتابیس، جنگو ستون `product_id` را در جدول مِدیا می‌سازد و روی آن یک قفل به نام **`UNIQUE` (یکتا)** می‌گذارد.
معنی یکتا بودن چیست؟ 
یعنی در کل جدول مدیا، فقط و فقط **یک ردیف** می‌تواند وجود داشته باشد که آی‌دی آن محصول (مثلاً محصول شماره ۵) در آن ثبت شده باشد.

**نتیجه عملی:** 
شما برای لپ‌تاپ ایسوس (آی‌دی ۵) یک عکس فرعی آپلود می‌کنید. رکورد با موفقیت ذخیره می‌شود. حالا می‌خواهید عکس فرعی دوم یا یک ویدیو برای همان لپ‌تاپ آپلود کنید؛ دیتابیس MySQL فوراً خطا می‌دهد: `Duplicate entry '5' for key 'product_id'`!

**خلاصه:** 
با `OneToOneField` هر محصول فقط و فقط می‌توانست **یک دانه** فایل فرعی داشته باشد، نه ۱۰ تا!
****
2. **چرا از `ForeignKey` استفاده کردیم (رابطه چند‌به‌یک):**
رابطه چند‌به‌یک (Many-to-One) یعنی **چندین** ردیف در جدول مدیا می‌توانند به **یک** محصول اشاره کنند. در این حالت ستون `product_id` در جدول مدیا دیگر `UNIQUE` نیست.

به این جدول فرضی دیتابیس (جدول `ProductMedia`) نگاه کنید:

| **id** | **product_id (Foreign Key)** | **media_type** | **file_path** |
| --- | --- | --- | --- |
| 1 | **5** (لپ‌تاپ ایسوس) | image | gallery/pic1.jpg |
| 2 | **5** (لپ‌تاپ ایسوس) | video | gallery/vid1.mp4 |
| 3 | **5** (لپ‌تاپ ایسوس) | image | gallery/pic2.jpg |
| 4 | **8** (گوشی آیفون) | image | gallery/iphone.jpg |

همانطور که می‌بینید، محصول شماره ۵ توانسته ۳ ردیف مختلف (دو عکس و یک ویدیو) در گالری داشته باشد. این دقیقاً همان چیزی است که ما می‌خواهیم؛ 

یعنی یک محصول بتواند یک **گالری** (مجموعه‌ای از فایل‌ها) داشته باشد.

<aside>
📢

**پس چطور محدودیت "حداکثر ۱۰ فایل" را اعمال کردیم؟**

</aside>

اگر دیتابیس به لطف `ForeignKey` اجازه می‌دهد که بی‌نهایت عکس برای یک محصول ثبت شود، پس چطور جلوی ادمین را بگیریم که ۱۰۰ تا عکس آپلود نکند؟
اینجا کدهای پایتون و جنگو به کمک ما می‌آیند. 

ما این محدودیت را در سطح **Business Logic (منطق کسب‌وکار)** اعمال کردیم، نه در سطح ساختار سخت‌گیرانه دیتابیس.

```bash
existing_media_count = ProductMedia.objects.filter(product=self.product).count()
if existing_media_count >= 10:
    raise ValidationError("شما نمی‌توانید بیشتر از ۱۰ فایل فرعی آپلود کنید.")
```

**کالبدشکافی منطق بالا:**
هر بار که ادمین می‌خواهد عکس جدیدی آپلود کند، این کد ابتدا در دیتابیس جستجو می‌کند (`filter`) و می‌شمارد (`count`) که این محصول تا الان چندتا عکس دارد.
اگر تعداد آن‌ها ۹ تا بود، اجازه می‌دهد عکس دهم ذخیره شود. اما اگر تعداد ۱۰ تا بود، پایتون ترمز را می‌کشد و با پرتاب `ValidationError` اجازه نمی‌دهد درخواست به دیتابیس برسد.

<aside>
📢

خلاصه و جمع‌بندی:

</aside>

- برای چیزهایی که **دقیقاً یکی** هستند (مثل تصویر اصلی محصول)، فیلد را مستقیم در خود محصول می‌گذاریم (که عملاً حکم یک‌به‌یک دارد).
- برای چیزهایی که **لیست یا گالری** هستند (مثل تصاویر فرعی)، از `ForeignKey` استفاده می‌کنیم تا اجازه ثبت چند ردیف داده شود.
- برای اعمال محدودیت روی تعداد لیست، از متدهای معتبرسازی مثل `clean` در جنگو استفاده می‌کنیم.

<aside>
📢

حالا که این منطق قدرتمند را پیاده کردیم، باید تغییرات را به دیتابیس اعلام کنیم. 

</aside>

> 44- در ترمینال دستورات زیر را اجرا کنید
> 
> 
> ```bash
> python manage.py makemigrations
> python manage.py migrate
> ```
> 

نتیجه شبیه زیر است:

```bash
$ python manage.py makemigrations products
Migrations for 'products':
  apps\products\migrations\0002_product_productmedia.py
    + Create model Product
    + Create model ProductMedia
    
$ python manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, auth, contenttypes, customers, products, sessions
Running migrations:
  Applying products.0002_product_productmedia... OK
```

<aside>
📢

متصل کردن این ساختار به پنل ادمین

</aside>

در حالت عادی، اگر بخواهیم برای یک محصول عکس فرعی آپلود کنیم، ادمین باید ابتدا به بخش `ProductMedia` برود، محصول را انتخاب کند، عکس را آپلود کند و ذخیره کند. این کار برای ۱۰ عکس یعنی ۱۰ بار رفت‌وآمد بین صفحات مختلف که اصلاً با معیارهای یک سیستم حرفه‌ای سازگار نیست.

جنگو برای این حل این مشکل قابلیتی به نام **Inline Admin** دارد. با این قابلیت، گالری تصاویر دقیقاً در زیر صفحه ساخت خود محصول باز می‌شود تا ادمین همه‌چیز را در یک صفحه مدیریت کند.

<aside>
📢

پیاده‌سازی مدیریت یکپارچه محصول و گالری

</aside>

> 45-  فایل `apps/products/admin.py` را باز کنید و کدهای زیر را به انتهای آن اضافه کنید:
> 
> 
> ```python
> from django.contrib import admin
> from .models import Category, Brand, Product, ProductMedia # مدل‌های جدید اضافه شدند
> 
> # کدهای قبلی مربوط به CategoryAdmin و BrandAdmin بدون تغییر اینجا بمانند...
> 
> # ۱. ساخت کلاس اینلاین برای گالری فرعی
> class ProductMediaInline(admin.TabularInline):
>     model = ProductMedia
>     extra = 1          # تعداد ردیف‌های خالی که به صورت پیش‌فرض نمایش داده می‌شود
>     max_num = 10       # قفل کردن فرانت‌اند ادمین روی حداکثر ۱۰ فایل فرعی
> 
> # ۲. ساخت کلاس مدیریت اصلی محصول
> @admin.register(Product)
> class ProductAdmin(admin.ModelAdmin):
>     # الف) ستون‌های نمایشی در جدول لیست محصولات
>     list_display = ['name', 'brand', 'category', 'price', 'inventory', 'created_at']
>     
>     # ب) باکس فیلتر در سمت راست پنل ادمین
>     list_filter = ['category', 'brand', 'created_at']
>     
>     # ج) باکس جستجوی پیشرفته
>     search_fields = ['name', 'description']
>     
>     # د) پر شدن خودکار اسلاگ محصول بر اساس نام آن
>     prepopulated_fields = {'slug': ('name',)}
>     
>     # هـ) تزریق گالری فرعی به انتهای صفحه محصول
>     inlines = [ProductMediaInline]
> ```
> 

<aside>
📢

کالبدشکافی خط به خط کدهای ادمین (بدون Vibe Coding)

</aside>

- **`class ProductMediaInline(admin.TabularInline)`:**
ما در جنگو دو نوع اینلاین داریم: `TabularInline` (جدولی) و `StackedInline` (پشته‌ای). مدل جدولی فیلدها را در یک ردیف افقی و بسیار فشرده نشان می‌دهد که برای آپلود عکس و ویدیو عالی است و صفحه را بیش از حد طولانی نمی‌کند.
- **`model = ProductMedia`:**
به جنگو می‌گوییم این ردیف‌های درون‌برنامه‌ای، قرار است داده‌های جدول `ProductMedia` را پر کنند. جنگو خودش به صورت هوشمند از روی رابطه `ForeignKey` می‌فهمد که این مِدیاها چطور به محصول متصل می‌شوند.
- **`extra = 1`:**
وقتی ادمین صفحه محصول را باز می‌کند، جنگو به طور پیش‌فرض ۱ ردیف خالی برای آپلود فایل جدید به او نشان می‌دهد. ادمین می‌تواند با دکمه Add another ردیف‌های بیشتری باز کند.
- **`max_num = 10`:**
این یک لایه امنیتی در فرانت‌اند پنل ادمین است. با این دستور، جنگو بعد از اینکه ادمین ۱۰ فایل فرعی را آپلود کرد، دکمه Add another را مخفی می‌کند تا ادمین اصلاً نتواند دکمه اضافه کردن را کلیک کند (یادتان هست که در مرحله قبل، لایه امنیتی بک‌اند را هم با متد `clean` در مدل قفل کرده بودیم؟ حالا سیستم از هر دو طرف کاملاً امن است).
- **`list_filter = [...]`:**
در پروژه‌های بزرگ با هزاران محصول، ادمین باید بتواند سریعاً محصولات را فیلتر کند. این دستور یک سایدبار هوشمند در سمت راست ادمین می‌سازد تا محصولات بر اساس برند یا دسته‌بندی خاص جداسازی شوند.
- **`search_fields = [...]`:**
این فیلد یک باکس سرچ به بالای صفحه اضافه می‌کند. وقتی ادمین متنی را سرچ می‌کند، جنگو پشت صحنه یک کوئری SQL با دستور `LIKE` روی فیلدهای `name` و `description` می‌زند تا کالا را پیدا کند.

<aside>
📢

تست سناریوهای واقعی در پنل ادمین

</aside>

حالا سرور پروژه را روشن کنید (`python manage.py runserver`) و به صفحه ادمین محصول بروید: `http://127.0.0.1:8000/admin/products/product/add/`

**سه سناریوی زیر را برای چالش کشیدن کدهایتان تست کنید:**

1. **تست اسلاگ و تصویر اصلی:** نام یک محصول را بنویسید (مثلاً: گوشی سامسونگ S24). ببینید چطور اسلاگ فارسی پر می‌شود. یک تصویر اصلی برای آن آپلود کنید.
2. **تست گالری فرعی:** در پایین صفحه، بخش گالری را می‌بینید. سعی کنید چند تصویر فرعی و یک ویدیوی کوتاه آپلود کنید و دکمه Save را بزنید. همه‌چیز باید بدون مشکل ذخیره شود.
3. **تست ولیدیتور (بسیار مهم):** یک ویدیوی طولانی (بالای ۲ دقیقه) یا یک فایل حجیم انتخاب کنید و سعی کنید محصول را ذخیره کنید. دیتابیس نباید رکورد را ثبت کند و جنگو باید دقیقاً بالای همان ردیف گالری، ارور فارسی که در متد `validate_media_file` نوشتیم را به ادمین نمایش دهد.

<aside>
📢

ارور  `'FieldFile' object has no attribute 'temporary_file_path'`
**AttributeError        at /admin/products/product/1….**

</aside>

چرا این خطا (AttributeError) رخ داد؟

شما سعی کردید از متد `temporary_file_path()` استفاده کنید تا آدرس فایل ویدیو را به OpenCV بدهید. اما جنگو در مدیریت فایل‌های آپلودی رفتار دوگانه‌ای دارد:

1. **فایل‌های کوچک (زیر ۲.۵ مگابایت):** جنگو برای سرعت بیشتر، این فایل‌ها را اصلاً روی هارد دیسک ذخیره نمی‌کند! بلکه آن‌ها را مستقیماً در حافظه رم (RAM) با کلاسی به نام `InMemoryUploadedFile` نگه می‌دارد. چون فایلی روی هارد نیست، طبیعتاً آدرس فیزیکی (Path) هم ندارد و متد `temporary_file_path` کار نمی‌کند.
2. **فایل‌های بزرگ (بالای ۲.۵ مگابایت):** جنگو این فایل‌ها را در پوشه موقت سیستم‌عامل با کلاسی به نام `TemporaryUploadedFile` ذخیره می‌کند. این فایل‌ها آدرس فیزیکی دارند.
3. **فایل‌های از قبل ذخیره شده:** اگر بخواهید محصولی را ویرایش کنید که از قبل ویدیویی دارد، جنگو یک شیء از نوع `FieldFile` به ولیدیتور می‌فرستد که آن هم متد `temporary_file_path` را ندارد.

از آنجا که کتابخانه `cv2` (OpenCV) فقط و فقط یک **آدرس فایل فیزیکی روی هارد** را می‌خواند و حافظه رم را نمی‌فهمد، سیستم کرش کرد.

<aside>
📢

راه حل معماری اصولی (استفاده از tempfile)

</aside>

برای حل این مشکل بدون اینکه به تنظیمات پایه جنگو دست بزنیم، باید یک فایل موقت فیزیکی روی سرور بسازیم، فایلِ جنگو (چه در رم باشد چه روی هارد) را تکه‌تکه (Chunk) داخل آن بنویسیم، آدرس آن را به OpenCV بدهیم و در نهایت آن فایل موقت را حذف کنیم.

> 46- فایل `apps/products/models.py` را باز کنید و تابع `validate_media_file` را به شکل زیر اصلاح کنید:
> 
> 
> ```python
> import cv2
> import os
> import tempfile # این کتابخانه استاندارد پایتون باید اضافه شود
> from django.db import models
> from django.core.exceptions import ValidationError
> 
> def validate_media_file(file):
>     # الف) بررسی حجم فایل (400 مگابایت به بایت)
>     max_size_mb = 400
>     max_size_bytes = max_size_mb * 1024 * 1024
>     if file.size > max_size_bytes:
>         raise ValidationError(f"حجم فایل نمی‌تواند بیشتر از {max_size_mb} مگابایت باشد.")
> 
>     # ب) بررسی مدت زمان ویدیو (اگر فایل ویدیو بود)
>     file_name = file.name.lower()
>     if file_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):
>         
>         # ۱. ساخت یک فایل موقت فیزیکی و امن روی سیستم‌عامل
>         with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
>             # ۲. خواندن فایل جنگو به صورت تکه‌تکه و نوشتن در فایل موقت
>             for chunk in file.chunks():
>                 temp_video.write(chunk)
>             temp_video_path = temp_video.name
> 
>         try:
>             # ۳. دادن آدرس فایل فیزیکی موقت به OpenCV
>             video = cv2.VideoCapture(temp_video_path)
>             
>             frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
>             fps = video.get(cv2.CAP_PROP_FPS)
>             
>             if fps > 0:
>                 duration_seconds = frames / fps
>                 if duration_seconds > 120:
>                     raise ValidationError("مدت زمان ویدیو نمی‌تواند بیشتر از ۲ دقیقه باشد.")
>         finally:
>             # ۴. پاکسازی (بسیار مهم): آزادسازی رم و حذف فایل موقت از روی هارد
>             if 'video' in locals():
>                 video.release()
>             if os.path.exists(temp_video_path):
>                 os.remove(temp_video_path)
> ```
> 

<aside>
📢

کالبدشکافی کدهای جدید

</aside>

- **`tempfile.NamedTemporaryFile`:** این ابزار درونی پایتون است. یک فایل فیزیکی کاملاً امن و یکتا روی هارد دیسک سرور می‌سازد. ما `delete=False` گذاشتیم تا فایل فوراً بسته نشود و بتوانیم آدرس آن (`temp_video.name`) را به OpenCV بدهیم.
- **`file.chunks()`:** ما کل فایل را یک‌جا در رم بارگذاری نمی‌کنیم (چون ممکن است ۴۰۰ مگابایت رم سرور را اشغال کند). با `chunks`، پایتون فایل را در بسته‌های کوچک (معمولاً ۶۴ کیلوبایتی) می‌خواند و در فایل موقت می‌نویسد. این کار برای جلوگیری از پر شدن حافظه (Memory Overflow) در پروداکشن الزامی است.
- **بلاک `try...finally`:** مهم‌ترین قانون در مدیریت فایل‌ها! اگر ویدیوی کاربر خراب باشد و OpenCV کرش کند، یا اگر خطای زمانِ بیش از ۲ دقیقه پرتاب شود (`raise ValidationError`)، اجرای کد متوقف می‌شود. بلاک `finally` تضمین می‌کند که **تحت هر شرایطی**، حتی اگر سرور خطا داد، فایل موقتی که ساختیم از روی هارد پاک شود تا هارد سرور به مرور زمان پر از ویدیوهای موقت نشود.

---

### چرا الان زمان مناسبی برای Swagger نیست؟

- **۱. کمبود نقطه‌های پایانی (Endpoints):** در حال حاضر، ما در کل پروژه فقط یک API واقعی داریم (همان `GET/PATCH /api/customers/me/` در فاز ۳). اگر الان ابزارهای OpenAPI (مثل `drf-spectacular` که استاندارد مدرن DRF است) را نصب کنیم، خروجی Swagger ما بسیار خالی و خسته‌کننده خواهد بود و نمی‌توانیم قدرت واقعی آن را ببینیم.
- **۲. از دست دادن تمرکز (Context Switching):** ما الان دقیقاً در قلب **Product Domain (فاز ۴)** هستیم. مدل‌ها را معماری کردیم، ولیدیتورهای پیچیده نوشتیم و ادمین را یکپارچه کردیم. اگر الان وارد تنظیمات زیرساختی (Infrastructure) مثل Swagger بشویم، تمرکزمان از روی منطق کسب‌وکار به هم می‌خورد.
- **۳. غول مرحله آخر محصولات (مشکل N+1):** ما هنوز Serializerها و Viewهای مربوط به محصولات را ننوشته‌ایم. در بخش نمایش محصولات، یک چالش وحشتناک به نام مشکل N+1 Query وجود دارد (وقتی یک کالا ۱۰ عکس دارد، دیتابیس برای هر عکس یک کوئری جداگانه می‌زند و سرور به شدت کُند می‌شود). حل این مشکل اولویت بسیار بالاتری نسبت به مستندسازی دارد.

<aside>
📢

در نقطه‌ای هستیم که مفاهیم پیشرفته‌ی جنگو و DRF خودشان را نشان می‌دهند.

</aside>

در این مرحله، هدف ما این است که دیتای محصول را به همراه **برند**، **دسته‌بندی** و **گالری تصاویرش** به یک JSON تمیز تبدیل کنیم. 
اما یک قانون مهم داریم: سریالایزر `Product` به سریالایزرهای دیگر وابسته است. 
یعنی قبل از اینکه بتوانیم محصول را JSON کنیم، باید به DRF یاد بدهیم که چطور یک "برند" یا "مدیا" را JSON کند.

<aside>
📢

قدم اول: ساخت Serializerهای پایه و Product Serializer

</aside>

> 47-  در مسیر `apps/products/` یک فایل جدید به نام `serializers.py` بسازید و کدهای زیر را بادقت وارد کنید:
> 
> 
> ```python
> from rest_framework import serializers
> from .models import Category, Brand, Product, ProductMedia
> 
> # ۱. سریالایزر دسته‌بندی
> class CategorySerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Category
>         fields = ['id', 'name', 'slug']
> 
> # ۲. سریالایزر برند
> class BrandSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Brand
>         fields = ['id', 'name', 'slug', 'image']
> 
> # ۳. سریالایزر گالری مدیا
> class ProductMediaSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = ProductMedia
>         fields = ['id', 'media_type', 'file']
> 
> # ۴. سریالایزر اصلی محصول (Master Serializer)
> class ProductSerializer(serializers.ModelSerializer):
>     # الف) Nested Serializers برای فیلدهای کلید خارجی (ForeignKey)
>     category = CategorySerializer(read_only=True)
>     brand = BrandSerializer(read_only=True)
>     
>     # ب) Nested Serializer برای رابطه معکوس (گالری)
>     media_gallery = ProductMediaSerializer(many=True, read_only=True)
> 
>     class Meta:
>         model = Product
>         fields = [
>             'id', 
>             'name', 
>             'slug', 
>             'description', 
>             'price', 
>             'inventory', 
>             'main_image',
>             'category', 
>             'brand', 
>             'media_gallery', # اضافه کردن گالری به خروجی نهایی
>             'created_at'
>         ]
>         
> ```
> 

<aside>
📢

کالبدشکافی خط به خط Serializerها (بدون Vibe Coding)

</aside>

- **چرا ۳ سریالایزر اول را ساختیم؟**
اگر در `ProductSerializer` فقط می‌نوشتیم `fields = ['category', 'brand']`، خروجی API فقط ID آن‌ها را برمی‌گرداند (مثلاً `"brand": 2`). اما در یک فروشگاه واقعی، فرانت‌اند به نام و اسلاگ برند هم نیاز دارد تا آن را نمایش دهد. با پاس دادن `CategorySerializer` و `BrandSerializer` به متغیرهای `category` و `brand`، ما به DRF می‌گوییم: "به جای ID، کل آبجکت برند را به صورت تو در تو (Nested) برگردان".
- **`media_gallery = ProductMediaSerializer(many=True, ...)`:**
    - کلمه `media_gallery`: یادتان هست در فایل `models.py` وقتی `ProductMedia` را می‌ساختیم، نوشتیم `related_name='media_gallery'`؟ اینجا دقیقاً باید از همان نام استفاده کنیم تا DRF بفهمد باید برود و فایل‌های فرعی این محصول را پیدا کند.
    - پارامتر `many=True`: این **حیاتی‌ترین** کلمه در این خط است. چون گالری یک رابطه "چند به یک" است (یک محصول، ۱۰ عکس)، DRF باید بداند که با یک لیست (List) از داده‌ها طرف است، نه یک آبجکت تکی. اگر `many=True` را نگذارید، سیستم کرش می‌کند.

### قدم دوم: غول مرحله آخر (مشکل N+1 در Views)

حالا که سریالایزر آماده است، باید View آن را بسازیم تا محصولات را به کاربر نمایش دهد (مثلاً در صفحه اصلی فروشگاه). اما اینجا یک تله بزرگ وجود دارد که برنامه‌نویسان تازه‌کار در آن می‌افتند: **مشکل N+1 Query**.

**مشکل N+1 چیست؟**
فرض کنید ۱۰ محصول در دیتابیس داریم. اگر در View فقط بنویسیم `Product.objects.all()`، جنگو ۱ کوئری می‌زند تا ۱۰ محصول را بیاورد.
سپس سریالایزر برای محصول اول می‌گوید: "من عکس‌های گالری‌ات را می‌خواهم!" -> جنگو ۱ کوئری دیگر می‌زند.
محصول دوم: "عکس‌های من؟" -> ۱ کوئری دیگر.
برای ۱۰ محصول، دیتابیس ۱۱ بار (۱ + ۱۰) درگیر می‌شود. حالا فرض کنید دیجی‌کالا در یک صفحه ۱۰۰ محصول با برند و دسته‌بندی و گالری لود کند... سرور با ۳۰۱ کوئری نابود می‌شود!

**راه‌حل معماری دیتابیس در جنگو:**

- `select_related`: برای روابط `ForeignKey` (مثل برند و دسته) استفاده می‌شود. جنگو در سطح دیتابیس یک `SQL JOIN` می‌زند و همه را در **همان ۱ کوئری اول** می‌آورد.
- `prefetch_related`: برای روابط معکوس و لیست‌ها (مثل گالری تصاویر) استفاده می‌شود. جنگو تمام گالری‌های مرتبط را فقط با **۱ کوئری اضافه** (با دستور `IN` در SQL) می‌آورد و در رم پایتون آن‌ها را به هم می‌چسباند.

> 48- در مسیر `apps/products/` فایل `views.py` را باز کنید (یا بسازید) و کدهای بهینه‌شده زیر را بنویسید:
> 
> 
> ```python
> from rest_framework.generics import ListAPIView
> from rest_framework.permissions import AllowAny
> from .models import Product
> from .serializers import ProductSerializer
> 
> class ProductListView(ListAPIView):
>     """
>     API دریافت لیست تمام محصولات فروشگاه
>     آزاد برای تمام کاربران (بدون نیاز به لاگین)
>     """
>     permission_classes = [AllowAny] # همه می‌توانند محصولات را ببینند
>     serializer_class = ProductSerializer
>     
>     # QuerySet کاملاً بهینه‌سازی شده برای جلوگیری از مشکل N+1
>     queryset = Product.objects.select_related(
>         'category', 
>         'brand'
>     ).prefetch_related(
>         'media_gallery'
>     ).all()
> ```
> 

### کالبدشکافی View

- **`ListAPIView`:** به جای اینکه خودمان به صورت دستی مثل فاز ۳ متد `get` بنویسیم و `Response` برگردانیم، از Generic View های آماده DRF استفاده کردیم. این کلاس به صورت خودکار کوئری‌ست را می‌گیرد، آن را به سریالایزر می‌دهد و در صورت تنظیم بودن Pagination (که در تنظیمات پایه انجام دادیم)، خروجی را صفحه‌بندی می‌کند.
- **`AllowAny`:** برعکس پروفایل مشتری (`IsAuthenticated`)، کاتالوگ محصولات باید برای عموم مردم و موتورهای جستجو (گوگل) باز باشد تا سئو سایت کار کند.
- **بهینه‌سازی Query:** با ترکیب `select_related` و `prefetch_related`، ما تعداد کوئری‌های دیتابیس را برای لود کردن ۱۰۰ محصول از **۳۰۱ کوئری به فقط ۲ کوئری** کاهش دادیم! این یعنی کد شما در سطح یک برنامه نویس سنیور و آماده برای ترافیک پروداکشن است.

<aside>
📢

قدم نهایی: اتصال به URL

</aside>

> 49- در مسیر `apps/products/` یک فایل به نام `urls.py` بسازید و مسیر زیر را تعریف کنید:
> 
> 
> ```python
> from django.urls import path
> from .views import ProductListView
> 
> urlpatterns = [
>     path('', ProductListView.as_view(), name='product-list'),
> ]
> ```
> 

> 50- **این URL را به روت اصلی API در فایل `apps/api/urls.py` متصل کنید:**
> 
> 
> فایل `apps/api/urls.py` را باز کنید و مسیر `products/` را به آن اضافه کنید:
> 
> ```python
> from django.urls import path
> from .views import ProductListView
> 
> urlpatterns = [
>     path('', ProductListView.as_view(), name='product-list'),
> ]
> ```
> 

حالا می‌توانید در Postman (بدون نیاز به توکن)، به آدرس `GET http://127.0.0.1:8000/api/products/` درخواست بزنید و محصولاتی که در پنل ادمین ساخته‌اید را با یک JSON بسیار زیبا، کامل (شامل برند و گالری) و دیتابیسی کاملاً بهینه‌شده مشاهده کنید.

| **ویژگی** | **select_related** | **prefetch_related** |
| --- | --- | --- |
| **نوع رابطه مناسب** | ForeignKey, OneToOne | ManyToMany, Reverse ForeignKey |
| **کارکرد در دیتابیس** | از طریق `SQL JOIN` | از طریق چند کوئری مجزا و فیلتر با `IN` |
| **تعداد کوئری‌ها** | همیشه **۱ کوئری** | **بیش از ۱ کوئری** (معمولاً ۲ کوئری) |
| **محل پردازش اتصال** | داخل خود دیتابیس (SQL) | داخل حافظه پایتون (Django ORM) |

> 51- داخل ترمینال این رو بنویس تا پکیچ django debug toolbar نصب بشه
> 
> 
> ```python
> pipenv install django-debug-toolbar
> ```
> 

> 51- داخل ترمینال این رو بنویس تا پکیچ django debug toolbar نصب بشه
> 
> 
> ```python
> pipenv install django-debug-toolbar
> ```
> 

> 52- داخل فایل [base.py](http://base.py) چک کن باشه
> 
> 
> ```python
> # Check for Prerequisites
> INSTALLED_APPS = [
>     # ...
>     "django.contrib.staticfiles",
>     # ...
> ]
> STATIC_URL = "static/"
> ```
> 

> 53- داخل فایل [base.py](http://base.py) اضافه کن
> 
> 
> ```python
> INTERNAL_IPS = [
>     # ...
>     "127.0.0.1",
>     # ...
> ]
> 
> INSTALLED_APPS = [
>     # ...
>     "debug_toolbar",
>     # ...
> ]
> 
> MIDDLEWARE = [
>     # ...
>     "debug_toolbar.middleware.DebugToolbarMiddleware",
>     # ...
> ]
> 
> ```
> 

> 54- داخل فایل config/urls.py اضافه کن
> 
> 
> ```python
> from django.urls import include, path
> from debug_toolbar.toolbar import debug_toolbar_urls
> 
> urlpatterns = [
>     # ... the rest of your URLconf goes here ...
> ] + debug_toolbar_urls()
> ```
> 

> 55- داخل فایل requirements.txt اضافه ش کن  و داخل گیت هاب push کن
> 
> 
> ```python
> pipenv requirements > requirements.txt
> ```
> 

> 56- برای تست کردن اپلیکیشن debug toolbar رو disable کن
**Disable the toolbar when running tests (optional)**
> 
> 
> ```python
> TESTING = "test" in sys.argv or "PYTEST_VERSION" in os.environ
> 
> if not TESTING:
>     INSTALLED_APPS = [
>         *INSTALLED_APPS,
>         "debug_toolbar",
>     ]
>     MIDDLEWARE = [
>         "debug_toolbar.middleware.DebugToolbarMiddleware",
>         *MIDDLEWARE,
>     ]
> ```
> 
> You should also modify your URLconf file:
> 
> ```python
> from django.conf import settings
> 
> if not settings.TESTING:
>     from debug_toolbar.toolbar import debug_toolbar_urls
> 
>     urlpatterns = [
>         *urlpatterns,
>     ] + debug_toolbar_urls()
> ```
> 

<aside>
📢

# پایان Part-4

</aside>
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-5.md`
```md
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
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-6.md`
```md
# ACRON Methodology Part-6

# فاز 5: Cart Domain

<aside>
📢

در Part-4 ، فاز 4 تمام شد

</aside>

حالا با قدرت وارد یکی از حساس‌ترین بخش‌های فروشگاه می‌شویم. سبد خرید در اپلیکیشن‌های مدرن (مثل دیجی‌کالا یا آمازون) تفاوت‌های زیادی با سیستم‌های قدیمی دارد.

**تصمیمات معماری (چیستی و چرایی):**

۱. **آیا سبد خرید نیاز به لاگین دارد؟**
در فروشگاه‌های مدرن، کاربر باید بتواند حتی بدون اینکه ثبت‌نام کرده باشد، محصولات را به سبد خرید اضافه کند. وقتی تصمیم به پرداخت گرفت، آن‌وقت لاگین می‌کند. پس ما نباید جدول `Cart` را به اجبار به `User` متصل کنیم.

۲. **چرا از UUID به عنوان Primary Key (کلید اصلی) استفاده می‌کنیم؟**
اگر آیدی سبد خرید عدد باشد (مثلاً `id=5`)، یک هکر به راحتی در Postman می‌نویسد `/api/carts/6/` و سبد خرید شخص دیگری را می‌بیند! وقتی کلید اصلی را UUID (یک رشته طولانی و تصادفی) قرار دهیم، حدس زدن سبد خرید دیگران عملاً غیرممکن می‌شود. فرانت‌اند این UUID را می‌گیرد و در `LocalStorage` مرورگر کاربر ذخیره می‌کند.

۳. **جلوگیری از داده‌های تکراری (Unique Together):**
اگر کاربر یک "لپ‌تاپ" در سبد خرید دارد و دوباره دکمه "افزودن به سبد" را می‌زند، دیتابیس نباید دو ردیف جداگانه برای لپ‌تاپ بسازد! بلکه باید تعداد (Quantity) لپ‌تاپ را در همان ردیف قبلی از ۱ به ۲ تغییر دهد.

> 1- **فعال‌سازی اپلیکیشن در `base.py`:**
> 
> 
> فایل config/settings/base.py را باز کنید و اپلیکیشن carts را از کامنت خارج کنید:
> 
> ```python
> INSTALLED_APPS = [
>     # ...
>     'apps.products',
>     'apps.carts', # این خط از کامنت خارج شود
> ]
> ```
> 

> 2- طراحی ساختار دیتابیس در فایل `apps/carts/models.py`:
> 
> 
> ```python
> import uuid
> from django.db import models
> from apps.products.models import Product
> 
> class Cart(models.Model):
>     # الف) جایگزینی ID عددی با UUID به عنوان کلید اصلی امنیتی
>     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
>     created_at = models.DateTimeField(auto_now_add=True)
> 
>     def __str__(self):
>         return str(self.id)
> 
> class CartItem(models.Model):
>     # ب) اتصال آیتم به سبد خرید
>     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
>     
>     # ج) اتصال آیتم به محصول
>     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
>     
>     # د) تعداد محصول در سبد
>     quantity = models.PositiveSmallIntegerField(default=1)
> 
>     class Meta:
>         # هـ) جلوگیری از ساخت دو ردیف برای یک محصول تکراری در یک سبد
>         unique_together = [['cart', 'product']]
> 
>     def __str__(self):
>         return f"{self.quantity} x {self.product.name}"
> ```
> 

**کالبدشکافی عمیق کدها (چرایی):**

- **`primary_key=True` در فیلد ID:** جنگو به صورت پیش‌فرض یک فیلد عددی پنهان به نام `id` می‌سازد. با این دستور به دیتابیس می‌گوییم: "ستون عددی پیش‌فرض را نساز، من می‌خواهم این UUID دقیقاً همان کلید اصلی و ستون شماره یک جدول من باشد."
- **`on_delete=models.CASCADE`:** * در رابطه `cart`: اگر یک سبد خرید به هر دلیلی پاک شود، تمام آیتم‌های داخل آن (CartItem) هم باید در دیتابیس دود شوند و از بین بروند. منطقی نیست آیتمی در دیتابیس بماند که صاحب (سبد) ندارد.
    - در رابطه `product`: اگر ادمین یک کالا را از سیستم حذف کند، آن کالا باید به صورت خودکار از سبد خرید تمام کاربران ناپدید شود.
- **`PositiveSmallIntegerField`:** برای تعداد کالا (Quantity) از این فیلد استفاده کردیم. چرا؟ چون تعداد کالا هرگز منفی نمی‌شود و از طرفی هیچکس ۳۲,۰۰۰ عدد لپ‌تاپ در یک سبد قرار نمی‌دهد! استفاده از `SmallInteger` به جای `Integer` ساده، فضای کمتری در حافظه RAM و هارد سرور اشغال می‌کند.
- **`unique_together = [['cart', 'product']]`:** این یک قفل ترکیبی در دیتابیس MySQL است. این کد به دیتابیس می‌گوید: "اگر کسی سعی کرد در سبد خرید شماره `X`، محصول `Y` را برای بار دوم `INSERT` کند، جلوی او را بگیر و ارور بده." (بعداً در Serializer یاد می‌گیریم که چطور این ارور را مدیریت کنیم و به جای ساختن ردیف جدید، عدد Quantity را `UPDATE` کنیم).

> 3- **اعمال مدل‌ها در دیتابیس:**
> 
> 
> در ترمینال خود کدهای زیر را اجرا کنید تا جداول ساخته شوند:
> 
> ```python
> python manage.py makemigrations carts
> python manage.py migrate
> ```
> 

خروجی:

```python
$ python manage.py makemigrations carts
Migrations for 'carts':
  apps\carts\migrations\0001_initial.py
    + Create model Cart
    + Create model CartItem

```

```python
$ python manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, auth, carts, contenttypes, customers, products, sessions
Running migrations:
  Applying carts.0001_initial... OK

```

<aside>
📢

**ا  On-the-fly vs. Stored**

</aside>

در این مرحله می‌خواهیم `CartSerializer` را بسازیم. اما قبل از اینکه دست به کیبورد ببریم، بیایید یک سناریوی مهم را در معماری نرم‌افزار بررسی کنیم: «محاسبه در لحظه» در برابر «ذخیره در دیتابیس» (On-the-fly vs. Stored).
شاید این سوال پیش بیاید که چرا فیلدی به نام total_price  را مستقیماً داخل مدل CartItem (در دیتابیس) ذخیره نکردیم؟ 
فرض کنید کاربر لپ‌تاپی به قیمت ۵۰ میلیون تومان را به سبد خرید اضافه می‌کند. 

اگر ما عدد ۵۰ میلیون را در رکورد سبد خرید ذخیره کنیم، چه می‌شود اگر فردا قیمت آن لپ‌تاپ در سایت تغییر کند و به ۵۵ میلیون برسد؟ سبد خرید کاربر همچنان ۵۰ میلیون را نشان می‌دهد که این یک باگ مالی خطرناک است!
به همین دلیل، ما قیمت کل را در دیتابیس ذخیره نمی‌کنیم، بلکه در لحظه‌ای که کاربر سبد خرید را درخواست می‌کند، آن را به صورت زنده (Dynamic) محاسبه کرده و می‌فرستیم.  این جادو در DRF با ابزاری به نام  SerializerMethodField انجام می‌شود.

<aside>
📢

قدم اول: ساخت Serializer سبد خرید و آیتم‌ها

</aside>

> 4- در مسیر `apps/carts/` یک فایل جدید به نام `serializers.py` بسازید و کدهای زیر را به دقت وارد کنید:
> 
> 
> ```python
> from rest_framework import serializers
> from .models import Cart, CartItem
> from apps.products.models import Product
> 
> # ۱. ساخت یک سریالایزر سبک و بهینه برای محصول داخل سبد خرید
> class SimpleProductSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Product
>         # ما در سبد خرید به توضیحات طولانی یا برند نیازی نداریم، فقط اطلاعات حیاتی!
>         fields = ['id', 'name', 'price', 'main_image']
> 
> # ۲. سریالایزر آیتم‌های داخل سبد (CartItem)
> class CartItemSerializer(serializers.ModelSerializer):
>     # نمایش اطلاعات محصول به صورت تو در تو، اما با سریالایزر سبک
>     product = SimpleProductSerializer(read_only=True)
>     
>     # تعریف یک فیلد محاسباتی که در دیتابیس وجود ندارد
>     total_price = serializers.SerializerMethodField()
> 
>     class Meta:
>         model = CartItem
>         fields = ['id', 'product', 'quantity', 'total_price']
> 
>     # متد متصل به فیلد محاسباتی بالا
>     def get_total_price(self, cart_item: CartItem):
>         # قیمت محصول × تعداد آن
>         return cart_item.quantity * cart_item.product.price
> 
> # ۳. سریالایزر اصلی سبد خرید (Cart)
> class CartSerializer(serializers.ModelSerializer):
>     id = serializers.UUIDField(read_only=True)
>     
>     # اتصال آیتم‌ها به سبد خرید (توجه: کلمه items همان related_name در مدل است)
>     items = CartItemSerializer(many=True, read_only=True)
>     
>     # فیلد محاسباتی برای جمع کل مبلغ کل سبد خرید
>     grand_total = serializers.SerializerMethodField()
> 
>     class Meta:
>         model = Cart
>         fields = ['id', 'items', 'grand_total']
> 
>     # متد متصل به فیلد محاسباتی مبلغ کل
>     def get_grand_total(self, cart: Cart):
>         # یک حلقه پایتونی برای جمع زدن قیمت کل تک‌تک آیتم‌های این سبد
>         return sum([item.quantity * item.product.price for item in cart.items.all()])
> ```
> 

<aside>
📢

کالبدشکافی عمیق و آموزش معماری این بخش

</aside>

بیایید این کدها را زیر ذره‌بین ببریم تا دقیقاً بفهمیم پشت صحنه چه اتفاقی می‌افتد:

۱. چرا `SimpleProductSerializer` را ساختیم؟ (مفهوم Over-fetching)

ما در فاز ۴ یک `ProductSerializer` بسیار قدرتمند ساختیم که دسته‌بندی، برند و گالری ۱۰ تایی تصاویر را لود می‌کرد. اگر همان را اینجا استفاده می‌کردیم، کاربر با باز کردن سبد خریدش حجم عظیمی از داده‌های غیرضروری را دانلود می‌کرد (به این مشکل در مهندسی نرم‌افزار Over-fetching می‌گویند که باعث کُندی لود اپلیکیشن می‌شود).
با ساختن یک نسخه "ساده‌سازی شده" (فقط نام، عکس اصلی و قیمت)، سایز (Payload) پاسخ API را به شدت کاهش دادیم.

۲. مکانیزم `SerializerMethodField` چگونه کار می‌کند؟

وقتی شما فیلدی از این نوع تعریف می‌کنید (مثل `total_price`)، جنگو می‌فهمد که نباید به دنبال این ستون در دیتابیس بگردد. در عوض، به صورت خودکار به دنبال متدی می‌گردد که اسم آن با `_get` شروع شود و نام فیلد در ادامه آن بیاید (یعنی `get_total_price`).

- **پارامتر ورودی متد (`cart_item`):** DRF به صورت خودکار، همان رکوردِ دیتابیسی که در حال سریالایز شدن است را به این متد پاس می‌دهد.
- **Type Hinting (`cart_item: CartItem`):** این عبارت در پایتون اجباری نیست، اما یک استاندارد کدنویسی بسیار تمیز است. با نوشتن آن، ویرایشگر کد شما (مثل VS Code) می‌فهمد که این متغیر از جنس مدل `CartItem` است و وقتی نقطه (`.`) می‌گذارید، متدها و فیلدهای آن را به شما پیشنهاد می‌دهد.

۳. جادوی محاسبه `grand_total` در پایتون

در متد `get_grand_total` ما از یک ویژگی قدرتمند پایتون به نام List Comprehension استفاده کردیم.
کد `[item.quantity * item.product.price for item in cart.items.all()]` این کار را می‌کند:

- می‌رود تمام آیتم‌های این سبد را می‌آورد (`cart.items.all()`).
- روی تک‌تک آن‌ها حلقه می‌زند.
- تعداد را ضربدر قیمت می‌کند.
- در نهایت یک لیست از اعداد (مبالغ) به ما می‌دهد (مثلاً `[50000, 120000]`).
سپس تابع داخلی پایتون یعنی `sum()` تمام اعداد آن لیست را با هم جمع می‌کند و مبلغ نهایی فاکتور به دست می‌آید.

با این معماری، هر بار که کاربر API سبد خرید را صدا می‌زند، قیمت‌ها دقیقاً با آخرین قیمت‌های ثبت شده در دیتابیسِ محصولات محاسبه می‌شوند و هرگز مغایرتی پیش نخواهد آمد.

<aside>
📢

**حالا که این سریالایزر هوشمند را ساختیم، نوبت به ویوها (Views) می‌رسد. در Viewهای سبد خرید، ما با یک چالش روبرو هستیم: "کاربر چطور یک آیتم را به سبد خرید اضافه کند در حالی که ما قانون `unique_together` (جلوگیری از کالای تکراری) را در دیتابیس گذاشته‌ایم؟"**

</aside>

همان‌طور که در دیتابیس تنظیم کردیم، یک سبد خرید نمی‌تواند دو ردیف مجزا برای یک محصول تکراری داشته باشد. 

اگر کاربر یک «گوشی اپل» در سبد خود دارد و دوباره دکمه «افزودن به سبد» را می‌زند، ما نباید به دیتابیس دستور `INSERT` (ساخت ردیف جدید) بدهیم، زیرا دیتابیس خشمگین شده و خطای ۵۰۰ (Server Error) میدهد.

 به جای آن، ما باید دستور `UPDATE` بدهیم و `quantity` (تعداد) را مثلاً از ۱ به ۲ تغییر دهیم.

اما سریالایزرهای پیش‌فرض DRF این هوشمندی را ندارند. 

پس ما باید کنترل سریالایزر را به دست بگیریم. 

این کار از طریق **جداسازی Serializerهای ورودی (Input) و خروجی (Output)** و اورراید کردن متد `save` انجام می‌شود.

<aside>
📢

ساخت Serializerهای ورودی (افزودن و ویرایش)

</aside>

> 5-  فایل `apps/carts/serializers.py` را باز کنید و کدهای زیر را به انتهای آن (زیر کدهای قبلی) اضافه کنید:
> 
> 
> ```python
> # این کلاس فقط برای زمانی است که کلاینت می‌خواهد محصولی را به سبد اضافه کند (POST)
> class AddCartItemSerializer(serializers.ModelSerializer):
>     # کلاینت فقط این دو شناسه را برای ما می‌فرستد
>     product_id = serializers.IntegerField()
>     cart_id = serializers.UUIDField()
> 
>     class Meta:
>         model = CartItem
>         fields = ['id', 'cart_id', 'product_id', 'quantity']
> 
>     # اعتبارسنجی: آیا این محصول اصلاً در فروشگاه وجود دارد؟
>     def validate_product_id(self, value):
>         if not Product.objects.filter(id=value).exists():
>             raise serializers.ValidationError("محصولی با این شناسه یافت نشد.")
>         return value
> 
>     # اعتبارسنجی: آیا این سبد خرید اصلاً وجود دارد؟
>     def validate_cart_id(self, value):
>         if not Cart.objects.filter(id=value).exists():
>             raise serializers.ValidationError("سبد خریدی با این شناسه یافت نشد.")
>         return value
> 
>     # قلب تپنده این بخش: تغییر رفتار ذخیره‌سازی برای دور زدن خطای دیتابیس
>     def save(self, **kwargs):
>         cart_id = self.validated_data['cart_id']
>         product_id = self.validated_data['product_id']
>         quantity = self.validated_data['quantity']
> 
>         try:
>             # سناریو ۱: آیا این محصول از قبل در این سبد خرید وجود دارد؟
>             cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
>             
>             # بله وجود دارد! پس فقط تعداد جدید را با تعداد قبلی جمع کن
>             cart_item.quantity += quantity
>             cart_item.save()
>             
>             self.instance = cart_item
>             
>         except CartItem.DoesNotExist:
>             # سناریو ۲: محصول در سبد نیست. پس یک ردیف جدید در دیتابیس بساز
>             self.instance = CartItem.objects.create(
>                 cart_id=cart_id, 
>                 product_id=product_id, 
>                 quantity=quantity
>             )
> 
>         return self.instance
> 
> # این کلاس فقط برای زمانی است که کلاینت می‌خواهد تعداد را تغییر دهد (PATCH)
> # مثلاً کاربر در سبد خرید دکمه + یا - را می‌زند
> class UpdateCartItemSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = CartItem
>         fields = ['quantity']
> ```
> 

<aside>
📢

کالبدشکافی کدهای Serializer (چیستی و چرایی)

</aside>

- **چرا کلاس‌های جدید ساختیم؟** در متدولوژی تمیزِ API، دیتایی که ما به کلاینت نشان می‌دهیم (خروجی) با دیتایی که از او می‌گیریم (ورودی) متفاوت است. `CartItemSerializer` (که در بخش قبل ساختیم) برای نمایش بود و شامل `product_name` و `total_price` بود. اما وقتی کلاینت می‌خواهد محصولی ثبت کند، فقط یک عدد `product_id` برای ما می‌فرستد. ما نمی‌توانیم از یک سریالایزر برای هر دو کار استفاده کنیم، بنابراین `AddCartItemSerializer` را فقط به عنوان "دروازه ورود داده" ساختیم.
- **متدهای `validate_<field_name>`:** همانند فاز ۳، ما اینجا هم امنیت را بالا بردیم. اگر یک هکر آیدی محصولی را بفرستد که در دیتابیس نیست، سیستم کرش نمی‌کند، بلکه متد `validate_product_id` یک خطای تمیزِ 400 Bad Request برمی‌گرداند.
- **متد `save` و متغیر `self.validated_data`:** وقتی جنگو تمام ولیدیشن‌ها را با موفقیت پاس می‌کند، دیتاهای تایید شده را در دیکشنری `validated_data` قرار می‌دهد. ما در بلوک `try` تلاش می‌کنیم با دستور `get` آن کالا را در آن سبد پیدا کنیم. اگر پیدا شد، فقط فیلد `quantity` آپدیت می‌شود (دور زدن `unique_together`) و اگر پیدا نشد، خطای `DoesNotExist` رخ می‌دهد که ما آن را در بلوک `except` شکار می‌کنیم و با دستور `create` ردیف جدید را می‌سازیم.

<aside>
📢

قدم دوم: ساخت Viewهای هوشمند سبد خرید

</aside>

اکنون باید کنترلرهای API (ویوها) را بسازیم تا درخواست‌های کلاینت را دریافت کرده و به سریالایزرهای مناسب هدایت کنند.

> 6- در مسیر `apps/carts/` فایل `views.py` را ایجاد کرده و کدهای زیر را وارد کنید:
> 
> 
> ```python
> from rest_framework.viewsets import ModelViewSet, GenericViewSet
> from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
> from drf_spectacular.utils import extend_schema_view, extend_schema
> from .models import Cart, CartItem
> from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
> 
> @extend_schema_view(
>     create=extend_schema(summary="ساخت سبد خرید جدید", tags=['Carts']),
>     retrieve=extend_schema(summary="دریافت محتویات سبد خرید", tags=['Carts']),
>     destroy=extend_schema(summary="حذف کامل سبد خرید", tags=['Carts']),
> )
> class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
>     """
>     ویو برای مدیریت خودِ سبد خرید (بدون آیتم‌ها).
>     توجه: متد List حذف شده است زیرا هیچ کاربری نباید لیست سبد خرید دیگران را ببیند.
>     """
>     # بهینه‌سازی کوئری دیتابیس برای جلوگیری از مشکل N+1 در دریافت آیتم‌های سبد
>     queryset = Cart.objects.prefetch_related('items__product').all()
>     serializer_class = CartSerializer
> 
> @extend_schema_view(
>     create=extend_schema(summary="افزودن محصول به سبد خرید", tags=['Cart Items']),
>     partial_update=extend_schema(summary="تغییر تعداد یک محصول در سبد", tags=['Cart Items']),
>     destroy=extend_schema(summary="حذف یک محصول از سبد خرید", tags=['Cart Items']),
> )
> class CartItemViewSet(ModelViewSet):
>     """
>     ویو برای مدیریت آیتم‌های داخل سبد خرید.
>     """
>     # جلوگیری از استفاده از متد PUT (ما فقط به PATCH برای تغییر تعداد نیاز داریم)
>     http_method_names = ['post', 'patch', 'delete']
>     
>     queryset = CartItem.objects.select_related('product').all()
> 
>     # جادوی DRF: انتخاب سریالایزر به صورت دینامیک بر اساس نوع درخواست (Method)
>     def get_serializer_class(self):
>         if self.request.method == 'POST':
>             return AddCartItemSerializer
>         elif self.request.method == 'PATCH':
>             return UpdateCartItemSerializer
>         
>         return CartItemSerializer
> ```
> 

<aside>
📢

کالبدشکافی کدهای View

</aside>

- **چرا `CartViewSet` از `ModelViewSet` ارث‌بری نکرد؟**
یک `ModelViewSet` کامل، ۵ متد دارد: ساختن، خواندن تکی، آپدیت کردن، پاک کردن و **لیست کردن همه (List)**. اگر ما از `ModelViewSet` استفاده می‌کردیم، مسیر `GET /api/carts/` باز می‌شد و هر کسی می‌توانست تمام سبدهای خرید فروشگاه را ببیند (یک فاجعه امنیتی!). با ارث‌بری از `GenericViewSet` و تزریق فقط سه میکسین (Mixin) ضروری یعنی `Create`, `Retrieve`, `Destroy`، ما به صورت جراحی‌گونه متدهای خطرناک را مسدود کردیم.
- **`prefetch_related('items__product')`:** علامت `__` (دو آندرلاین) در جنگو به معنای نفوذ به عمق جداول است. این کد می‌گوید: "وقتی سبد خرید را از دیتابیس آوردی، تمام آیتم‌هایش (`items`) و تمام محصولاتِ آن آیتم‌ها (`product`) را هم از قبل کش (Cache) کن تا به مشکل N+1 برنخوریم."
- **متد `get_serializer_class`:** این یکی از پیشرفته‌ترین تکنیک‌های DRF است (Dynamic Serializers). کلاینت به یک URL واحد متصل می‌شود، اما بک‌اند ما می‌فهمد که اگر درخواست `POST` بود، باید از سریالایزر `AddCartItem` (که فقط آی‌دی می‌گیرد) استفاده کند و اگر `PATCH` بود از سریالایزر آپدیت استفاده کند.

<aside>
📢

قدم سوم: تنظیم URLهای روتر

</aside>

> 7- در مسیر `apps/carts/` فایل `urls.py` را ایجاد کنید:
> 
> 
> ```python
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CartViewSet, CartItemViewSet
> 
> router = DefaultRouter()
> # ثبت ویوست سبد خرید (آی‌دی این مسیر از نوع UUID خواهد بود)
> router.register('carts', CartViewSet, basename='carts')
> 
> # ثبت ویوست آیتم‌های سبد خرید
> router.register('cart-items', CartItemViewSet, basename='cart-items')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

> 8-  مسیر نهایی را در `apps/api/urls.py` اضافه کنید:
> 
> 
> ```python
> # بخشی از فایل apps/api/urls.py
> urlpatterns = [
>     # ...
>     path('customers/', include('apps.customers.urls')),
>     path('products/', include('apps.products.urls')),
>     # اضافه کردن مسیر سبد خرید به قلب API
>     path('', include('apps.carts.urls')), 
> ]
> ```
> 
> (نکته: چون در روتر خودش کلمات `carts` و `cart-items` را تعریف کردیم، اینجا رشته را خالی گذاشتیم `''` تا URLها دوبل نشوند).
> 

> 
> 
> 
> تست عملیات (مهم‌ترین بخش)
> 
> حالا سرور را روشن کنید و به آدرس Swagger (`http://127.0.0.1:8000/api/docs/`) بروید.
> ۱. یک درخواست `POST` به `/api/carts/` بزنید تا یک سبد خرید خالی ساخته شود. UUID تولید شده را کپی کنید.
> ۲. حالا یک درخواست `POST` به `/api/cart-items/` بزنید. در Body درخواست، UUID سبد خرید، آی‌دی یک محصول از فروشگاه، و تعداد (`quantity: 1`) را بفرستید.
> ۳. **تست جادوی ما:** دوباره همان درخواست را عیناً تکرار کنید. خواهید دید که به جای ارور دیتابیس، تعداد محصول شما ۲ می‌شود!
> 

در اینجا راهنمای قدم‌به‌قدم برای ویرایش و ارسال Body در Swagger آمده است:

### راهنمای تصویری و قدم‌به‌قدم ارسال Body در Swagger

> **1-  پیدا کردن Endpoint مورد نظر**
> 
- در صفحه Swagger (آدرس `http://127.0.0.1:8000/api/docs/`)، به پایین اسکرول کنید تا به تگ **Cart Items** (که در `@extend_schema` تعریف کردیم) برسید.
- روی نوار سبز رنگ که نوشته شده `POST /api/cart-items/` (افزودن محصول به سبد خرید) کلیک کنید تا این بخش باز و منبسط شود.

> **2- فعال‌سازی حالت تست**
> 
- در گوشه سمت راستِ پنلی که باز شد، یک دکمه خاکستری یا سفید رنگ به نام **`Try it out`** وجود دارد. روی آن کلیک کنید.
- *چرایی:* با زدن این دکمه، Swagger فرم‌ها و باکس‌های متنی را از حالت "فقط خواندنی" (Read-only) خارج کرده و به شما اجازه ویرایش و ارسال اطلاعات به سرور را می‌دهد.

> **3- پیدا کردن و ویرایش باکس Body**
> 
- بعد از زدن دکمه `Try it out`، کمی پایین‌تر بخشی به نام **Request body** ظاهر می‌شود.
- داخل این بخش، یک باکس متنیِ مشکی یا خاکستری رنگ (شبیه به محیط کدنویسی) می‌بینید که حاوی یک ساختار JSON اولیه است.
- شما باید اطلاعات داخل این باکس را پاک کنید و اطلاعات واقعی خودتان را به شکل زیر جایگزین کنید:

```json
{
  "cart_id": "UUID-سبد-خریدی-که-در-مرحله-۱-کپی-کردید",
  "product_id": 1,
  "quantity": 1
}
```

*(نکته: به جای `1` در `product_id`، آی‌دی یکی از محصولاتی که قبلاً در پنل ادمین ساخته‌اید را قرار دهید. دقت کنید که ساختار JSON با دقت رعایت شود، مثلاً کلمات داخل کوتیشن `""` باشند).*

> **4- ارسال درخواست به سمت بک‌اند (Execute)**
> 
- دقیقاً در زیر همان باکس Request body، یک دکمه بزرگِ آبی رنگ به نام **`Execute`** وجود دارد. روی آن کلیک کنید.
- *چرایی:* این دکمه دقیقاً معادل دکمه Send در Postman است. با زدن آن، مرورگر شما درخواست POST را به همراه بدنه JSON که نوشتید، به ویوی `CartItemViewSet` در بک‌اند جنگو می‌فرستد.

> **5- مشاهده نتیجه (Responses)**
> 
- کمی پایین‌تر از دکمه Execute، بخشی به نام **Responses** و قسمت **Server response** وجود دارد.
- در آنجا می‌توانید `Code` (که باید `201` یا `200` باشد) و `Details` (که همان خروجی JSON از سمت سرور است) را مشاهده کنید.

> 6- حالا دقیقاً همین عملیات را انجام دهید، یک بار محصول را ثبت کنید و سپس بدون اینکه چیزی را تغییر دهید، **دوباره دکمه `Execute` را بزنید**. در پاسخ دوم سرور، باید ببینید که اروری دریافت نمی‌کنید و عدد `quantity` برای آن محصول از ۱ به ۲ تغییر کرده است. این همان جادویی است که با اورراید کردن متد `save` در Serializer پیاده‌سازی کردیم!
> 

**تصمیم معماری و راه حل**
همان‌طور که قبلاً بحث کردیم، **سبد خرید باید برای کاربران مهمان (بدون لاگین) هم باز باشد.** شاید بپرسید آیا این کار از نظر امنیتی خطرناک نیست؟
پاسخ: **خیر.** چون کلید اصلی سبد خرید ما یک **UUID** است (مثلاً `3fa85f64-5717-4562-b3fc-2c963f66afa6`). حدس زدن این رشته تصادفی برای هکرها عملاً غیرممکن است (احتمال ۱ در $2^{122}$). بنابراین فقط کسی که این UUID را دارد (که در مرورگر خود کاربر ذخیره می‌شود) می‌تواند سبد خرید را ببیند یا ویرایش کند.

<aside>
📢

**قفل‌گشایی از APIهای سبد خرید:**

</aside>

> 9- فایل `apps/carts/views.py` را باز کنید. ماژول `AllowAny` را ایمپورت کرده و آن را به هر دو کلاس اضافه کنید: 
لطفا از کپی و پیست استفاده نکنید !!! 
تمام کد را خوانده و قسمت های لازم را انتقال دهید:
> 
> 
> ```python
> # این ایمپورت را به بالای فایل اضافه کنید
> from rest_framework.permissions import AllowAny
> 
> # ... کدهای قبلی ...
> 
> class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
>     # این خط را اضافه کنید تا قفل شکسته شود
>     permission_classes = [AllowAny]
>     
>     queryset = Cart.objects.prefetch_related('items__product').all()
>     serializer_class = CartSerializer
> 
> class CartItemViewSet(ModelViewSet):
>     # این خط را اضافه کنید تا قفل شکسته شود
>     permission_classes = [AllowAny]
>     
>     http_method_names = ['post', 'patch', 'delete']
>     queryset = CartItem.objects.select_related('product').all()
>     
>     # ... بقیه کدها بدون تغییر ...
> ```
> 

<aside>
📢

یک نکته آموزشی درباره Swagger (قفلِ بالای صفحه)

</aside>

اگر در آینده API خاصی داشتید که **واقعاً** نیاز به لاگین داشت (مثل پروفایل مشتری) و خواستید آن را در Swagger تست کنید، باید چه کار کنید؟

1. ابتدا از طریق مسیر `POST /api/token/` یوزرنیم و پسورد خود را می‌فرستید.
2. سرور به شما یک `access_token` می‌دهد. آن را کپی می‌کنید.
3. در بالاترین قسمت صفحه Swagger، یک دکمه سبز رنگ با آیکون قفل به نام **Authorize** وجود دارد. روی آن کلیک می‌کنید.
4. توکن خود را در باکس مربوطه Paste می‌کنید و دکمه Authorize را می‌زنید.
از این به بعد، Swagger به صورت خودکار توکن شما را در تمام درخواست‌هایی که با دکمه `Execute` می‌زنید، تزریق می‌کند و دیگر خطای ۴۰۱ نمی‌گیرید.

<aside>
📢

# پایان Part-6

</aside>
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-7.md`
```md
# ACRON Methodology Part-7

<aside>
📢

در Part-6 ، فاز 5 تمام شد تعداد قدم ها 9 قدم

</aside>

# فاز 6: Cart Domain

---

<aside>
📢

**فعال‌سازی و طراحی مدل‌های سفارش**

</aside>

کالبدشکافی معماری سفارشات (تفاوت Cart و Order چیست؟)

قبل از کدنویسی، باید یک مفهوم حیاتی در سیستم‌های مالی و فروشگاهی را درک کنیم: **«تغییرپذیری در برابر تغییرناپذیری» (Mutable vs. Immutable)**.

- **سبد خرید (Cart):** یک موجودیت موقت و **تغییرپذیر** است. کاربر می‌تواند امروز یک لپ‌تاپ به سبدش اضافه کند، فردا قیمت لپ‌تاپ در سایت تغییر کند و وقتی کاربر به سبدش نگاه می‌کند، قیمت جدید را می‌بیند.
- **سفارش (Order):** یک **اسنپ‌شات (عکسِ لحظه‌ای)** از تاریخ است و کاملاً **تغییرناپذیر** است. وقتی کاربر دکمه پرداخت را می‌زند و سفارش ثبت می‌شود، قیمت آن کالا در آن ثانیه، باید برای همیشه در دیتابیس ثبت (فریز) شود. اگر یک سال بعد قیمت لپ‌تاپ ۳ برابر شد، فاکتور کاربر (Order) نباید تغییر کند؛ او باید دقیقاً همان مبلغی را ببیند که در زمان خرید پرداخت کرده است.

به همین دلیل است که ما نمی‌توانیم فقط به جدول `Product` متصل بمانیم، بلکه باید فیلدی به نام `unit_price` (قیمت واحد) را در جدول `OrderItem` کپی و ذخیره کنیم.

> 1- فایل `config/settings/base.py` را باز کنید و اپلیکیشن `orders` را از کامنت خارج کنید:
> 
> 
> ```python
> INSTALLED_APPS = [
>     # ...
>     'apps.carts',
>     'apps.orders', # این خط از کامنت خارج شود
> ]
> ```
> 

> 2-  فایل `apps/orders/models.py` را باز کنید و کدهای مهندسی‌شده‌ی زیر را بنویسید:
> 
> 
> ```python
> import uuid
> from django.db import models
> from apps.customers.models import Customer
> from apps.products.models import Product
> 
> class Order(models.Model):
>     # ۱. تعریف وضعیت‌های مختلف یک سفارش با استفاده از TextChoices
>     class OrderStatus(models.TextChoices):
>         PENDING = 'P', 'در انتظار پرداخت'
>         COMPLETED = 'C', 'پرداخت موفق'
>         CANCELED = 'X', 'لغو شده'
> 
>     # ۲. شناسه یکتا و غیرقابل حدس برای پیگیری سفارش
>     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
>     
>     # ۳. ارتباط با مشتری (سفارش برخلاف سبد خرید، حتماً صاحب دارد)
>     customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
>     
>     # ۴. وضعیت فعلی سفارش
>     status = models.CharField(
>         max_length=1, 
>         choices=OrderStatus.choices, 
>         default=OrderStatus.PENDING
>     )
>     
>     # ۵. زمان ثبت سفارش
>     created_at = models.DateTimeField(auto_now_add=True)
> 
>     def __str__(self):
>         return f"Order {self.id} - {self.customer.user.username}"
> 
> class OrderItem(models.Model):
>     order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
>     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
>     quantity = models.PositiveSmallIntegerField()
>     
>     # ۶. مهم‌ترین فیلد این فاز: فریز کردن قیمت!
>     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
> 
>     def __str__(self):
>         return f"{self.product.name} (x{self.quantity})"
> ```
> 

آموزش عمیق کدهای مدل سفارش (چرایی انتخاب‌ها)

1. چرا از `models.TextChoices` استفاده کردیم؟
در گذشته برنامه‌نویسان جنگو یک لیست ساده (تاپل) برای گزینه‌ها می‌نوشتند. اما کلاس `TextChoices` (که در نسخه‌های جدیدتر جنگو معرفی شد) بسیار شیء‌گراتر و تمیزتر است. این کار به ما اجازه می‌دهد در هر جای کد به جای اینکه بنویسیم `if status == 'P'`, به صورت حرفه‌ای بنویسیم `if status == Order.OrderStatus.PENDING`. این کار جلوی خطاهای تایپی (Typo) را می‌گیرد و کد را به شدت خوانا می‌کند.
2. تفاوت `on_delete=models.PROTECT` با CASCADE در اینجا چیست؟
در سبد خرید (`Cart`) ما از `CASCADE` استفاده کردیم، چون اگر کالا از فروشگاه پاک می‌شد، اشکالی نداشت از سبدِ پرداخت‌نشده‌ی کاربر هم غیب شود.
اما در اینجا از `PROTECT` استفاده کردیم. فاکتور و سفارش، سند قانونی و مالی یک کسب‌وکار هستند. اگر ادمین تصمیم گرفت "گوشی آیفون ۱۳" را از دیتابیس پاک کند، دیتابیس باید ارور بدهد و بگوید: *"شما حق ندارید این کالا را پاک کنید، چون در ۳ فاکتورِ گذشته فروخته شده است!"* قانون طلایی سیستم‌های مالی: هیچ‌چیزِ مرتبط با تراکنش‌های گذشته نباید به سادگی قابل پاک شدن (CASCADE) باشد.
3. فیلد `unit_price` در `OrderItem`:
همان‌طور که در ابتدای صحبت‌ها توضیح دادم، این فیلد برای ثبت اسنپ‌شات قیمت است. بعداً در مرحله `Service Layer` (فاز ۸)، ما کدی می‌نویسیم که محتویات `CartItem` را می‌خواند و داخل `OrderItem` کپی می‌کند و در همان لحظه، قیمت فعلی کالا (`product.price`) را داخل `unit_price` ذخیره می‌کند.

<aside>
📢

**انتقال تغییرات به دیتابیس**

</aside>

حالا که معماری قدرتمند فاکتورها را چیدیم، باید آن را روی MySQL اعمال کنیم.

> 2- در ترمینال بنویس:
> 
> 
> ```python
> python manage.py makemigrations orders
> python manage.py migrate
> ```
> 

<aside>
📢

### ایستگاه منطقیِ بعدی ما، **مفهوم Service Layer (لایه سرویس)** است که در متدولوژی acron (فاز ۸) به آن اشاره شده. 

لایه سرویس جایی است که ما منطق تبدیلِ "سبد خرید" به "سفارش" را می‌نویسیم. (تبدیل رکوردهای موقت به رکوردهای دائمی).

</aside>

پنل مدیریت برای بخش سفارشات (فاکتورها) یکی از حساس‌ترین بخش‌های هر فروشگاه اینترنتی است. در اینجا، ما باید کاملاً با ذهنیت یک سیستم مالی کدنویسی کنیم: **فاکتورها اسناد قانونی هستند و نباید به راحتی قابل دستکاری باشند.**

بیایید ابتدا این امنیت را در پنل ادمین پیاده کنیم و سپس وارد مفهوم شگفت‌انگیز لایه سرویس (Service Layer) بشویم.

<aside>
📢

**قدم اول: پیاده‌سازی پنل مدیریت سفارشات (ایمن و غیرقابل تغییر)**

</aside>

> 3- فایل `apps/orders/admin.py` را باز کنید و کدهای زیر را بادقت وارد کنید:
> 
> 
> ```python
> from django.contrib import admin
> from .models import Order, OrderItem
> 
> # ۱. اینلاین برای آیتم‌های داخل فاکتور
> class OrderItemInline(admin.TabularInline):
>     model = OrderItem
>     extra = 0 # ما نمی‌خواهیم ادمین دستی آیتم جدیدی به فاکتور اضافه کند
>     
>     # قفل کردن فیلدها: ادمین نباید بتواند قیمت یا تعداد کالای فروخته شده را عوض کند!
>     readonly_fields = ['product', 'quantity', 'unit_price']
>     
>     # جلوگیری از حذف کردن یک آیتم از وسط فاکتور ثبت شده
>     can_delete = False
> 
> # ۲. مدیریت اصلی فاکتورها
> @admin.register(Order)
> class OrderAdmin(admin.ModelAdmin):
>     list_display = ['id', 'customer', 'status', 'created_at']
>     list_filter = ['status', 'created_at']
>     
>     # جستجو در روابط عمیق دیتابیس
>     search_fields = ['id', 'customer__user__username', 'customer__phone_number']
>     
>     # قفل کردن فیلدهای اصلی فاکتور
>     readonly_fields = ['id', 'customer', 'created_at']
>     
>     inlines = [OrderItemInline]
>     
>     # جلوگیری از ساخت فاکتور دستی توسط ادمین (فاکتور فقط باید از طریق خرید کاربر ساخته شود)
>     def has_add_permission(self, request):
>         return False
> ```
> 

### کالبدشکافی خط به خط کدهای ادمین (چیستی و چرایی)

- `extra = 0` و `can_delete = False`: برخلاف گالری تصاویر (که ادمین باید می‌توانست عکس اضافه و کم کند)، در فاکتور مالی ادمین به هیچ وجه نباید بتواند آیتمی را به فاکتوری که پرداخت شده اضافه کند یا از آن حذف کند. این دو دستور، دکمه‌های Add و Delete را در فرانت‌اند پنل ادمین مخفی می‌کنند.
- `readonly_fields`: ما فیلدهای حیاتی مثل `unit_price` (قیمت فریز شده) و `quantity` را فقط-خواندنی کردیم. این یعنی ادمین در صفحه جزئیات سفارش فقط می‌تواند اطلاعات را ببیند، اما فیلدها خاکستری هستند و قابل ویرایش نیستند. تنها چیزی که ادمین حق دارد عوض کند، فیلد `status` (وضعیت سفارش) است (مثلاً تغییر از "در انتظار" به "موفق").
- `customer__user__username`: این یکی از جادوهای جنگو (ORM) است. علامت `__` (دو آندرلاین) به دیتابیس می‌گوید: "از جدول `Order` برو به جدول `Customer`، از آنجا برو به جدول `CustomUser` و در فیلد `username` جستجو کن." این باعث می‌شود ادمین بتواند با تایپ کردن نام کاربری یک شخص، تمام فاکتورهای او را پیدا کند.
- `has_add_permission`: ما با اورراید کردن این متد و برگرداندن `False`، دکمه "Add Order" را به طور کامل از پنل ادمین حذف کردیم! چرایی: فاکتور باید نتیجه یک تراکنش سیستمی باشد، نه اینکه ادمین بنشیند و دستی فاکتور بسازد.

---

### ورود به دنیای لایه سرویس (Service Layer)

اکنون که دیتابیس و پنل ادمین ما آماده است، می‌خواهیم API پرداخت و ثبت نهایی سفارش را بنویسیم. در پروژه‌های مبتدی، برنامه‌نویس تمام کدهای تبدیل سبد خرید به سفارش را مستقیماً داخل `views.py` می‌نویسد (الگوی ضد‌معماری به نام Fat Views).

اما در پروژه های بزرگ تر شبیه acron ، ما از **معماری سه‌لایه (Three-Tier Architecture)** استفاده می‌کنیم.

#### چرا به لایه سرویس نیاز داریم؟

فرض کنید کاربر روی دکمه "تکمیل خرید" کلیک می‌کند. چه اتفاقاتی باید بیفتد؟

1. پیدا کردن سبد خرید کاربر.
2. بررسی اینکه آیا کالاها هنوز در انبار موجودی دارند (`inventory` > 0)؟
3. اگر موجودی نبود، خطا بدهد.
4. اگر موجودی بود، یک رکورد جدید در جدول `Order` بسازد.
5. روی تک‌تک `CartItem`ها حلقه بزند و آن‌ها را به `OrderItem` تبدیل کند.
6. قیمت فعلی کالا را در `unit_price` فریز (کپی) کند.
7. موجودی انبار (`inventory`) را کاهش دهد.
8. سبد خرید (`Cart`) را برای همیشه پاک کند.

اگر تمام این ۸ مرحله پیچیده را در `views.py` بنویسیم، کد ما غیرقابل خواندن، غیرقابل تست و به شدت کثیف می‌شود. لایه سرویس (Service Layer) دقیقاً برای همین به وجود آمده است: 

**جدا کردن «منطق پردازشی کسب‌وکار» از «منطق دریافت درخواست HTTP».**

<aside>
📢

قدم بعدی: ساخت اسکلت‌بندی لایه سرویس

</aside>

> 4- در مسیر `apps/orders/` یک فایل جدید به نام `services.py` بسازید.

این فایل قرار است "مغز متفکر" بخش فروش ما باشد. ما یک کلاس و یک متد درون آن تعریف می‌کنیم که هیچ ارتباطی با `request`، `response`، یا `JSON` ندارد؛ بلکه فقط با دیتابیس و منطق خالص پایتون کار می‌کند.
> 
> 
> ```python
> from django.db import transaction
> from rest_framework.exceptions import ValidationError
> from apps.carts.models import Cart
> from apps.orders.models import Order, OrderItem
> 
> class OrderService:
>     
>     @staticmethod
>     @transaction.atomic
>     def create_order_from_cart(cart_id, customer):
>         """
>         این سرویس یک سبد خرید را می‌گیرد و آن را به یک فاکتور قطعی تبدیل می‌کند.
>         """
>         # ۱. پیدا کردن سبد خرید به همراه آیتم‌ها و محصولاتش (برای جلوگیری از N+1)
>         try:
>             cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
>         except Cart.DoesNotExist:
>             raise ValidationError("سبد خرید یافت نشد یا قبلاً پرداخت شده است.")
> 
>         # ۲. اگر سبد خرید خالی بود، اجازه ساخت فاکتور نده!
>         if cart.items.count() == 0:
>             raise ValidationError("سبد خرید شما خالی است.")
> 
>         # ۳. ساخت فاکتور اولیه (Header)
>         order = Order.objects.create(customer=customer)
> 
>         # ۴. تبدیل تک‌تک آیتم‌های سبد به آیتم‌های فاکتور
>         order_items_to_create = []
>         for cart_item in cart.items.all():
>             product = cart_item.product
>             
>             # بررسی موجودی انبار در لحظه آخر
>             if product.inventory < cart_item.quantity:
>                 raise ValidationError(f"موجودی محصول '{product.name}' کافی نیست.")
> 
>             # کسر از موجودی انبار
>             product.inventory -= cart_item.quantity
>             product.save()
> 
>             # آماده‌سازی آیتم فاکتور (دقت کنید قیمت همین الان فریز می‌شود)
>             order_items_to_create.append(
>                 OrderItem(
>                     order=order,
>                     product=product,
>                     quantity=cart_item.quantity,
>                     unit_price=product.price  # فریز کردن قیمت!
>                 )
>             )
> 
>         # ۵. ذخیره یکجای تمام آیتم‌ها در دیتابیس (بسیار بهینه‌تر از ذخیره تک‌تک)
>         OrderItem.objects.bulk_create(order_items_to_create)
> 
>         # ۶. حذف سبد خرید (چون تبدیل به فاکتور شد)
>         cart.delete()
> 
>         return order
> ```
> 

### کالبدشکافی لایه سرویس و دکوراتور `@transaction.atomic`

یکی از حیاتی‌ترین خطوط این کد، دکوراتور `@transaction.atomic` است.
تصور کنید مراحل ۱ تا ۴ به خوبی پیش رفت، اما ناگهان در مرحله ۵ برق سرور رفت یا دیتابیس کِرَش کرد! چه می‌شود؟
از انبار کالا کسر شده، فاکتور ناقص ساخته شده، اما سبد خرید پاک نشده است! این یک فاجعه مالی است.

دکوراتور `@transaction.atomic` یک سپر محافظتی دور کل این تابع می‌کشد. این سپر به دیتابیس می‌گوید: **"یا تمام این مراحل را تا آخر خط بی‌نقص انجام بده، یا اگر در هر خطی ارور رخ داد، تمام تغییراتی که تا آن لحظه دادی را برگردان (Rollback) و انگار هیچ اتفاقی نیفتاده است."** این اصل در علوم کامپیوتر به نام ACID شناخته می‌شود و در سیستم‌های فروشگاهی از نان شب واجب‌تر است.

https://fa.wikipedia.org/wiki/%D8%A7%D8%B3%DB%8C%D8%AF_(%D9%BE%D8%A7%DB%8C%DA%AF%D8%A7%D9%87_%D8%AF%D8%A7%D8%AF%D9%87)#1._%D8%AA%D8%AC%D8%B2%DB%8C%D9%87%E2%80%8C%D9%86%D8%A7%D9%BE%D8%B0%DB%8C%D8%B1%DB%8C_(Atomicity)

![image.png](image.png)

ما اکنون پیچیده‌ترین بخش تجاری (Business Logic) پروژه را به تمیزترین شکل ممکن در یک سرویس ایزوله کردیم. این سرویس اکنون آماده است تا توسط API View فراخوانی شود.

### . آیا ایمپورت مستقیم از یک App به App دیگر کار درستی است؟

در دنیای استاندارد جنگو و معماری یکپارچه (Monolith)، **بله، این کار کاملاً رایج و پذیرفته شده است**.
نکته طلایی این است که ما این ایمپورت را **داخل لایه سرویس (`services.py`)** انجام دادیم، نه داخل `models.py`. اگر `models.py` اپلیکیشن سفارشات را به `models.py` سبد خرید متصل می‌کردیم، خطر رخ دادن خطای وحشتناک «ایمپورت حلقوی» (Circular Import) به شدت بالا می‌رفت. با انتقال این منطق به لایه سرویس، ما این خطر را خنثی کردیم.

### ۲. آیا این کار باعث پیچیدگی غیرقابل فهم می‌شود (Tight Coupling)؟

پاسخ صریح: **در مقیاس‌های بسیار بزرگ، بله.**
در مهندسی نرم‌افزار به این حالت **Tight Coupling (وابستگی شدید)** می‌گویند. با این کد، اپلیکیشن `orders` اکنون به اپلیکیشن `carts` زنجیر شده است. اگر فردا بخواهید پروژه را به معماری میکروسرویس (Microservices) تبدیل کنید و سبد خرید را روی یک سرور و سفارشات را روی سروری دیگر بگذارید، این ایمپورت مستقیم باعث شکستن سیستم می‌شود. اما در یک پروژه Monolithic، این میزان از وابستگی در لایه سرویس کاملاً قابل مدیریت است.

### ۳. آیا راه بهتری هم وجود دارد؟

بله، برای کاهش این وابستگی راه‌حل‌های پیشرفته‌تری وجود دارد که نیازمند معماری‌های پیچیده‌تر است:

- **معماری رویدادمحور (Event-Driven Architecture):** در این الگو، اپلیکیشن `carts` و `orders` اصلاً یکدیگر را نمی‌شناسند. وقتی کاربر روی "تکمیل خرید" کلیک می‌کند، سرویس سبد خرید یک سیگنال (Event) در کل سیستم پخش می‌کند: *"یک سبد خرید با موفقیت بسته شد!"*. سپس سرویس سفارشات که در حال گوش دادن به رویدادهاست، این پیام را می‌گیرد و فاکتور را می‌سازد. (در جنگو این کار با Django Signals یا ابزارهایی مثل Celery/RabbitMQ انجام می‌شود).
- **تزریق وابستگی (Dependency Injection):** استفاده از اینترفیس‌ها به جای مدل‌های مستقیم، که البته در پایتون و جنگو کمتر از زبان‌هایی مثل جاوا مرسوم است.

**نکته واقع‌گرایانه:** به عنوان یک برنامه‌نویس بک‌اند، همیشه باید مراقب تله **Over-engineering (مهندسی بیش از حد)** باشید. برای فاز فعلی، همین معماری سه‌لایه (استفاده از `services.py`) یک تعادل عالی بین تمیزی کد و سرعت توسعه است.

<aside>
📢

### . نقش `core/services.py` در نقشه توسعه چیست؟

</aside>

در معماری نرم‌افزار، اپلیکیشن `core` به عنوان **قلب تپنده و زیرساخت مشترک (Shared Infrastructure)** سیستم عمل می‌کند.

وقتی سرویسی می‌نویسیم که فقط مربوط به سبد خرید است، جایش در `apps.carts.services` است. اما سرویس‌هایی در پروژه‌های واقعی وجود دارند که به هیچ Domain خاصی تعلق ندارند و همه اپلیکیشن‌ها به آن‌ها نیاز پیدا می‌کنند. اینجا دقیقاً نقطه استفاده از `core/services.py` است.

**مثال‌های کاربردی برای `core/services.py` در آینده پروژه:**

- **سرویس ارسال پیامک (SMS Service):** فردا می‌خواهید وقتی فاکتور ساخته شد، به کاربر پیامک برود. از طرفی وقتی در پروفایلش ثبت‌نام کرد هم پیامک برود. منطق اتصال به API کاوه‌نگار یا ملی‌پیامک در `core` نوشته می‌شود تا همه جا قابل فراخوانی باشد.
- **سرویس ایمیل (Email Notification):** برای ارسال رسید فاکتور یا فراموشی رمز عبور.
- **تولید فایل PDF:** متدی که یک دیکشنری پایتونی می‌گیرد و یک فایل PDF فاکتور یا گزارش خروجی می‌دهد.
- **ذخیره‌سازی ابری (Cloud Storage):** اگر بخواهید در آینده تصاویر را به جای هارد سرور روی S3 آمازون یا آروان‌کلاد آپلود کنید.

با قرار دادن این سرویس‌های عمومی در `core`، شما از قانون **DRY (Don't Repeat Yourself)** در بالاترین سطح معماری پیروی می‌کنید.

<aside>
📢

کجای کار هستیم؟

</aside>

ما دیتابیس سفارشات (`models.py`) و مغز متفکر سیستم (`services.py`) را ساخته‌ایم. اما کلاینت (فرانت‌اند یا موبایل) چطور باید با این مغز متفکر صحبت کند؟ ما هنوز هیچ «دروازه»ای برای آن نساخته‌ایم.

بنابراین، **مرحله بعدی ما ساخت لایه API (Serializer و View) برای سفارشات است** تا فرآیند تبدیل سبد خرید به فاکتور را به اینترنت متصل کنیم.

<aside>
📢

قدم اول: ساخت Serializerهای سفارش

</aside>

در اینجا ما به دو سریالایزر نیاز داریم: یکی برای **نمایش** فاکتور به کاربر (خروجی)، و دیگری برای **دریافت** درخواست ثبت سفارش (ورودی).

> 5-  در مسیر `apps/orders/` یک فایل جدید به نام `serializers.py` بسازید
> 
> 
> ```python
> from rest_framework import serializers
> from .models import Order, OrderItem
> from apps.carts.models import Cart
> from .services import OrderService
> 
> # ۱. سریالایزر نمایش آیتم‌های فاکتور
> class OrderItemSerializer(serializers.ModelSerializer):
>     # برای نمایش نام محصول به جای فقط آی‌دی آن
>     product_name = serializers.CharField(source='product.name', read_only=True)
>     
>     class Meta:
>         model = OrderItem
>         fields = ['id', 'product_name', 'quantity', 'unit_price']
> 
> # ۲. سریالایزر نمایش کل فاکتور
> class OrderSerializer(serializers.ModelSerializer):
>     items = OrderItemSerializer(many=True, read_only=True)
>     
>     class Meta:
>         model = Order
>         fields = ['id', 'status', 'created_at', 'items']
> 
> # ۳. سریالایزر عملیاتی: فقط برای دریافت آی‌دی سبد خرید و ساخت فاکتور
> class CreateOrderSerializer(serializers.Serializer):
>     cart_id = serializers.UUIDField()
> 
>     def validate_cart_id(self, cart_id):
>         # بررسی اینکه آیا این سبد خرید اصلاً وجود دارد؟
>         if not Cart.objects.filter(id=cart_id).exists():
>             raise serializers.ValidationError("سبد خرید نامعتبر است یا قبلا پرداخت شده است.")
>         return cart_id
> 
>     def save(self, **kwargs):
>         cart_id = self.validated_data['cart_id']
>         
>         # استخراج مشتری از ریکوئست (کاربر باید لاگین باشد)
>         # ما request را از طریق context از سمت View به اینجا پاس می‌دهیم
>         customer = self.context['request'].user.customer
>         
>         # فراخوانی لایه سرویس که در مرحله قبل ساختیم!
>         order = OrderService.create_order_from_cart(cart_id=cart_id, customer=customer)
>         
>         return order
> ```
> 

<aside>
📢

قدم دوم: ساخت Controller یا View

</aside>

حالا باید یک ViewSet بسازیم که درخواست‌های HTTP را مدیریت کند. در اینجا برخلاف سبد خرید، **کاربر حتماً باید لاگین کرده باشد** تا بتواند سفارش ثبت کند.

> 6-  فایل `apps/orders/views.py` را باز کرده و کدهای زیر را وارد کنید:
> 
> 
> ```python
> from rest_framework.viewsets import GenericViewSet
> from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
> from rest_framework.permissions import IsAuthenticated
> from drf_spectacular.utils import extend_schema_view, extend_schema
> from .models import Order
> from .serializers import OrderSerializer, CreateOrderSerializer
> 
> @extend_schema_view(
>     create=extend_schema(summary="تبدیل سبد خرید به سفارش (فاکتور)", tags=['Orders']),
>     list=extend_schema(summary="لیست سفارشات کاربر", tags=['Orders']),
>     retrieve=extend_schema(summary="جزئیات یک سفارش", tags=['Orders']),
> )
> class OrderViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
>     """
>     ویوست مدیریت سفارشات مشتری.
>     دقت کنید که متدهای آپدیت و حذف مسدود شده‌اند، زیرا فاکتور قابل تغییر نیست.
>     """
>     # فقط کاربران لاگین شده حق دسترسی دارند
>     permission_classes = [IsAuthenticated]
> 
>     # هر کاربر فقط باید فاکتورهای خودش را ببیند، نه دیگران را!
>     def get_queryset(self):
>         user = self.request.user
>         
>         # جلوگیری از خطای کاربرانی که هنوز پروفایل Customer ندارند
>         if hasattr(user, 'customer'):
>             return Order.objects.prefetch_related('items__product').filter(customer=user.customer)
>         return Order.objects.none()
> 
>     # انتخاب سریالایزر بر اساس نوع متد (دریافت یا ثبت)
>     def get_serializer_class(self):
>         if self.request.method == 'POST':
>             return CreateOrderSerializer
>         return OrderSerializer
>     
>     # ارسال آبجکت request به سریالایزر برای دسترسی به اطلاعات کاربر
>     def get_serializer_context(self):
>         return {'request': self.request}
> ```
> 

<aside>
📢

قدم سوم: اتصال URLها

</aside>

برای اینکه این API در دسترس قرار بگیرد، باید آن را به سیستم روتر جنگو متصل کنیم.

> 7- در مسیر `apps/orders/` فایل `urls.py` را ایجاد کنید:
> 
> 
> ```python
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import OrderViewSet
> 
> router = DefaultRouter()
> router.register('orders', OrderViewSet, basename='orders')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

> 8- این مسیر را در `apps/api/urls.py` (روتر مرکزی) ثبت کنید:
> 
> 
> ```python
> urlpatterns = [
>     # ... مسیرهای قبلی ...
>     path('', include('apps.carts.urls')),
>     path('', include('apps.orders.urls')), # اضافه شدن مسیر سفارشات
> ]
> ```
> 

### معماری این بخش چگونه کار می‌کند؟ (Flow)

۱. کاربر در فرانت‌اند دکمه **"ثبت سفارش"** را می‌زند.
۲. یک درخواست `POST` حاوی توکن احراز هویت و `cart_id` به سرور می‌آید.
۳. ویوی ما چک می‌کند کاربر لاگین است (`IsAuthenticated`).
۴. دیتا به `CreateOrderSerializer` می‌رود و ولیدیت می‌شود.
۵. سریالایزر به `OrderService` (لایه سرویس) دستور می‌دهد: *"این سبد خرید را بگیر و برای این مشتری فاکتور کن."*
۶. لایه سرویس با دیتابیس درگیر می‌شود، سبد را پاک می‌کند، کالاها را به فاکتور می‌برد و قیمت‌ها را فریز می‌کند.
۷. در نهایت یک فاکتور شیک ساخته شده و کد `201 Created` به کلاینت برمی‌گردد.

با این کدها، چرخه اصلی فروشگاه (از دیدن محصول تا ثبت فاکتور) از نظر منطقی کامل شده است.

<aside>
📢

رفع باگ‌های منطقی در همان لایه‌ای که کشف می‌شوند (مثل همین قفل شدن موجودی انبار)، از انباشته شدن بدهی فنی (Technical Debt) در آینده جلوگیری می‌کند.

</aside>

برای بازگرداندن موجودی انبار، در سیستم‌های مقیاس‌پذیر و به خصوص داشبوردهای پیشرفته مدیریت انبار، معماری استاندارد استفاده از تسک‌های پس‌زمینه با ابزارهایی مانند Celery و Redis است تا سیستم به صورت کاملاً خودکار و در بک‌گراند فاکتورها را بررسی کند. اما از آنجایی که در این فاز هنوز Celery را به پروژه متصل نکرده‌ایم، منطق «بررسی در لحظه» (Just-in-Time) را در لایه سرویس پیاده‌سازی می‌کنیم.

<aside>
📢

بخش اول: پیاده‌سازی منطق انقضای ۱۵ دقیقه‌ای فاکتور

</aside>

ما باید دو متد جدید به «مغز متفکر» سفارشات اضافه کنیم: یکی برای لغو فاکتور و بازگرداندن موجودی انبار، و دیگری برای بررسی زمان سپری شده.

> 9- فایل `apps/orders/services.py` را باز کرده و این تغییرات را به کلاس `OrderService` اضافه کنید: 
ابتدا این ایمپورت‌ها را به بالای فایل اضافه کنید:
> 
> 
> ```python
> from django.utils import timezone
> from datetime import timedelta
> ```
> 
> سپس کدهای زیر را به داخل کلاس `OrderService` (زیر متد قبلی) اضافه کنید:
> 
> ```python
> @staticmethod
>     @transaction.atomic
>     def cancel_expired_order(order):
>         """
>         این متد فاکتور را لغو کرده و موجودی کالاها را به انبار برمی‌گرداند.
>         """
>         # اگر وضعیت فاکتور چیزی غیر از "در انتظار پرداخت" است، کاری نکن
>         if order.status != Order.OrderStatus.PENDING:
>             return False
> 
>         # حلقه روی تمام آیتم‌های فاکتور برای بازگرداندن موجودی
>         # استفاده از select_related برای جلوگیری از مشکل N+1 در ارتباط با جدول Product
>         for item in order.items.select_related('product'):
>             product = item.product
>             product.inventory += item.quantity
>             product.save()
> 
>         # تغییر وضعیت فاکتور به لغو شده
>         order.status = Order.OrderStatus.CANCELED
>         order.save()
>         return True
> 
>     @staticmethod
>     def validate_order_for_payment(order_id):
>         """
>         این متد قبل از ارسال کاربر به درگاه بانکی فراخوانی می‌شود
>         تا بررسی کند آیا هنوز برای پرداخت فرصت دارد یا خیر.
>         """
>         try:
>             order = Order.objects.get(id=order_id)
>         except Order.DoesNotExist:
>             raise ValidationError("سفارش یافت نشد.")
> 
>         if order.status == Order.OrderStatus.COMPLETED:
>             raise ValidationError("این سفارش قبلاً پرداخت شده است.")
>             
>         if order.status == Order.OrderStatus.CANCELED:
>             raise ValidationError("این سفارش لغو شده است.")
> 
>         # محاسبه زمان انقضا (زمان ثبت فاکتور + ۱۵ دقیقه)
>         expiration_time = order.created_at + timedelta(minutes=15)
>         
>         # مقایسه با زمان حال
>         if timezone.now() > expiration_time:
>             # فراخوانی متد بازگرداندن موجودی به انبار
>             OrderService.cancel_expired_order(order)
>             raise ValidationError("زمان ۱۵ دقیقه‌ای پرداخت به پایان رسیده و سفارش به دلیل اتمام مهلت لغو شد.")
>         
>         return order
> ```
> 

با این معماری، هر زمان که بخواهیم کاربر را به درگاه بانکی متصل کنیم، ابتدا متد `validate_order_for_payment` را صدا می‌زنیم. اگر زمان گذشته باشد، سیستم خودکار موجودی را به انبار برمی‌گرداند و جلوی پرداخت را می‌گیرد.

<aside>
📢

بخش دوم: تکمیل پروفایل کاربری (Customer Profile و Address)

</aside>

> 10- به‌روزرسانی مدل‌ها: فایل `apps/customers/models.py` را باز کنید: ما مدل `Customer` را گسترش می‌دهیم و مدل جدیدی به نام `Address` می‌سازیم (چون یک مشتری می‌تواند چندین آدرس داشته باشد: خانه، محل کار و...).
> 
> 
> ```python
> from django.db import models
> from django.conf import settings
> 
> class Customer(models.Model):
>     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
>     phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
>     birth_date = models.DateField(null=True, blank=True)
> 
>     def __str__(self):
>         return f"{self.user.first_name} {self.user.last_name}"
> 
> class Address(models.Model):
>     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
>     province = models.CharField(max_length=50, verbose_name="استان")
>     city = models.CharField(max_length=50, verbose_name="شهر")
>     street = models.TextField(verbose_name="آدرس دقیق (خیابان، پلاک، واحد)")
>     postal_code = models.CharField(max_length=10, verbose_name="کد پستی")
> 
>     def __str__(self):
>         return f"{self.province}, {self.city} - {self.postal_code}"
> ```
> 

> 11- دستور زیر را در ترمینال تکرار کنید:
> 
> 
> ```python
> 	python manage.py makemigrations
> 	python manage.py migrate
> ```
> 

خروجی

```python
$ python manage.py makemigrations orders
Migrations for 'orders':
  apps\orders\migrations\0001_initial.py
    + Create model Order
    + Create model OrderItem

$ python manage.py migrate
Operations to perform:
  Apply all migrations: accounts, admin, auth, carts, contenttypes, customers, orders, products, sessions
Running migrations:
  Applying orders.0001_initial... OK

```

> 12- ساخت سریالایزرها: در مسیر `apps/customers/` فایل `serializers.py` را ایجاد کنید:
> 
> 
> ```python
> from rest_framework import serializers
> from .models import Order, OrderItem
> from apps.carts.models import Cart
> from .services import OrderService
> 
> # ۱. سریالایزر نمایش آیتم‌های فاکتور
> # 1. Serializer to display invoice items
> class OrderItemSerializer(serializers.ModelSerializer):
>     # برای نمایش نام محصول به جای فقط آی‌دی آن
>     # To display the product name instead of just its ID
>     product_name = serializers.CharField(source='product.name', read_only=True)
>     
>     class Meta:
>         model = OrderItem
>         fields = ['id', 'product_name', 'quantity', 'unit_price']
> 
> # ۲. سریالایزر نمایش کل فاکتور
> #2. Serializer to display the entire invoice
> class OrderSerializer(serializers.ModelSerializer):
>     items = OrderItemSerializer(many=True, read_only=True)
>     
>     class Meta:
>         model = Order
>         fields = ['id', 'status', 'created_at', 'items']
> 
> # ۳. سریالایزر عملیاتی: فقط برای دریافت آی‌دی سبد خرید و ساخت فاکتور
> # 3. Operational Serializer: Only for getting the shopping cart ID and creating the invoice
> class CreateOrderSerializer(serializers.Serializer):
>     cart_id = serializers.UUIDField()
> 
>     def validate_cart_id(self, cart_id):
>         # بررسی اینکه آیا این سبد خرید اصلاً وجود دارد؟
>         # Check if this shopping cart even exists?
>         if not Cart.objects.filter(id=cart_id).exists():
>             raise serializers.ValidationError("سبد خرید نامعتبر است یا قبلا پرداخت شده است.")
>         return cart_id
> 
>     def save(self, **kwargs):
>         cart_id = self.validated_data['cart_id']
>         
>         # استخراج مشتری از ریکوئست (کاربر باید لاگین باشد)
>         # ما request را از طریق context از سمت View به اینجا پاس می‌دهیم
>         # Extract the customer from the request (user must be logged in)
>         # We pass the request here via context from the View side
>         customer = self.context['request'].user.customer
>         
>         # فراخوانی لایه سرویس که در مرحله قبل ساختیم!
>         # Call the service layer we created in the previous step!
>         order = OrderService.create_order_from_cart(cart_id=cart_id, customer=customer)
>         
>         return order
>     
> ```
> 

> 13- ساخت Viewها: در مسیر `apps/customers/` فایل `views.py` را باز کنید:
ما به دو API نیاز داریم: یکی برای خواندن و ویرایش پروفایل شخصی، و دیگری برای مدیریت آدرس‌ها.
> 
> 
> ```python
> from rest_framework.viewsets import ModelViewSet
> from rest_framework.generics import RetrieveUpdateAPIView
> from rest_framework.permissions import IsAuthenticated
> from .models import Customer, Address
> from .serializers import CustomerProfileSerializer, AddressSerializer
> 
> class CustomerProfileView(RetrieveUpdateAPIView):
>     """
>     این ویو برای مشاهده و ویرایش پروفایل کاربری خود شخص است.
>     This view is for viewing and editing a person's own user profile.
>     """
>     serializer_class = CustomerProfileSerializer
>     permission_classes = [IsAuthenticated]
> 
>     def get_object(self):
>         # این متد جادویی باعث می‌شود نیازی به ارسال ID در URL نباشد.
>         # کاربر بر اساس توکنی که می‌فرستد، فقط پروفایل خودش را دریافت می‌کند.
>         # This magic method eliminates the need to send the ID in the URL.
>         # The user only gets their own profile based on the token they send.
>         customer, created = Customer.objects.get_or_create(user=self.request.user)
>         return customer
> 
> class AddressViewSet(ModelViewSet):
>     """
>     مدیریت آدرس‌های پستی کاربر
>     Manage user mailing addresses
>     """
>     serializer_class = AddressSerializer
>     permission_classes = [IsAuthenticated]
> 
>     def get_queryset(self):
>         # هر کاربر فقط آدرس‌های خودش را می‌بیند
>         # Each user only sees their own addresses
>         return Address.objects.filter(customer__user=self.request.user)
> 
>     def perform_create(self, serializer):
>         # در زمان ساخت آدرس جدید، فیلد customer به صورت خودکار با کاربر فعلی پر می‌شود
>         # When creating a new address, the customer field is automatically filled with the current user
>         customer, created = Customer.objects.get_or_create(user=self.request.user)
>         serializer.save(customer=customer)
> 
> ```
> 

متد `get_or_create` در ORM جنگو، یک ویژگی خاص دارد: این متد به جای یک آبجکت ساده، همیشه یک **تاپل (Tuple)** دوتایی برمی‌گرداند.

ساختار خروجی این متد به این شکل است: `(object, boolean)`

- **متغیر اول (`customer`):** خودِ آبجکت دیتابیس است (چه آن را پیدا کرده باشد، چه همان لحظه ساخته باشد).
- **متغیر دوم (`created`):** یک مقدار منطقی (True یا False) است.
    - اگر کاربر قبلاً پروفایل `Customer` داشته و جنگو فقط آن را از دیتابیس **خوانده (Get)** باشد، مقدار `created` برابر با `False` می‌شود.
    - اگر کاربر پروفایل نداشته و جنگو همان لحظه یک رکورد جدید برایش **ساخته (Create)** باشد، مقدار `created` برابر با `True` می‌شود.

### چرا آن را نوشتیم ولی در کدهای بعدی از آن استفاده نکردیم؟

در قطعه کدی که من نوشتم، ما عملاً کاری با متغیر `created` نداریم (چون فقط می‌خواستیم پروفایل را به دست بیاوریم). اما **مجبوریم** آن را بنویسیم تا عمل Unpacking (استخراج مقادیر از تاپل) در پایتون به درستی انجام شود.

اگر فقط می‌نوشتیم:

```python
customer = Customer.objects.get_or_create(user=self.request.user)
```

در این حالت، متغیر `customer` تبدیل به یک تاپل می‌شد (مثلاً: `(<Customer Object>, False)`) و وقتی در خط بعدی می‌خواستیم آن را به سریالایزر پاس بدهیم، سیستم کِرَش می‌کرد و ارور می‌داد چون سریالایزر یک آبجکت می‌خواهد، نه یک تاپل!

**دو راه استاندارد برای هندل کردن این موضوع در پایتون وجود دارد:**

1- روشی که استفاده کردیم (خوانا و واضح برای برنامه‌نویسان دیگر):

```python
customer, created = Customer.objects.get_or_create(...)
```

2- استفاده از متغیرِ پنهان `_` (روش مرسوم در پایتون برای متغیرهایی که نیازی به آن‌ها نداریم):

```python
customer, _ = Customer.objects.get_or_create(...)
```

هر دو روش از نظر منطق برنامه‌نویسی کاملاً یکسان عمل می‌کنند.

### چه زمانی متغیر `created` واقعاً به درد می‌خورد؟

در سناریوهای تجاری لایه سرویس، این متغیر به شدت کاربردی است. فرض کنید می‌خواهیم وقتی پروفایل مشتری برای **اولین بار** ساخته می‌شود، یک پیامک یا ایمیل خوش‌آمدگویی برایش ارسال شود. با استفاده از این متغیر به راحتی می‌توانیم این کار را مدیریت کنیم:

```python
customer, created = Customer.objects.get_or_create(user=self.request.user)

if created:
    # این کد فقط زمانی اجرا می‌شود که رکورد جدیدی در دیتابیس ثبت شده باشد
    # مثلا: فراخوانی سرویس پیامک
    SmsService.send_welcome_message(customer.user.first_name)
```

پس در کدهای مربوط به این مرحله از توسعه ما، حضور `created` صرفاً برای تفکیک درست خروجیِ متدِ جنگو بود تا بتوانیم بدون خطا متغیر `customer` را استخراج کنیم.

> 14-  تنظیم مسیرها: در مسیر `apps/customers/` فایل `urls.py` را ایجاد کنید:
> 
> 
> ```python
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CustomerProfileView, AddressViewSet
> 
> router = DefaultRouter()
> router.register('addresses', AddressViewSet, basename='addresses')
> 
> urlpatterns = [
>     path('profile/', CustomerProfileView.as_view(), name='customer-profile'),
>     path('', include(router.urls)),
> ]
> ```
> 

<aside>
📢

### تا اینجا در معماری سیستم چه اتفاقی افتاده است؟

</aside>

**ما با موفقیت «ستون فقرات تراکنش‌های مالی» سیستم را ساختیم. در ذهن خود این جریان داده را تجسم کنید:**

1. **موجودیت موقت (Cart):** کاربر وارد سایت می‌شود و شروع به انتخاب کالا می‌کند. این اطلاعات در سبد خرید ذخیره می‌شود. سبد خرید بی‌ثبات است؛ کالاها کم و زیاد می‌شوند و قیمت‌ها با نوسان دیتابیس تغییر می‌کنند.
2. **موجودیت دائمی و فریز شده (Order):** به محض اینکه کاربر تصمیم به خرید می‌گیرد، لایه سرویسِ ما (همان `OrderService`) وارد عمل می‌شود. این لایه مثل یک دروازه‌بان، سبد خرید را از بین می‌برد، موجودی انبار را کسر می‌کند و یک «عکسِ ثابت و غیرقابل تغییر» از قیمت و کالاها به نام فاکتور (Order) ثبت می‌کند.
3.  **هویت مشتری (Customer & Address):** همزمان، ما فضایی ساختیم تا این فاکتورهای بی‌صاحب، به یک انسان واقعی با آدرس پستی دقیق متصل شوند.

<aside>
📢

راهنمای تست بصری و عملیاتی (قدم به قدم در Swagger)

</aside>

برای اینکه این مفاهیم انتزاعی را در عمل ببینید، پروژه را `runserver` کنید و آدرس

 `http://127.0.0.1:8000/api/schema/swagger-ui/` را در مرورگر باز کنید. 

مسیر زیر را دقیقاً به همین ترتیب طی کنید:

<aside>
📢

**قدم اول: احراز هویت (ورود به سیستم)**

</aside>

1. در Swagger به بخش `token` (احتمالاً `POST /api/token/`) بروید.
2. یوزرنیم و پسورد کاربری که قبلاً ساخته‌اید را وارد کنید و `Execute` را بزنید.
3. مقدار `access` توکن را کپی کنید، روی دکمه قفل سبز رنگ (Authorize) در بالای صفحه کلیک کرده و توکن را آنجا قرار دهید. اکنون شما به عنوان یک کاربر لاگین شده شناخته می‌شوید.

<aside>
📢

**قدم دوم: هویت‌بخشی و ثبت آدرس (دستاوردهای جدید)**

</aside>

1. **ساخت/مشاهده پروفایل:** به مسیر `GET /api/customers/profile/` بروید و `Execute` کنید. خواهید دید که سیستم به صورت خودکار (به لطف همان متد `get_or_create`) پروفایل شما را می‌سازد و اطلاعات اولیه را برمی‌گرداند.
2. **ثبت آدرس پستی:** به مسیر `POST /api/customers/addresses/` بروید. در بخش بدنه (Body)، اطلاعات یک آدرس تستی (استان، شهر، خیابان، کد پستی) را وارد و `Execute` کنید. باید کد `201 Created` بگیرید.

<aside>
📢

**قدم سوم: چرخه‌ی خرید (آماده‌سازی سبد)**

</aside>

1. یک سبد خرید در `POST /api/carts/` بسازید (آی‌دی `cart_id` را کپی کنید).
2. یک یا چند محصول تستی را از طریق `POST /api/cart-items/` به این سبد خرید اضافه کنید.

<aside>
📢

**قدم چهارم: لحظه‌ی جادویی لایه سرویس (تبدیل سبد به فاکتور)**

</aside>

1. حالا به سراغ مسیر `POST /api/orders/` بروید.
2. در بدنه درخواست، فقط `cart_id` که در مرحله قبل کپی کرده بودید را وارد کنید و `Execute` را بزنید.
3. **نتیجه‌ای که باید ببینید:** یک فاکتور کامل (Order) با وضعیت `P` (در انتظار پرداخت) به شما نمایش داده می‌شود. قیمت‌ها در فیلد `unit_price` ثبت شده‌اند.
4. **تست عمیق‌تر:** اگر الان دوباره سعی کنید سبد خریدِ قبلی را با متد `GET` فراخوانی کنید، ارور ۴۰۴ می‌گیرید، چون لایه سرویس ما آن سبد را پس از تبدیل به فاکتور، با موفقیت معدوم کرده است! همچنین اگر پنل ادمین محصولات را چک کنید، می‌بینید که موجودی انبار کسر شده است.

<aside>
📢

**مرحله‌ی بعدی توسعه چیست؟**

</aside>

ما الان یک فاکتورِ در انتظار پرداخت داریم و موجودی انبار را هم برای این مشتری رزرو (کسر) کرده‌ایم. در دنیای واقعی کسب‌وکار، قدم منطقی بعدی دریافت پول است!

ایستگاه بعدی ما باید **فاز پرداخت (Payment Domain)** باشد. در این مرحله باید:

- جدولی برای ثبت تراکنش‌های مالی (Payments) بسازیم که به سفارش (Order) متصل باشد.
- معماری اتصال به درگاه پرداخت (مثل زرین‌پال یا یک درگاه شبیه‌ساز تستی) را پیاده‌سازی کنیم.
- پس از پرداخت موفق، وضعیت فاکتور را از `PENDING` به `COMPLETED` تغییر دهیم.

<aside>
📢

# پایان Part-7

</aside>
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-8.md`
```md
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
```

### File: `apps\Documentation\Markdown document\ACRON Methodology Part-9.md`
```md
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
```

### File: `apps\notifications\__init__.py`
```python

```

### File: `apps\notifications\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `apps\notifications\apps.py`
```python
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = 'apps.notifications'

```

### File: `apps\notifications\models.py`
```python
from django.db import models

# Create your models here.

```

### File: `apps\notifications\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\notifications\views.py`
```python
from django.shortcuts import render

# Create your views here.

```

### File: `apps\orders\__init__.py`
```python

```

### File: `apps\orders\admin.py`
```python
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    # فاکتور نهایی نباید توسط ادمین دستکاری شود تا جلوی فساد مالی گرفته شود
    readonly_fields = ['product', 'quantity', 'unit_price']
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['id', 'customer__user__username']
    inlines = [OrderItemInline]
    
    # سفارشات ثبت شده نباید خودسرانه حذف شوند
    def has_delete_permission(self, request, obj=None):
        return False



```

### File: `apps\orders\apps.py`
```python
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'apps.orders'

```

### File: `apps\orders\models.py`
```python
import uuid

from django.db import models

from apps.customers.models import Customer, Address

from apps.products.models import Product



class Order(models.Model):
    # ۱. تعریف وضعیت‌های مختلف یک سفارش با استفاده از TextChoices
    class OrderStatus(models.TextChoices):
        PENDING = 'P', 'در انتظار پرداخت'
        COMPLETED = 'C', 'پرداخت موفق'
        CANCELED = 'X', 'لغو شده'

    # ۲. شناسه یکتا و غیرقابل حدس برای پیگیری سفارش
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ۳. ارتباط با مشتری (سفارش برخلاف سبد خرید، حتماً صاحب دارد)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
    
    # ۴. وضعیت فعلی سفارش
    status = models.CharField(
        max_length=1, 
        choices=OrderStatus.choices, 
        default=OrderStatus.PENDING
    )
    
    # ۵. زمان ثبت سفارش
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.user.username}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveSmallIntegerField()
    
    # 6. The most important field of this phase: Freezing the price!
    # ۶. مهم‌ترین فیلد این فاز: فریز کردن قیمت!
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"









```

### File: `apps\orders\serializers.py`
```python
from rest_framework import serializers

from .models import Order, OrderItem

from apps.carts.models import Cart

from .services import OrderService

# ۱. سریالایزر نمایش آیتم‌های فاکتور
class OrderItemSerializer(serializers.ModelSerializer):
    # برای نمایش نام محصول به جای فقط آی‌دی آن
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'quantity', 'unit_price']


# ۲. سریالایزر نمایش کل فاکتور
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'status', 'created_at', 'items']


# ۳. سریالایزر عملیاتی: فقط برای دریافت آی‌دی سبد خرید و ساخت فاکتور
class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        # بررسی اینکه آیا این سبد خرید اصلاً وجود دارد؟
        if not Cart.objects.filter(id=cart_id).exists():
            raise serializers.ValidationError("سبد خرید نامعتبر است یا قبلا پرداخت شده است.")
        return cart_id

    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        
        # استخراج مشتری از ریکوئست (کاربر باید لاگین باشد)
        # ما request را از طریق context از سمت View به اینجا پاس می‌دهیم
        customer = self.context['request'].user.customer
        
        # فراخوانی لایه سرویس که در مرحله قبل ساختیم!
        order = OrderService.create_order_from_cart(cart_id=cart_id, customer=customer)
        
        return order


```

### File: `apps\orders\services.py`
```python
from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from rest_framework.exceptions import ValidationError

from apps.carts.models import Cart

from apps.orders.models import Order, OrderItem


class OrderService:
    """
    This service takes a shopping cart and converts it into a finalized invoice (order).
    """  
    @staticmethod
    @transaction.atomic
    def create_order_from_cart(cart_id, customer):
        """
        این سرویس یک سبد خرید را می‌گیرد و آن را به یک فاکتور قطعی تبدیل می‌کند.
        """
        # ۱. پیدا کردن سبد خرید به همراه آیتم‌ها و محصولاتش (برای جلوگیری از N+1)
        try:
            cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
        except Cart.DoesNotExist:
            raise ValidationError("سبد خرید یافت نشد یا قبلاً پرداخت شده است.")

        # ۲. اگر سبد خرید خالی بود، اجازه ساخت فاکتور نده!
        if cart.items.count() == 0:
            raise ValidationError("سبد خرید شما خالی است.")

        # ۳. ساخت فاکتور اولیه (Header)
        order = Order.objects.create(customer=customer)

        # ۴. تبدیل تک‌تک آیتم‌های سبد به آیتم‌های فاکتور
        order_items_to_create = []
        for cart_item in cart.items.all():
            product = cart_item.product
            
            # بررسی موجودی انبار در لحظه آخر
            if product.inventory < cart_item.quantity:
                raise ValidationError(f"موجودی محصول '{product.name}' کافی نیست.")

            # کسر از موجودی انبار
            product.inventory -= cart_item.quantity
            product.save()

            # آماده‌سازی آیتم فاکتور (دقت کنید قیمت همین الان فریز می‌شود)
            order_items_to_create.append(
                OrderItem(
                    order=order,
                    product=product,
                    quantity=cart_item.quantity,
                    unit_price=product.price  # فریز کردن قیمت!
                )
            )

        # ۵. ذخیره یکجای تمام آیتم‌ها در دیتابیس (بسیار بهینه‌تر از ذخیره تک‌تک)
        OrderItem.objects.bulk_create(order_items_to_create)

        # ۶. حذف سبد خرید (چون تبدیل به فاکتور شد)
        cart.delete()

        return order

    @staticmethod
    @transaction.atomic
    def cancel_expired_order(order):
        """
        این متد فاکتور را لغو کرده و موجودی کالاها را به انبار برمی‌گرداند.
        """
        # اگر وضعیت فاکتور چیزی غیر از "در انتظار پرداخت" است، کاری نکن
        if order.status != Order.OrderStatus.PENDING:
            return False

        # حلقه روی تمام آیتم‌های فاکتور برای بازگرداندن موجودی
        # استفاده از select_related برای جلوگیری از مشکل N+1 در ارتباط با جدول Product
        for item in order.items.select_related('product'):
            product = item.product
            product.inventory += item.quantity
            product.save()

        # تغییر وضعیت فاکتور به لغو شده
        order.status = Order.OrderStatus.CANCELED
        order.save()
        return True

    @staticmethod
    def validate_order_for_payment(order_id):
        """
        این متد قبل از ارسال کاربر به درگاه بانکی فراخوانی می‌شود
        تا بررسی کند آیا هنوز برای پرداخت فرصت دارد یا خیر.
        """
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise ValidationError("سفارش یافت نشد.")

        if order.status == Order.OrderStatus.COMPLETED:
            raise ValidationError("این سفارش قبلاً پرداخت شده است.")
            
        if order.status == Order.OrderStatus.CANCELED:
            raise ValidationError("این سفارش لغو شده است.")

        # محاسبه زمان انقضا (زمان ثبت فاکتور + ۱۵ دقیقه)
        expiration_time = order.created_at + timedelta(minutes=15)
        
        # مقایسه با زمان حال
        if timezone.now() > expiration_time:
            # فراخوانی متد بازگرداندن موجودی به انبار
            OrderService.cancel_expired_order(order)
            raise ValidationError("زمان ۱۵ دقیقه‌ای پرداخت به پایان رسیده و سفارش به دلیل اتمام مهلت لغو شد.")
        
        return order





```

### File: `apps\orders\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\orders\urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]


```

### File: `apps\orders\views.py`
```python
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import Order
from .serializers import OrderSerializer, CreateOrderSerializer

@extend_schema_view(
    create=extend_schema(summary="تبدیل سبد خرید به سفارش (فاکتور)", tags=['Orders']),
    list=extend_schema(summary="لیست سفارشات کاربر", tags=['Orders']),
    retrieve=extend_schema(summary="جزئیات یک سفارش", tags=['Orders']),
)
class OrderViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """
    ویوست مدیریت سفارشات مشتری.
    دقت کنید که متدهای آپدیت و حذف مسدود شده‌اند، زیرا فاکتور قابل تغییر نیست.
    """
    # فقط کاربران لاگین شده حق دسترسی دارند
    permission_classes = [IsAuthenticated]

    # هر کاربر فقط باید فاکتورهای خودش را ببیند، نه دیگران را!
    def get_queryset(self):
        user = self.request.user
        
        # جلوگیری از خطای کاربرانی که هنوز پروفایل Customer ندارند
        if hasattr(user, 'customer'):
            return Order.objects.prefetch_related('items__product').filter(customer=user.customer)
        return Order.objects.none()

    # انتخاب سریالایزر بر اساس نوع متد (دریافت یا ثبت)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer
    
    # ارسال آبجکت request به سریالایزر برای دسترسی به اطلاعات کاربر
    def get_serializer_context(self):
        return {'request': self.request}



```

### File: `apps\payments\__init__.py`
```python

```

### File: `apps\payments\admin.py`
```python
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'order', 'amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['transaction_id', 'order__id']
    
    # تمام فیلدهای مالی را برای ادمین Read-Only می‌کنیم تا امنیت حفظ شود
    readonly_fields = ['transaction_id', 'order', 'amount', 'status', 'created_at', 'updated_at']

    def has_add_permission(self, request):
        return False # ادمین نباید بتواند دستی تراکنش مالی خلق کند

    def has_delete_permission(self, request, obj=None):
        return False # تراکنش مالی هرگز نباید حذف شود



```

### File: `apps\payments\apps.py`
```python
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    name = 'apps.payments'

```

### File: `apps\payments\models.py`
```python
#  import models from django.db for defining the Payment model
from django.db import models

# import uuid for generating unique transaction IDs
import uuid

#  import the Order model from the orders app to establish a relationship with the Payment model
from apps.orders.models import Order

# Define the Payment model to represent payment transactions associated with orders
class Payment(models.Model):
    """
    Model representing a payment transaction for an order.
    Each order can have only one active payment record.
    """
    class PaymentStatus(models.TextChoices):
        PENDING = 'P', 'در انتظار پرداخت'
        SUCCESS = 'S', 'موفق'
        FAILED = 'F', 'ناموفق'

    # هر فاکتور فقط یک رکورد پرداخت فعال دارد
    # var order is a one-to-one relationship with the Order model, 
    # ensuring that each order can have only one associated payment record.
    # The on_delete=models.PROTECT option prevents deletion of the order if a payment exists,
    # and related_name='payment' allows reverse access from the Order model to its associated Payment.
    order = models.OneToOneField(Order, on_delete=models.PROTECT, related_name='payment')

    # The amount field represents the transaction amount for the payment.
    amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="مبلغ تراکنش")
    

    # کد رهگیری یکتای سیستم ما (به جای کد مرچنت بانک)
    # The transaction_id field is 
    # a UUIDField that generates a unique identifier for each payment transaction.
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # status field represents the current status of the payment,
    # using the PaymentStatus choices defined above. The default status is set to PENDING.
    status = models.CharField(max_length=1, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    

    # ثبت زمان‌های دقیق برای پیگیری‌های مالی
    # The created_at and updated_at fields are DateTimeFields 
    # that automatically record the timestamp of when the payment record is 
    # created and last updated, respectively.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # The __str__ method provides a human-readable representation of the Payment instance,
    # displaying the transaction ID and current status 
    # for easy identification in the admin interface or logs.
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.status}"




```

### File: `apps\payments\serializers.py`
```python
# serializers for payments app, connected to the mock bank callback endpoint

# why import serializers from rest_framework? 
# because we are using DRF to build our API endpoints, 
# and DRF provides a powerful and,
# flexible way to serialize and deserialize data. 
# The serializers module provides classes,
# that help convert complex data types, such as Django models, 
# into native Python datatypes that can then be easily rendered into JSON, 
# XML or other content types. 
# It also provides validation and deserialization of input data.
from rest_framework import serializers

# what is InitiatePaymentSerializer?
# InitiatePaymentSerializer is a serializer class that defines the structure of the data
class InitiatePaymentSerializer(serializers.Serializer):
    # This line was modified to match the orders database
    order_id = serializers.UUIDField()


# what is MockBankCallbackSerializer?
# MockBankCallbackSerializer is a serializer class,
# that defines the structure of the callback data from the mock bank
class MockBankCallbackSerializer(serializers.Serializer):
    transaction_id = serializers.UUIDField()
    is_successful = serializers.BooleanField(default=True, help_text="تیک بزنید تا پرداخت موفق شبیه‌سازی شود")




```

### File: `apps\payments\services.py`
```python
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

from apps.shipments.services import ShipmentService  # <--- اضافه کردن این ایمپورت


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
            
                        # === اتصال زنجیره معماری ===
            # به محض موفقیت پرداخت، به صورت خودکار دستور خروج از انبار صادر می‌شود
            ShipmentService.create_shipment(payment.order)

        else:
            # تغییر وضعیت پرداخت به ناموفق
            # دقت کنید: فاکتور را لغو نمی‌کنیم تا کاربر بتواند در فرصت ۱۵ دقیقه‌ای دوباره تلاش کند
            payment.status = Payment.PaymentStatus.FAILED
            
        payment.save()
        return payment





```

### File: `apps\payments\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\payments\urls.py`
```python
# This file defines the URL patterns for the payments app, 
# which includes endpoints for initiating payments and simulating bank callbacks.
from django.urls import path, include

# Importing DefaultRouter from Django REST framework,
# to automatically generate URL patterns for the PaymentViewSet.
from rest_framework.routers import DefaultRouter

# This import statement brings in the PaymentViewSet class,
# from the views module of the payments app, 
# which contains the logic for handling payment-related actions.
from .views import PaymentViewSet

# This block of code sets up a router for the payments app,
# registering the PaymentViewSet with the router under the 'payments' prefix.
router = DefaultRouter()
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
]




```

### File: `apps\payments\views.py`
```python
# This is a Django viewset for handling payment-related actions, 
# including initiating payments and simulating bank callbacks for testing purposes.
from rest_framework.viewsets import GenericViewSet

# Importing necessary modules from Django REST framework,
# for handling HTTP responses, actions, and permissions.
from rest_framework.response import Response

# Importing decorators and permissions to manage access control for the viewset actions.
from rest_framework.decorators import action

# Why are we importing IsAuthenticated and AllowAny?
# We import IsAuthenticated to ensure that only authenticated users can initiate payments,
from rest_framework.permissions import IsAuthenticated, AllowAny

# Why are we importing extend_schema?
# We import extend_schema from drf_spectacular to provide detailed API documentation for the view
from drf_spectacular.utils import extend_schema

# Why are we importing serializers and services?
# We import serializers to validate and serialize the incoming request data for initiating payments
from .serializers import InitiatePaymentSerializer, MockBankCallbackSerializer

# Why are we importing PaymentService?
# We import PaymentService to handle the business logic related to payment processing,
from .services import PaymentService

# What is the purpose of the PaymentViewSet class?
# The PaymentViewSet class 
# is a Django viewset that provides endpoints for initiating payments and simulating bank callbacks.
class PaymentViewSet(GenericViewSet):
    
    @extend_schema(request=InitiatePaymentSerializer, summary="درخواست تولید لینک پرداخت", tags=['Payments'])
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def initiate(self, request):
        serializer = InitiatePaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        order_id = serializer.validated_data['order_id']
        
        # ارسال به هسته مرکزی پرداخت
        url, trx_id = PaymentService.initiate_payment(order_id, request.user)
        
        return Response({
            "message": "لینک پرداخت با موفقیت تولید شد.",
            "gateway_url": url,
            "transaction_id": trx_id
        })

    @extend_schema(request=MockBankCallbackSerializer, summary="شبیه‌ساز درگاه بانک (تست)", tags=['Payments'])
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def mock_verify(self, request):
        """
        این ویو نقش بانک را بازی می‌کند. 
        در دنیای واقعی، بانک پس از پرداخت کاربر، اطلاعات را به یک URL مشابه این می‌فرستد.
        """
        serializer = MockBankCallbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        trx_id = serializer.validated_data['transaction_id']
        is_successful = serializer.validated_data['is_successful']
        
        payment = PaymentService.verify_mock_payment(trx_id, is_successful)
        
        return Response({
            "payment_status": payment.get_status_display(),
            "order_status": payment.order.get_status_display()
        })




```

### File: `apps\products\__init__.py`
```python

```

### File: `apps\products\admin.py`
```python
from django.contrib import admin

from .models import Category, Brand, Product, ProductMedia # مدل‌های جدید اضافه شدند


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # ۱. مشخص کردن ستون‌هایی که در لیست ادمین نمایش داده می‌شوند
    list_display = ['name', 'slug', 'parent']

    # ۲. جادوی پر شدن خودکار اسلاگ بر اساس نام
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



# ۱. ساخت کلاس اینلاین برای گالری فرعی
class ProductMediaInline(admin.TabularInline):
    model = ProductMedia
    extra = 1          # تعداد ردیف‌های خالی که به صورت پیش‌فرض نمایش داده می‌شود
    max_num = 10       # قفل کردن فرانت‌اند ادمین روی حداکثر ۱۰ فایل فرعی


# ۲. ساخت کلاس مدیریت اصلی محصول
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # الف) ستون‌های نمایشی در جدول لیست محصولات
    list_display = ['name', 'brand', 'category', 'price', 'inventory', 'created_at']
    
    # ب) باکس فیلتر در سمت راست پنل ادمین
    list_filter = ['category', 'brand', 'created_at']
    
    # ج) باکس جستجوی پیشرفته
    search_fields = ['name', 'description']
    
    # د) پر شدن خودکار اسلاگ محصول بر اساس نام آن
    prepopulated_fields = {'slug': ('name',)}
    
    # هـ) تزریق گالری فرعی به انتهای صفحه محصول
    inlines = [ProductMediaInline]




```

### File: `apps\products\apps.py`
```python
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'apps.products'

```

### File: `apps\products\models.py`
```python
import os
import cv2
import tempfile # این کتابخانه استاندارد پایتون باید اضافه شود

from django.db import models
from django.core.exceptions import ValidationError




def validate_media_file(file):
    # الف) بررسی حجم فایل (400 مگابایت به بایت)
    max_size_mb = 400
    max_size_bytes = max_size_mb * 1024 * 1024
    if file.size > max_size_bytes:
        raise ValidationError(f"حجم فایل نمی‌تواند بیشتر از {max_size_mb} مگابایت باشد.")

    # ب) بررسی مدت زمان ویدیو (اگر فایل ویدیو بود)
    file_name = file.name.lower()
    if file_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):
        
        # ۱. ساخت یک فایل موقت فیزیکی و امن روی سیستم‌عامل
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
            # ۲. خواندن فایل جنگو به صورت تکه‌تکه و نوشتن در فایل موقت
            for chunk in file.chunks():
                temp_video.write(chunk)
            temp_video_path = temp_video.name

        try:
            # ۳. دادن آدرس فایل فیزیکی موقت به OpenCV
            video = cv2.VideoCapture(temp_video_path)
            
            frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
            fps = video.get(cv2.CAP_PROP_FPS)
            
            if fps > 0:
                duration_seconds = frames / fps
                if duration_seconds > 120:
                    raise ValidationError("مدت زمان ویدیو نمی‌تواند بیشتر از ۲ دقیقه باشد.")
        finally:
            # ۴. پاکسازی (بسیار مهم): آزادسازی رم و حذف فایل موقت از روی هارد
            if 'video' in locals():
                video.release()
            if os.path.exists(temp_video_path):
                os.remove(temp_video_path)


class Category(models.Model):
    # دسته‌بندی والد (برای ساختار درختی)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name='children'
    )
    
    name = models.CharField(max_length=255)
    
    # اسلاگ برای 
    # URL
    # های سئو-محور
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    
    description = models.TextField(blank=True)
    
    # تصویر دسته‌بندی
    image = models.ImageField(upload_to='categories/%Y/%m/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='brands/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    # استفاده از 
    # Decimal
    # برای قیمت‌ها الزامی است
    inventory = models.PositiveIntegerField(default=0) # موجودی کالا نباید منفی باشد
    
    # تصویر اصلی محصول (اجباری)
    main_image = models.ImageField(upload_to='products/main/%Y/%m/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ۳. ساخت مدل گالری فرعی (تصاویر و ویدیوها)
class ProductMedia(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media_gallery')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    
    # استفاده از 
    # FileField
    #  چون هم عکس را قبول می‌کند و هم ویدیو را
    file = models.FileField(upload_to='products/gallery/%Y/%m/', validators=[validate_media_file])

    # متد 
    # clean
    #  برای محدود کردن تعداد کل مدیاهای یک محصول به حداکثر ۱۰ عدد
    def clean(self):
        super().clean()
        # شمارش مدیاهای فعلی این محصول در دیتابیس (بدون احتساب رکوردی که الان دارد ذخیره می‌شود)
        if self.product_id:
            existing_media_count = ProductMedia.objects.filter(product=self.product).exclude(pk=self.pk).count()
            if existing_media_count >= 10:
                raise ValidationError("شما نمی‌توانید بیشتر از ۱۰ فایل فرعی (تصویر/ویدیو) برای یک محصول آپلود کنید.")

    def save(self, *args, **kwargs):
        # قبل از ذخیره نهایی در دیتابیس، حتماً متد 
        # clean
        #  را صدا می‌زنیم تا ولیدیشن‌ها اجرا شوند
        self.full_clean()
        super().save(*args, **kwargs)



      
        

```

### File: `apps\products\serializers.py`
```python
from rest_framework import serializers

from . import models

# ۱. سریالایزر دسته‌بندی
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'slug']

# ۲. سریالایزر برند
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ['id', 'name', 'slug', 'image']

# ۳. سریالایزر گالری مدیا
class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductMedia
        fields = ['id', 'media_type', 'file']

# ۴. سریالایزر اصلی محصول (Master Serializer)
class ProductSerializer(serializers.ModelSerializer):
    # الف) Nested Serializers برای فیلدهای کلید خارجی (ForeignKey)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    
    # ب) Nested Serializer برای رابطه معکوس (گالری)
    media_gallery = ProductMediaSerializer(many=True, read_only=True)
 
    class Meta:
        model = models.Product
        fields = [
            'id', 
            'name', 
            'slug', 
            'description', 
            'price', 
            'inventory', 
            'main_image',
            'category', 
            'brand', 
            'media_gallery', # اضافه کردن گالری به خروجی نهایی
            'created_at'
        ]




```

### File: `apps\products\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\products\urls.py`
```python
from rest_framework.routers import DefaultRouter


from .views import ProductViewSet

# استفاده از روتر برای تولید خودکار 
# URL
# ها
router = DefaultRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = router.urls



```

### File: `apps\products\views.py`
```python
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Product
from .serializers import ProductSerializer

# تعریف 
# Swagger
#  فقط یک‌بار در بالای 
# ViewSet
@extend_schema_view(
    list=extend_schema(
        summary="دریافت لیست محصولات",
        description="لیست تمامی محصولات به همراه برند، دسته‌بندی و گالری تصاویر.",
        tags=['Products Catalog'],
    ),
    retrieve=extend_schema(
        summary="دریافت جزئیات محصول",
        description="اطلاعات کامل یک محصول بر اساس Slug.",
        tags=['Products Catalog'],
    )
)
class ProductViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    queryset = Product.objects.select_related(
        'category', 
        'brand'
    ).prefetch_related(
        'media_gallery'
    ).all()



    
```

### File: `apps\reviews\__init__.py`
```python

```

### File: `apps\reviews\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `apps\reviews\apps.py`
```python
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    name = 'reviews'

```

### File: `apps\reviews\models.py`
```python
from django.db import models

# Create your models here.

```

### File: `apps\reviews\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\reviews\views.py`
```python
from django.shortcuts import render

# Create your views here.

```

### File: `apps\shipments\__init__.py`
```python

```

### File: `apps\shipments\admin.py`
```python
from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'status', 'carrier', 'tracking_number', 'created_at']
    list_filter = ['status', 'carrier', 'created_at']
    search_fields = ['order__id', 'tracking_number']
    
    # سفارش مربوطه نباید در انبار جابجا شود
    readonly_fields = ['order', 'created_at', 'shipped_at', 'delivered_at']
    
    fieldsets = (
        ("اطلاعات پایه سفارش", {
            'fields': ('order', 'created_at')
        }),
        ("وضعیت لجستیک و انبارداری", {
            'fields': ('status', 'carrier', 'tracking_number')
        }),
        ("زمان‌بندی‌های ارسال", {
            'fields': ('shipped_at', 'delivered_at'),
            'classes': ('collapse',) # این بخش را پنهان میکند تا صفحه شلوغ نشود
        }),
    )




```

### File: `apps\shipments\apps.py`
```python
from django.apps import AppConfig


class ShipmentsConfig(AppConfig):
    name = 'apps.shipments'

```

### File: `apps\shipments\models.py`
```python
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




```

### File: `apps\shipments\serializers.py`
```python
from rest_framework import serializers
from .models import Shipment

class ShipmentTrackerSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    carrier_display = serializers.CharField(source='get_carrier_display', read_only=True)
    tracking_url = serializers.CharField(source='get_tracking_url', read_only=True)

    class Meta:
        model = Shipment
        fields = [
            'id', 'status', 'status_display', 'carrier', 
            'carrier_display', 'tracking_number', 'tracking_url',
            'created_at', 'shipped_at', 'delivered_at'
        ]
        
        

```

### File: `apps\shipments\services.py`
```python
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





```

### File: `apps\shipments\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `apps\shipments\urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerShipmentViewSet

router = DefaultRouter()
router.register('track', CustomerShipmentViewSet, basename='shipment-track')

urlpatterns = [
    path('', include(router.urls)),
]



```

### File: `apps\shipments\views.py`
```python
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Shipment

from .serializers import ShipmentTrackerSerializer



class CustomerShipmentViewSet(ReadOnlyModelViewSet):
    """
    ویو فقط خواندنی (ReadOnly) برای اینکه کاربران وضعیت مرسوله خود را تعقیب کنند.
    """
    serializer_class = ShipmentTrackerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # هر کاربر فقط مرسوله‌ای را می‌بیند که فاکتور آن متعلق به خودش است
        return Shipment.objects.filter(order__customer__user=self.request.user)
        
        
    

```

### File: `config\__init__.py`
```python

```

### File: `config\asgi.py`
```python
"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

```

### File: `config\urls.py`
```python
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),



    # ------------------- Swagger URLs ------------------- #
    # ۱. تولید فایل خام 
    # OpenAPI
    #  (به فرمت YAML/JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # ۲. رابط کاربری گرافیکی 
    # Swagger
    #  (توسعه‌دهندگان بک‌اند و فرانت‌اند)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # ۳. رابط کاربری 
    # Redoc
    #  (جایگزین Swagger، مناسب برای ارائه به مدیران)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]



if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()



```

### File: `config\wsgi.py`
```python
"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

```

### File: `config\zxcZXCsettings.txt`
```txt
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 6.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1r%tnk@im4n@uk5zx!q*i@wkr69darorwnglm%sa!_1ou=8#_w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

```

### File: `config\settings\__init__.py`
```python
from .development import *


```

### File: `config\settings\base.py`
```python
# This file is part of the Django settings for the project. 
# It contains base configurations that are common across different environments 
# (like development, testing, and production).

# why import os and sys?
# The os module is used for interacting with the operating system,
import os

# why import sys?
# The sys module provides access to some variables used or maintained by the interpreter
from pathlib import Path

# why import sys?
# The sys module provides access to some variables used or maintained by the interpreter
import sys


# why import timedelta?
# The timedelta class is used to represent a duration,
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#  BASE_DIR is defined as the parent directory of the current file's parent directory.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# The SECRET_KEY is a critical setting in Django that is used for cryptographic signing.
# It should be kept secret in production environments to ensure the security of the application.
SECRET_KEY = 'django-insecure-1r%tnk@im4n@uk5zx!q*i@wkr69darorwnglm%sa!_1ou=8#_w'

# Security warning: don't run with debug turned on in production!
# The DEBUG setting controls whether Django will display detailed error pages.
# It should be set to False in production to avoid exposing sensitive information.
ALLOWED_HOSTS = []



# Application definition
# The INSTALLED_APPS setting defines the list of applications that are enabled in this Django project.
# It includes both built-in Django apps and custom apps created for the project.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Third party
    # The third-party apps listed here are additional packages 
    # that provide extra functionality to the Django project.
    'rest_framework',
    'drf_spectacular', # مستندسازی API


    # CREATE by me
    # The custom apps listed here are specific to this project 
    # and contain the business logic and models for different parts of the application.
    'apps.accounts',
    'apps.api',
    'apps.carts',
    'apps.customers',
    # 'apps.notifications',
    'apps.orders',
    'apps.payments',
    'apps.products',
    # 'apps.reviews',
    'apps.shipments',
]

# The MIDDLEWARE setting defines a list of middleware classes ,
# that are used to process requests and responses in the Django application.
# Middleware is a way to process requests globally, 
# before they reach the view or after the view has processed them.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# The ROOT_URLCONF setting specifies the Python module,
# that contains the URL configuration for the project.
# It tells Django which module to use for resolving URLs to views.
ROOT_URLCONF = 'config.urls'
TESTING = "test" in sys.argv or "PYTEST_VERSION" in os.environ

# The TEMPLATES setting defines the configuration for the template engine used in the project.
# It specifies the backend engine, directories for template files,
# and context processors that provide additional data to templates.
# for contuct between the debug_toolbar and the templates, 
# we can use context processors to pass data from the backend to the frontend templates.
if not TESTING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]
    INTERNAL_IPS = [
        "127.0.0.1",
    ]


# The WSGI_APPLICATION setting specifies the Python path to the WSGI application callable,
# that Django's built-in servers (and some third-party servers) use to communicate with the application.
# It is used to deploy the Django application on a web server that supports the WSGI interface.
WSGI_APPLICATION = 'config.wsgi.application'

# The TEMPLATES setting defines the configuration for the template engine used in the project.
# It specifies the backend engine, directories for template files,
# and context processors that provide additional data to templates.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators
# why use password validators?
# Password validators are used to enforce certain rules and requirements for user passwords.
# and they help improve the security of user accounts, 
# by ensuring that passwords are strong and not easily guessable.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# what is i18n? 
# i18n stands for internationalization, 
# which is the process of designing and developing software applications
# that can be adapted to different languages and 
# regions without requiring changes to the source code.
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# why use static files?
# Static files are files that are served directly to the client,
# without any processing or modification by the
# server. They are typically used for assets like images, 
# CSS files, JavaScript files, and other resources
# that do not change frequently and 
# can be cached by the client's browser for improved performance.
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'


# why use media files?
# Media files are user-uploaded files that are stored on the server and,
# can be accessed by users through the application.
# They are typically used for content that is generated or uploaded by users,

AUTH_USER_MODEL = "accounts.CustomUser"

#  why use REST_FRAMEWORK settings?
# The REST_FRAMEWORK setting is used to configure the behavior of the Django REST Framework (DRF),
# which is a powerful and flexible toolkit for building Web APIs in Django.
# And it allows you to customize various aspects of the API,
# such as authentication, permissions, pagination, and more.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
     # تنظیمات قبلی شما (مثل Authentication و Pagination) اینجا می‌مانند...


    
    # اضافه کردن کلاس تولیدکننده مستندات
    # The 'DEFAULT_SCHEMA_CLASS' setting specifies the class,
    # that will be used to generate the API schema for your project.
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# why use SIMPLE_JWT settings?
# The SIMPLE_JWT setting is used to configure the behavior of the Simple JWT package,
# which is a third-party package for handling,
# JSON Web Tokens (JWT) authentication in Django REST Framework.
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}



# تنظیمات اختصاصی Swagger
# why use SPECTACULAR_SETTINGS?
# The SPECTACULAR_SETTINGS setting is used to configure the behavior of the drf-spectacular package,
# which is a third-party package for generating OpenAPI 3.0 documentation for Django REST Framework APIs.
SPECTACULAR_SETTINGS = {
    'TITLE': 'ACRON Project API with Swagger',
    'DESCRIPTION': 'مستندات جامع APIهای فروشگاه ACRON شامل بخش مشتریان و محصولات',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False, # برای تمیز ماندن خروجی نهایی
    
    # تنظیمات امنیتی برای تست 
    # API
    # ها داخل خود مرورگر
    'SECURITY': [
        {'jwtAuth': []}
    ],
    'SECURITY_DEFINITIONS': {
        'jwtAuth': {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
        }
    }
}





```

### File: `config\settings\development.py`
```python
# development.py is a settings file for the development environment in a Django project. 
# It contains configuration settings that are specific to the development environment, 
# such as enabling debug mode, configuring the database connection, 
# and other settings that are suitable for local development.
# this is the settings file for the development environment, 
# which is used when running the Django project locally on a developer's machine.

# why import * from base.py?
# The import statement from .base import * is used to import all the settings defined in the
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# we can use SQLite for development, which is a lightweight database that doesn't require a separate server.
# or we can use MySQL for development, which is a more robust database that requires a separate server.
# or we can use PostgreSQL for development, which is a powerful database that requires a separate server.
# PostgreSQL is a good choice for development,
# because it is a powerful database that requires a separate server.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'acron',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '1234',
        'PORT': '3306',
    }
}



```

### File: `config\settings\production.py`
```python
# Production settings

# Debug mode should be turned off in production for security reasons.
DEBUG = False

# ALLOWED_HOSTS is a list of strings representing the host/domain names that this Django site can serve.
# In production, you should set this to the actual domain names of your site.
ALLOWED_HOSTS = ['acronproject.com', 'www.acronproject.com', 'acronproject.com', 'www.acronproject.com', 'localhost', '127.0.0.1']




```

### File: `core\__init__.py`
```python

```

### File: `core\exceptions.py`
```python

```

### File: `core\mixins.py`
```python

```

### File: `core\pagination.py`
```python

```

### File: `core\permissions.py`
```python

```

### File: `core\services.py`
```python

```
