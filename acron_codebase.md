# ACRON Project Export

## Project Structure
```text
├── .github/
│   └── workflows/
│       └── django.yml
├── backend/
│   ├── apps/
│   │   ├── Documentation/
│   │   ├── accounts/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── advisor/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── services.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── ai/
│   │   │   ├── management/
│   │   │   │   └── commands/
│   │   │   │       └── run_mcp.py
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── test_client.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── permissions.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── carts/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── customers/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── services.py
│   │   │   ├── signals.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── notifications/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   ├── orders/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── services.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── payments/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── services.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── products/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── reviews/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   └── views.py
│   │   └── shipments/
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── services.py
│   │       ├── tests.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── brands/
│   │   └── 2026/
│   │       └── 07/
│   ├── categories/
│   │   └── 2026/
│   │       └── 07/
│   ├── config/
│   │   ├── settings/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   └── production.py
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── zxcZXCsettings.txt
│   ├── core/
│   │   ├── __init__.py
│   │   ├── exceptions.py
│   │   ├── mixins.py
│   │   ├── pagination.py
│   │   ├── permissions.py
│   │   └── services.py
│   ├── products/
│   │   ├── gallery/
│   │   │   └── 2026/
│   │   │       └── 07/
│   │   └── main/
│   │       └── 2026/
│   │           └── 07/
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── layout/
│   │   ├── context/
│   │   ├── features/
│   │   │   └── products/
│   │   │       ├── components/
│   │   │       └── services/
│   │   ├── pages/
│   │   ├── services/
│   ├── README.md
│   ├── package-lock.json
│   ├── package.json
├── CONTRIBUTING.md
├── Documentation.md
├── README.md
└── acron_codebase.md

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
* [Part-10](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-10-39ada1eb8b9d8032ac20ec61c189d41e)
* [Part-11](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-11-39cda1eb8b9d80aa8352d4456958750f)
* [Part-12](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-12-39fda1eb8b9d80e2a1dccc54e00ce765)
* [Part-13](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-13-3a0da1eb8b9d80ac9228ed8e884447f0)
* [Part-14](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-14-3a2da1eb8b9d80ad9df4fabcf68758fc)
* [Part-15](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-15-3a7da1eb8b9d8064bdaee01ac27bc2a8)
* [Part-16](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-16-3abda1eb8b9d80f38103c9ebe28af117)
* [Part-17](https://sinalalenakhsh.notion.site/ACRON-Methodology-Part-17-3adda1eb8b9d80ce8f49f9001684483e)








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
- [x] **MCP:** Model Context Control to Responsing interfaces with secure callback handling.
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


### How to run
* after cloning
* write in Terminal:  pipenv shell
* than: pipenv install Pipefile.lock


```

### File: `acron_codebase.md`
```md

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

    # ۱. مشخص کردن پوشه پیش‌فرض برای اجرای تمام دستورات این جاب (جابجایی به پوشه backend)
    defaults:
      run:
        working-directory: backend

    # ۲. راه‌اندازی دیتابیس موقت MySQL روی سرور گیت‌هاب
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
        # ۳. هماهنگی با requirements: جنگو ۶ حداقل به پایتون ۳.۱۲ نیاز دارد
        python-version: ["3.12", "3.13"]

    steps:
    - uses: actions/checkout@v5

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'
        # مشخص کردن مسیر دقیق فایل ریکوایرمنتس برای کش گیت‌هاب
        cache-dependency-path: backend/requirements.txt 

    # ۴. نصب ابزارهای لینوکسی مورد نیاز برای کامپایل کتابخانه mysqlclient
    - name: Install Linux Dependencies for MySQL
      run: |
        sudo apt-get update
        sudo apt-get install -y default-libmysqlclient-dev pkg-config build-essential

    - name: Install Python Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # ۵. اجرای تست‌ها با معرفی آدرس فایل تنظیمات
    - name: Run Tests
      env:
        DJANGO_SETTINGS_MODULE: config.settings.development
      run: |
        python manage.py test


        
```

### File: `backend\requirements.txt`
```txt
-i https://pypi.org/simple
annotated-types==0.7.0; python_version >= '3.8'
anyio==4.14.2; python_version >= '3.10'
asgiref==3.12.1; python_version >= '3.10'
attrs==26.1.0; python_version >= '3.9'
certifi==2026.6.17; python_version >= '3.7'
cffi==2.1.0; python_version >= '3.10'
click==8.4.2; python_version >= '3.10'
colorama==0.4.6; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6'
cryptography==49.0.0; python_version >= '3.9' and python_full_version not in '3.9.0, 3.9.1'
django==6.0.7; python_version >= '3.12'
django-cors-headers==4.9.0; python_version >= '3.9'
django-debug-toolbar==7.0.0; python_version >= '3.10'
djangorestframework==3.17.1; python_version >= '3.10'
djangorestframework-simplejwt==5.5.1; python_version >= '3.9'
drf-spectacular==0.29.0; python_version >= '3.7'
h11==0.16.0; python_version >= '3.8'
httpcore==1.0.9; python_version >= '3.8'
httpx==0.28.1; python_version >= '3.8'
httpx-sse==0.4.3; python_version >= '3.9'
idna==3.18; python_version >= '3.9'
inflection==0.5.1; python_version >= '3.5'
jsonschema==4.26.0; python_version >= '3.10'
jsonschema-specifications==2025.9.1; python_version >= '3.9'
mcp==1.28.1; python_version >= '3.10'
mysqlclient==2.2.8; python_version >= '3.10'
numpy==2.5.0; python_version >= '3.12'
opencv-python==5.0.0.93; python_version >= '3.6'
pillow==12.3.0; python_version >= '3.10'
pycparser==3.0; python_version >= '3.10'
pydantic==2.13.4; python_version >= '3.9'
pydantic-core==2.46.4; python_version >= '3.9'
pydantic-settings==2.14.2; python_version >= '3.10'
pyjwt[crypto]==2.13.0; python_version >= '3.9'
python-dotenv==1.2.2; python_version >= '3.10'
python-multipart==0.0.32; python_version >= '3.10'
pywin32==312; python_version >= '3.9'
pyyaml==6.0.3; python_version >= '3.8'
referencing==0.37.0; python_version >= '3.10'
rpds-py==2026.6.3; python_version >= '3.11'
sqlparse==0.5.5; python_version >= '3.8'
sse-starlette==3.4.5; python_version >= '3.10'
starlette==1.3.1; python_version >= '3.10'
typing-extensions==4.16.0; python_version >= '3.9'
typing-inspection==0.4.2; python_version >= '3.9'
tzdata==2026.3; python_version >= '2'
uritemplate==4.2.0; python_version >= '3.9'
uvicorn==0.51.0; python_version >= '3.10'

```

### File: `backend\apps\accounts\__init__.py`
```python

```

### File: `backend\apps\accounts\admin.py`
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "first_name",

                    "last_name",

                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = [
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'last_login',

    ]

```

### File: `backend\apps\accounts\apps.py`
```python
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'


```

### File: `backend\apps\accounts\models.py`
```python
from django.contrib.auth.models import AbstractUser

from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    


    
```

### File: `backend\apps\accounts\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\accounts\views.py`
```python
from django.shortcuts import render

# Create your views here.

```

### File: `backend\apps\advisor\__init__.py`
```python

```

### File: `backend\apps\advisor\admin.py`
```python
# apps/advisor/admin.py

from django.contrib import admin
from .models import Conversation, Message

class MessageInline(admin.TabularInline):
    """
    این کلاس به ما اجازه می‌دهد که پیام‌های هر گفتگو را به صورت مستقیم 
    و در داخل صفحه همان گفتگو در پنل ادمین مشاهده کنیم (Inline).
    """
    model = Message
    extra = 0 # تعداد ردیف‌های خالی اضافی برای ایجاد پیام جدید را صفر می‌گذاریم
    readonly_fields = ['role', 'content', 'detected_tone', 'created_at']
    can_delete = False # برای حفظ تاریخچه‌ها، امکان حذف دستی پیام‌ها از داخل ادمین گفتگو را می‌بندیم


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """
    تنظیمات مدیریت گفتگوها در پنل ادمین.
    """
    list_display = ['id', 'get_user_or_guest', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'visitor_session_key']
    inlines = [MessageInline] # نمایش پیام‌های مرتبط در پایین صفحه گفتگو

    def get_user_or_guest(self, obj):
        if obj.user:
            return obj.user.username
        return f"مهمان ({obj.visitor_session_key or 'نامشخص'})"
    get_user_or_guest.short_description = "کاربر / مهمان"


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    تنظیمات مدیریت تک پیام‌ها در پنل ادمین.
    """
    list_display = ['id', 'conversation_link', 'role', 'short_content', 'detected_tone', 'created_at']
    list_filter = ['role', 'detected_tone', 'created_at']
    search_fields = ['content', 'conversation__id']
    readonly_fields = ['created_at']

    def short_content(self, obj):
        return obj.content[:75] + "..." if len(obj.content) > 75 else obj.content
    short_content.short_description = "خلاصه متن"

    def conversation_link(self, obj):
        # ایجاد یک لینک مستقیم به گفتگوی مادر در پنل ادمین
        from django.urls import reverse
        from django.utils.html import format_html
        link = reverse("admin:advisor_conversation_change", args=[obj.conversation.id])
        return format_html('<a href="{}">مشاهده گفتگو ({})</a>', link, obj.conversation.id.hex[:8])
    conversation_link.short_description = "لینک گفتگو"


```

### File: `backend\apps\advisor\apps.py`
```python
from django.apps import AppConfig


class AdvisorConfig(AppConfig):
    name = 'apps.advisor'

```

### File: `backend\apps\advisor\models.py`
```python
# apps/advisor/models.py

from django.db import models
from django.conf import settings
import uuid

class Conversation(models.Model):
    """
    هر نمونه از این کلاس، نشان‌دهنده یک جلسه چت (Chat Session) است.
    کاربران (حتی بدون لاگین یا با لاگین) می‌توانند یک چت جدید شروع کنند.
    برای امنیت و غیرقابل حدس بودن جلسات چت، کلید اصلی را UUID قرار می‌دهیم.
    """
    # استفاده از UUID به جای کلید عددی (ID) برای جلوگیری از دسترسی غیرمجاز دیگران به تاریخچه چت‌ها
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # اگر کاربر لاگین کرده باشد، او را به این گفتگو متصل می‌کنیم. اگر مهمان باشد، Null می‌ماند.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='advisor_conversations',
        verbose_name="کاربر"
    )
    
    # ذخیره آی‌پی یا یک کلید شناسایی فرانت‌اند برای تحلیل بهتر رفتار کاربران غیرلاگین
    visitor_session_key = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name="کلید نشست بازدیدکننده"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ شروع گفتگو")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین فعالیت")

    class Meta:
        ordering = ['-updated_at']
        verbose_name = "گفتگوی مشاور"
        verbose_name_plural = "گفتگوهای مشاور"

    def __str__(self):
        user_str = self.user.username if self.user else f"مهمان ({self.id.hex[:8]})"
        return f"گفتگو با {user_str} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class Message(models.Model):
    """
    هر سطر از این جدول، یک پیام (یا سوال از طرف کاربر یا پاسخ از طرف هوش مصنوعی) را ذخیره می‌کند.
    """
    ROLE_CHOICES = [
        ('user', 'کاربر'),
        ('assistant', 'دستیار هوش مصنوعی'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # اتصال پیام به گفتگوی مربوطه؛ اگر گفتگو پاک شود، تمام پیام‌های آن نیز پاک خواهند شد (CASCADE)
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name="گفتگو"
    )
    
    # نقش ارسال‌کننده پیام (آیا کاربر سوال پرسیده یا هوش مصنوعی پاسخ داده؟)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        verbose_name="نقش ارسال‌کننده"
    )
    
    # متن اصلی پیام
    content = models.TextField(verbose_name="محتوای پیام")
    
    # تحلیل لحن پیام کاربر (مثلاً فنی، عامیانه، رسمی، بیزینسی) که توسط لایه سرویس تشخیص داده شده است
    detected_tone = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="لحن شناسایی‌شده"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال")

    class Meta:
        ordering = ['created_at'] # پیام‌ها باید به ترتیب زمان ارسال نمایش داده شوند تا رشته گفتگو درست بماند
        verbose_name = "پیام"
        verbose_name_plural = "پیام‌ها"

    def __str__(self):
        return f"{self.get_role_display()}: {self.content[:50]}..."



        
```

### File: `backend\apps\advisor\serializers.py`
```python
# apps/advisor/serializers.py

from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    """
    سریالایزر برای نمایش پیام‌های داخل یک گفتگو.
    """
    role_display = serializers.CharField(source='get_role_display', read_only=True)

    class Meta:
        model = Message
        fields = [
            'id',
            'role',
            'role_display',
            'content',
            'detected_tone',
            'created_at'
        ]
        read_only_fields = ['id', 'role_display', 'detected_tone', 'created_at']


class ConversationSerializer(serializers.ModelSerializer):
    """
    سریالایزر برای ساخت گفتگو و واکشی اطلاعات کلی آن.
    """
    # نمایش پیام‌های مرتبط با گفتگو به صورت Nested (تو در تو)
    messages = MessageSerializer(many=True, read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Conversation
        fields = [
            'id',
            'user',
            'user_username',
            'visitor_session_key',
            'messages',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'user', 'user_username', 'created_at', 'updated_at']


class AskAdvisorInputSerializer(serializers.Serializer):
    """
    سریالایزر اختصاصی برای دریافت ورودی سوال کاربر.
    این کلاس به صورت مستقیم به مدل وصل نیست و فقط وظیفه ولیدیشن ورودی خام API را دارد.
    """
    question = serializers.CharField(
        required=True, 
        min_length=3, 
        error_messages={
            'required': 'لطفاً سوال خود را بفرستید.',
            'min_length': 'سوال شما باید حداقل ۳ کاراکتر باشد.'
        }
    )






```

### File: `backend\apps\advisor\services.py`
```python
# apps/advisor/services.py

import json
from .models import Conversation, Message
# در صورت تمایل به استفاده از APIهای واقعی، اینجا پکیج‌های مربوطه (مثلاً هدرهای درخواستی به API جنگو یا Gemini) را ایمپورت می‌کنیم.

class AdvisorAIService:
    """
    سرویس مدیریت ارتباط با مدل زبانی (LLM) برای مشاور هوشمند پروژه و خالق اثر (سینا لاله بخش).
    """

    @staticmethod
    def get_system_context() -> str:
        """
        این متد کانتکست جامع و پرامپت سیستمی (System Prompt) را تولید می‌کند.
        این اطلاعات بر اساس رزومه رسمی سینا لاله بخش و کدهای پروژه ACRON طراحی شده است.
        """
        return """
        شما "مشاور هوشمند پروژه ACRON" و دستیار ارشد طراح و برنامه نویس این پروژه، "سینا لاله بخش" (Sina Lalehbakhsh) هستید.
        وظیفه شما پاسخگویی به سوالات کارفرمایان، بازدیدکنندگان، و مهندسانی است که می‌خواهند درباره پروژه ACRON یا استخدام و همکاری با سینا لاله بخش بدانند.

        اطلاعات درباره خالق اثر (سینا لاله بخش):
        - تخصص اصلی: مهندس ارشد بک‌اند جنگو (Django Backend Engineer) متمرکز بر معماری داده‌ها، کارایی (Performance) و مقیاس‌پذیری (Scalability).
        - مهارت‌های فنی برجسته: طراحی حرفه‌ای وب‌سرویس‌های RESTful با DRF، بهینه‌سازی کوئری‌های جنگو (تخصص عمیق در select_related, prefetch_related و Annotations برای کاهش کوئری‌های سنگین)، امنیت وب و جلوگیری از آسیب‌پذیری‌های وب، اجرای فرایندهای پس‌زمینه (Celery, Async Views)، و اصول دواپس/ابرپایه.
        - سوابق غیر فنی: دارای تحصیلات و تجربه در حوزه ارتباط تصویری و طراحی گرافیک (از هنرستان کمال‌الملک)، طراحی لوگو، مجسمه‌سازی سه بعدی و هویت بصری. این ویژگی باعث می‌شود کدهای او بسیار تمیز، منظم و مانند یک اثر هنری ساختاریافته باشند.
        - پکیج‌های متن‌باز: توسعه‌دهنده و منتشرکننده پکیج‌های پایتونی در PyPI مانند git-auto-django و push-py.
        - راه‌های ارتباطی: تلفن 09126507649، ایمیل sinalalehbakhsh@gmail.com، گیت‌هاب sinalalebakhsh.
        - شرایط کاری: علاقمند به کارهای چالش‌برانگیز، سیستم‌های با لود بالا، پروژه‌های تلفیقی وب و هوش مصنوعی.

        اطلاعات درباره پروژه ACRON (یک پروژه نمونه سطحِ جهانی):
        - یک سیستم تجارت الکترونیک (E-commerce) ماژولار و بسیار پیشرفته که به صورت Modular Monolith در جنگو طراحی شده است.
        - فازهای توسعه شامل:
          1. زیرساخت پایگاه داده (MySQL با ساختار بهینه و CustomUser).
          2. پیاده‌سازی DRF به همراه ساده‌سازی احراز هویت با JWT.
          3. دامنه مشتریان (Customer Domain) با Nested Serializers و سیگنال‌ها جهت ساخت خودکار پروفایل.
          4. دامنه محصولات و مستندسازی مدرن APIها با استفاده از drf-spectacular (OpenAPI 3.0).
          5. دامنه سبد خرید (Cart) بدون نیاز به لاگین اجباری و با استفاده از UUID جهت امنیت مطلق.
          6. دامنه سفارشات (Order) با ثبت دائمی و تغییرناپذیر (Immutable) قیمت واحد در OrderItem در لحظه خرید و اعمال تراکنش‌های دیتابیس برای کسر موجودی انبار.
          7. دامنه پرداخت با شبیه‌ساز امن درگاه بانکی (Mock Payment Gateway).
          8. دامنه ارسال مرسولات (Shipment & Fulfillment) که به محض تایید تراکنش، به صورت خودکار با سیگنال ایجاد می‌شود.
          9. پروتکل MCP (Model Context Protocol): که پروژه را تبدیل به یک سرور MCP برای هوش مصنوعی می‌کند تا هوش مصنوعی به عنوان ابزار (Tools) و منابع (Resources) مستقیماً به دیتابیس پروژه متصل شود و وضعیت سفارشات و بسته‌ها را استعلام کند.

        قوانین پاسخگویی (بسیار مهم):
        ۱. لحن (Tone) سوال کاربر را ارزیابی کنید. اگر کاربر با ادبیات رسمی و بیزینسی سوال پرسیده، پاسخ شما کاملاً رسمی، محترمانه و شرکتی باشد. اگر ادبیات کاربر صمیمی و خودمانی است، شما نیز با لحنی گرم، صمیمی، متقاعدکننده و در عین حال حرفه‌ای پاسخ دهید. اگر کاربر فنی صحبت می‌کند، جزییات عمیق معماری را به او توضیح دهید.
        ۲. هدف اصلی شما متقاعد کردن کارفرما برای همکاری با سینا لاله بخش یا استفاده از ساختار قدرتمند پروژه ACRON است.
        ۳. پاسخ‌های شما باید مستند، شیوا و عاری از ادعاهای توخالی باشد. همیشه از کدهای باکیفیت و معماری دقیق پروژه به عنوان سند توانمندی سینا استفاده کنید.
        """

    @classmethod
    def generate_response(cls, conversation_id: str, user_message_content: str) -> Message:
        """
        این متد جریان گفتگو را مدیریت می‌کند:
        ۱. پیام کاربر را در دیتابیس ذخیره می‌کند.
        ۲. تاریخچه پیام‌های قبلی گفتگو را لود می‌کند تا هوش مصنوعی حافظه داشته باشد.
        ۳. لحن را تشخیص می‌دهد و پرامپت را به مدل ارسال می‌کند.
        ۴. پاسخ دریافتی را ذخیره و بازمی‌گرداند.
        """
        # واکشی گفتگو از دیتابیس
        conversation = Conversation.objects.get(id=conversation_id)
        
        # تشخیص اولیه لحن (به عنوان مثال برای نسخه شبیه‌سازی؛ در دنیای واقعی این کار را به LLM می‌سپاریم)
        detected_tone = cls._analyze_user_tone(user_message_content)
        
        # ذخیره پیام کاربر در دیتابیس
        user_message = Message.objects.create(
            conversation=conversation,
            role='user',
            content=user_message_content,
            detected_tone=detected_tone
        )
        
        # واکشی تاریخچه گفتگو برای ارسال به هوش مصنوعی (حافظه چت)
        chat_history = Message.objects.filter(conversation=conversation).order_by('created_at')
        
        # ساختن کانتکست ارسالی به مدل
        # در دنیای واقعی:
        # response = client.generate_content(
        #     system_instruction=cls.get_system_context(),
        #     contents=[{"role": m.role, "parts": [m.content]} for m in chat_history]
        # )
        # ai_reply = response.text
        
        # شبیه‌ساز منطقی هوش مصنوعی بر اساس کانتکست پروژه و رزومه سینا لاله بخش:
        ai_reply = cls._mock_llm_response(user_message_content, detected_tone, chat_history)
        
        # ذخیره پاسخ دستیار هوش مصنوعی در دیتابیس
        assistant_message = Message.objects.create(
            conversation=conversation,
            role='assistant',
            content=ai_reply,
            detected_tone=detected_tone # لحن پاسخ با لحن کاربر تطابق دارد
        )
        
        # آپدیت فیلد updated_at در جدول گفتگو برای مانیتورینگ ادمین
        conversation.save() # این کار متد save() مدل گفتگو را صدا می‌زند و فیلد auto_now را آپدیت می‌کند
        
        return assistant_message

    @staticmethod
    def _analyze_user_tone(text: str) -> str:
        """
        یک تحلیل‌گر ساده و کلیدواژه‌ای برای تشخیص لحن کاربر.
        در نسخه نهایی، خود LLM این کار را با دقت بالاتری انجام می‌دهد.
        """
        text_lower = text.lower()
        if any(w in text_lower for w in ["سلام داداش", "چطوری", "سینا کیه", "کارت چیه", "باحال", "دمت", "حاجی", "ببین", "میشه"]):
            return "Friendly / Informal (صمیمی و عامیانه)"
        elif any(w in text_lower for w in ["جناب", "همکاری", "قرارداد", "شرکت", "محترم", "رزومه", "استخدام", "آیا", "آقای", "آقا"]):
            return "Business / Formal (رسمی و شرکتی)"
        elif any(w in text_lower for w in ["معماری", "کدبیس", "uuid", "select_related", "درگاه", "mcp", "دیتابیس", "prefetch_related", "database", "user", "django"]):
            return "Technical / Deep (فنی و مهندسی)"
        return "General (عمومی)"

    @staticmethod
    def _mock_llm_response(question: str, tone: str, history) -> str:
        """
        این متد پاسخ‌های دقیق و متناسب با دیتای واقعی رزومه سینا و پروژه ACRON تولید می‌کند.
        هدف نمایش چگونگی رفتار هوشمندانه عامل بر اساس لحن است.
        """
        q = question.lower()
        
        # سناریو ۱: سوال درباره شخصیت یا تخصص‌های سینا لاله بخش
        if "سینا" in q or "طراح" in q or "تخصص" in q or "برنامه نویس" in q:
            if "Friendly" in tone:
                return (
                    "سلام رفیق! سینا لاله بخش رو بخوام برات خلاصه کنم، یه مهندس بک‌اندِ عشقِ جنگوئه که کارش فقط کد زدن نیست؛ "
                    "اون هنر خوندن (ارتباط تصویری و مجسمه‌سازی) رو با مهندسی داده ترکیب کرده. واسه همین کدهایی که می‌نویسه "
                    "مثل یه تابلوی نقاشی، تمیز، بهینه و ساختاریافته‌ست! توی جنگو و بهینه‌سازی دیتابیس (ORM) استاده و پکیج‌های "
                    "باکلاس توی PyPI داره. دوست داری پروژه‌شو ببینی یا مستقیم با خودش لینک بشی؟"
                )
            elif "Business" in tone:
                return (
                    "با سلام و احترام خدمت شما همکار گرامی. آقای سینا لاله بخش، مهندس ارشد بک‌اند جنگو هستند که تخصص "
                    "ویژه‌ای در طراحی سیستم‌های با کارایی بالا (High-Performance APIs) و بهینه‌سازی لایه دیتابیس دارند. "
                    "ایشان با داشتن پیشینه تحصیلی در حوزه طراحی گرافیک و ارتباط تصویری، فرآیندهای تحلیل نیازمندی‌ها را "
                    "بسیار دقیق و با معماری بصری بی‌نظیری پیاده‌سازی می‌کنند. برای بررسی شرایط همکاری یا برگزاری جلسه فنی، "
                    "می‌توانید با شماره 09126507649 تماس حاصل فرمایید."
                )
            else: # فنی
                return (
                    "درود بر شما توسعه‌دهنده گرامی. پشته فنی آقای لاله بخش متمرکز بر جنگو (Django/DRF) با تأکید بر ORM Optimization است. "
                    "ایشان مهارت بالایی در حل چالش‌های N+1 Query با استفاده از متدهای پیشرفته جنگو دارند. همچنین توسعه پکیج‌های متن‌باز "
                    "مانند `git-auto-django` و `push-py` و معماری ماژولار پروژه ACRON گواهی بر تسلط عمیق ایشان بر توسعه پایدار نرم‌افزار است."
                )

        # سناریو ۲: سوال درباره پروژه ACRON
        elif "پروژه" in q or "acron" in q or "آکرون" in q:
            return (
                "پروژه ACRON یک شاهکار معماری Modular Monolith در جنگو است که تا فاز ۱۰ پیش رفته است. "
                "این پروژه شامل مدیریت سبد خرید ناهمگام با UUID، ثبت سفارشات با قیمت فریز شده (Immutable)، "
                "درگاه پرداخت شبیه‌ساز ایزوله، و صدور خودکار مرسوله از طریق سیگنال‌هاست. "
                "بخش متمایزکننده آن، پیاده‌سازی پروتکل MCP (Model Context Protocol) است که به هوش مصنوعی اجازه می‌دهد "
                "مستقیماً به عنوان یک عامل اجرایی به دیتابیس پروژه متصل شود و وضعیت‌ها را مدیریت کند."
            )

        # پاسخ عمومی با متقاعدسازی بر اساس لحن
        else:
            if "Business" in tone:
                return (
                    "پرسش بسیار هوشمندانه‌ای مطرح فرمودید. آقای سینا لاله بخش آمادگی دارند تا راهکارهای هوش مصنوعی و "
                    "پلتفرم‌های پیچیده شما (مانند سیستم‌های دوستیابی هوشمند یا پلتفرم‌های واسط کارفرما و کارگر) را "
                    "با همین متدولوژی استاندارد ACRON و با تکیه بر لایه‌های مستحکم امنیتی و داده‌ای توسعه دهند. "
                    "آیا تمایل دارید پروپوزال فنی این مدل‌ها را برای شما ارسال کنیم؟"
                )
            else:
                return (
                    "پرسش جالبی بود! این دقیقاً همان نوع چالش‌هایی است که من (مشاور هوشمند ACRON) و سینا لاله بخش عاشق حل کردنش هستیم. "
                    "تلفیق هوش مصنوعی و وب‌سرویس‌های بهینه، هنر ماست. بگو پروژه‌ات در چه مرحله‌ای هست تا دقیق راهنمایی‌ات کنم رفیق!"
                )
            


```

### File: `backend\apps\advisor\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\advisor\urls.py`
```python
# apps/advisor/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvisorViewSet

# استفاده از DefaultRouter برای ساخت خودکار مسیرهای استاندارد RESTful
router = DefaultRouter()
router.register(r'advisor', AdvisorViewSet, basename='advisor')

urlpatterns = [
    path('', include(router.urls)),
]




```

### File: `backend\apps\advisor\views.py`
```python
# apps/advisor/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .models import Conversation
from .serializers import ConversationSerializer, AskAdvisorInputSerializer, MessageSerializer
from .services import AdvisorAIService

class AdvisorViewSet(viewsets.ModelViewSet):
    """
    مجموعه وب‌سرویس‌های مدیریت گفتگو و ارتباط با مشاور هوشمند پروژه ACRON و سینا لاله بخش.
    این مسیر نیاز به لاگین اجباری ندارد تا همه کارفرمایان بتوانند به راحتی با مشاور چت کنند.
    """
    permission_classes = [AllowAny]
    queryset = Conversation.objects.prefetch_related('messages').all()
    serializer_class = ConversationSerializer
    
    # برای امنیت، متدهای ویرایش و حذف کلی گفتگوها را در سطح عمومی API غیرفعال می‌کنیم
    http_method_names = ['get', 'post', 'delete']

    def perform_create(self, serializer):
        """
        هنگام ایجاد یک گفتگوی جدید، اگر کاربر لاگین کرده باشد، او را ثبت می‌کنیم.
        همچنین آی‌پی یا سشن بازدیدکننده را نیز برای بررسی‌های بعدی ذخیره می‌کنیم.
        """
        user = self.request.user if self.request.user.is_authenticated else None
        
        # گرفتن آی‌پی ساده کاربر به عنوان کلید سشن مهمان
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
            
        serializer.save(user=user, visitor_session_key=ip)

    @extend_schema(
        summary="ارسال سوال به مشاور هوشمند پروژه",
        description="با ارسال شناسه گفتگو و سوال خود، پاسخ هوشمند و متقاعدکننده منطبق با لحن خود را دریافت کنید.",
        request=AskAdvisorInputSerializer,
        responses={
            200: OpenApiResponse(response=MessageSerializer, description="پاسخ هوش مصنوعی تولید و ذخیره شد."),
            400: OpenApiResponse(description="ورودی نامعتبر است.")
        }
    )
    @action(detail=True, methods=['post'], url_path='ask')
    def ask(self, request, pk=None):
        """
        مسیر اختصاصی: POST /api/advisor/{conversation_uuid}/ask/
        این متد سوال کاربر را دریافت کرده، به لایه سرویس منتقل می‌کند و پاسخ هوشمند را برمی‌گرداند.
        """
        # ۱. لود کردن گفتگوی مربوطه از دیتابیس
        conversation = self.get_object()
        
        # ۲. بررسی و اعتبارسنجی ورودی سوال با سریالایزر اختصاصی
        input_serializer = AskAdvisorInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        user_question = input_serializer.validated_data['question']
        
        # ۳. فراخوانی لایه سرویس برای ارتباط با مدل زبانی و ذخیره‌سازی پیام‌ها
        ai_response_message = AdvisorAIService.generate_response(
            conversation_id=conversation.id,
            user_message_content=user_question
        )
        
        # ۴. سریالایز کردن پاسخ نهایی هوش مصنوعی برای ارسال به کلاینت
        output_serializer = MessageSerializer(ai_response_message)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
    





```

### File: `backend\apps\ai\__init__.py`
```python

```

### File: `backend\apps\ai\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `backend\apps\ai\apps.py`
```python
from django.apps import AppConfig


class AiConfig(AppConfig):
    name = 'apps.ai'

```

### File: `backend\apps\ai\models.py`
```python
from django.db import models

# Create your models here.

```

### File: `backend\apps\ai\test_client.py`
```python
import sys
import os
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_test_client():
    # ----------------- 🧪 آزمایشگاه امنیت -----------------
    # سناریو ۱: شناسه کاربری که در دیتابیس مالک سفارش "6d8c603e-fcde-44e2-9fe6-f93c87971948" است را وارد کنید (مثلاً "1")
    # سناریو ۲: شناسه یک کاربر دیگر یا یک کاربر فرضی (مثلاً "99") را بگذارید تا هک را شبیه‌سازی کنید!
    logged_in_user_id = "5" 
    # -----------------------------------------------------

    env_vars = os.environ.copy()
    env_vars["ACRON_USER_ID"] = logged_in_user_id

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-u", "manage.py", "run_mcp"], 
        env=env_vars
    )
    
    print("⏳ در حال اتصال به سرور هوش مصنوعی ACRON...")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("✅ اتصال با موفقیت برقرار شد!\n")
                
                # برای تست، از همان شناسه سفارش قبلی استفاده می‌کنیم
                target_order_id = "6d8c603e-fcde-44e2-9fe6-f93c87971948" 
                print(f"🤖 [شبیه‌سازی LLM]: در حال فراخوانی ابزار برای سفارش {target_order_id} با شناسه کاربر لود شده: {logged_in_user_id}...")
                
                result = await session.call_tool(
                    "get_order_status", 
                    arguments={"order_uuid": target_order_id}
                )
                
                print("\n📥 پاسخ دریافتی:")
                print(result.content[0].text)
                
    except Exception as e:
        print(f"❌ خطایی در کلاینت رخ داد: {e}")

if __name__ == "__main__":
    asyncio.run(run_test_client())





```

### File: `backend\apps\ai\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\ai\views.py`
```python
from django.shortcuts import render

# Create your views here.

```

### File: `backend\apps\ai\management\commands\run_mcp.py`
```python
import os
from django.core.management.base import BaseCommand
from mcp.server.fastmcp import FastMCP
from apps.orders.models import Order
from apps.shipments.models import Shipment
from asgiref.sync import sync_to_async

mcp = FastMCP("ACRON Core AI Engine")

@mcp.tool()
async def get_order_status(order_uuid: str) -> str:
    """
    Get the current billing/payment status of an order using its UUID.
    """
    # خواندن متغیر محیطیِ امن که توسط جنگو ست شده است
    user_id = os.environ.get("ACRON_USER_ID")
    if not user_id:
        return "خطای امنیتی: کاربر احراز هویت نشده است."

    @sync_to_async
    def fetch_order():
        try:
            # 🛡️ دیوار امنیتی: بررسی دسترسی کاربر به سفارش
            # اگر مدل سفارش شما مستقیماً به User متصل است، از فیلتر زیر استفاده کنید:
            # order = Order.objects.get(id=order_uuid, user_id=user_id)
            
            # اگر مدل سفارش شما از طریق Customer به User متصل است:
            order = Order.objects.get(id=order_uuid, customer__user_id=user_id)
            
            return f"سفارش شماره {order_uuid} در وضعیت [{order.get_status_display()}] قرار دارد."
        except Order.DoesNotExist:
            return "خطا: سفارشی با این شناسه برای شما یافت نشد یا شما دسترسی ندارید."
        except Exception as e:
            return f"خطای غیرمنتظره در سیستم: {str(e)}"
            
    return await fetch_order()


@mcp.tool()
async def track_shipment_status(order_uuid: str) -> str:
    """
    Track the physical shipping status, carrier info, and tracking code for an order.
    """
    user_id = os.environ.get("ACRON_USER_ID")
    if not user_id:
        return "خطای امنیتی: کاربر احراز هویت نشده است."

    @sync_to_async
    def fetch_shipment():
        try:
            # 🛡️ دیوار امنیتی: بررسی دسترسی کاربر به مرسوله از طریق سفارش
            # اگر سفارش مستقیم به User وصل است:
            # shipment = Shipment.objects.get(order__id=order_uuid, order__user_id=user_id)
            
            # اگر سفارش به Customer و مشتری به User وصل است:
            shipment = Shipment.objects.get(order__id=order_uuid, order__customer__user_id=user_id)
            
            tracking_code = shipment.tracking_number or "هنوز صادر نشده است"
            tracking_link = shipment.get_tracking_url() or "لینک پیگیری موجود نیست"
            
            return (
                f"وضعیت ارسال: {shipment.get_status_display()}\n"
                f"شرکت حمل و نقل: {shipment.get_carrier_display()}\n"
                f"کد رهگیری پستی: {tracking_code}\n"
                f"لینک مستقیم پیگیری: {tracking_link}"
            )
        except Shipment.DoesNotExist:
            return "اطلاعات مرسوله یافت نشد. ممکن است این سفارش متعلق به شما نباشد یا هنوز صادر نشده باشد."
        except Exception as e:
            return f"خطای غیرمنتظره در سیستم: {str(e)}"
            
    return await fetch_shipment()


class Command(BaseCommand):
    help = "Starts the ACRON Model Context Protocol (MCP) Server"
    requires_system_checks = []

    def handle(self, *args, **options):
        self.stderr.write(self.style.SUCCESS("🤖 سرور هوش مصنوعی ACRON (MCP) روشن شد..."))
        mcp.run(transport="stdio")



```

### File: `backend\apps\api\__init__.py`
```python

```

### File: `backend\apps\api\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `backend\apps\api\apps.py`
```python
from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api'
```

### File: `backend\apps\api\models.py`
```python
from django.db import models

# Create your models here.

```

### File: `backend\apps\api\permissions.py`
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

### File: `backend\apps\api\serializers.py`
```python
# apps/api/serializers.py

from rest_framework import serializers


from apps.accounts import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser

        fields = ['id', 'username', 'email', 'first_name', 'last_name',]


```

### File: `backend\apps\api\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\api\urls.py`
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
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API
    path('', include('apps.carts.urls')), 
    # orders
    path('', include('apps.orders.urls')), 
    # اضافه کردن مسیرهای مشاور هوشمند جدید
    path('', include('apps.advisor.urls')),
    # 🔑 JWT Authentication
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

### File: `backend\apps\api\views.py`
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

### File: `backend\apps\carts\__init__.py`
```python

```

### File: `backend\apps\carts\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `backend\apps\carts\apps.py`
```python
from django.apps import AppConfig


class CartsConfig(AppConfig):
    name = 'apps.carts'

```

### File: `backend\apps\carts\models.py`
```python
import uuid
from django.db import models

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # 🔴 اتصال سبد خرید به مشتری (برای کاربران لاگین شده)
    customer = models.OneToOneField(
        'customers.Customer',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='cart'
    )

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    


```

### File: `backend\apps\carts\serializers.py`
```python
from rest_framework import serializers
from .models import Cart, CartItem
from apps.products.models import Product


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'main_image']


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    # 🔴 تغییر نام به total_price جهت هماهنگی کامل با Cart.jsx
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

    def get_total_price(self, cart: Cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    cart_id = serializers.UUIDField()

    class Meta:
        model = CartItem
        fields = ['id', 'cart_id', 'product_id', 'quantity']

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("محصولی با این شناسه یافت نشد.")
        return value

    def validate_cart_id(self, value):
        if not Cart.objects.filter(id=value).exists():
            raise serializers.ValidationError("سبد خریدی با این شناسه یافت نشد.")
        return value

    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, 
                product_id=product_id, 
                quantity=quantity
            )

        return self.instance


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']




        
```

### File: `backend\apps\carts\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\carts\urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()

# 🔴 ثبت cart-items قبل از '' ضروری است تا تداخل URL ایجاد نشود
router.register('cart-items', CartItemViewSet, basename='cart-items')
router.register('', CartViewSet, basename='carts')

urlpatterns = [
    path('', include(router.urls)),
]
```

### File: `backend\apps\carts\views.py`
```python
from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.customers.models import Customer
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.create()
        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            customer, _ = Customer.objects.get_or_create(user=request.user)
            cart, _ = Cart.objects.get_or_create(customer=customer)
        else:
            cart = Cart.objects.create()

        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='mine', permission_classes=[IsAuthenticated])
    def mine(self, request):
        customer, _ = Customer.objects.get_or_create(user=request.user)
        cart, _ = Cart.objects.get_or_create(customer=customer)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class CartItemViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post', 'patch', 'delete']
    queryset = CartItem.objects.select_related('product').all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
```

### File: `backend\apps\customers\__init__.py`
```python

```

### File: `backend\apps\customers\admin.py`
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

### File: `backend\apps\customers\apps.py`
```python
from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.customers'

    def ready(self):
        from . import signals






```

### File: `backend\apps\customers\models.py`
```python
# acron/backend/apps/customers/models.py

from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Address(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='addresses')
    title = models.CharField(max_length=50,help_text="مثال: خانه، محل کار",null=True,blank=True)
    receiver_name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.TextField()
    postal_code = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
```

### File: `backend\apps\customers\serializers.py`
```python
from rest_framework import serializers
from .models import Customer, Address


class AddressSerializer(serializers.ModelSerializer):
    """
    سریالایزر برای تبدیل مدل آدرس به JSON و برعکس
    """
    class Meta:
        model = Address
        fields = [
            'id', 
            'title', 
            'receiver_name', 
            'phone_number', 
            'province', 
            'city', 
            'street', 
            'postal_code', 
            'is_default'
        ]
        read_only_fields = ['id']


class CustomerSerializer(serializers.ModelSerializer):
    """
    سریالایزر ساده برای اطلاعات کلی مشتری
    """
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'phone_number']


class CustomerProfileSerializer(serializers.ModelSerializer):
    """
    سریالایزر کامل برای صفحه پروفایل (شامل اطلاعات کاربری و لیست آدرس‌ها)
    """
    # خواندن فیلدهای مرتبط از مدل User از طریق رابطه OneToOne
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    customer_phone = serializers.CharField(source='phone_number', read_only=True)
    
    # دریافت آدرس‌های مرتبط با این مشتری (سریالایزر چندتایی)
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'customer_phone', 
            'addresses'
        ]


        
```

### File: `backend\apps\customers\services.py`
```python
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



```

### File: `backend\apps\customers\signals.py`
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

### File: `backend\apps\customers\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\customers\urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, CustomerProfileView

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = [
    path('profile/', CustomerProfileView.as_view(), name='user-profile'),
    path('', include(router.urls)),
]

```

### File: `backend\apps\customers\views.py`
```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import action

from .models import Customer, Address
from .serializers import CustomerProfileSerializer, AddressSerializer, CustomerSerializer
from .services import AddressService


class CustomerMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customer, _ = Customer.objects.get_or_create(user=request.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def patch(self, request):
        customer, _ = Customer.objects.get_or_create(user=request.user)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
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
        # این متد باعث می‌شود نیازی به ارسال ID در URL نباشد.
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
        customer, _ = Customer.objects.get_or_create(user=self.request.user)
        
        # اگر این اولین آدرس کاربر باشد، به صورت خودکار پیش‌فرض می‌شود
        is_first = not Address.objects.filter(customer=customer).exists()
        
        # اگر کاربر آدرس جدید را پیش‌فرض انتخاب کرده یا اولین آدرسش است
        if serializer.validated_data.get('is_default', False) or is_first:
            Address.objects.filter(customer=customer, is_default=True).update(is_default=False)
            serializer.save(customer=customer, is_default=True)
        else:
            serializer.save(customer=customer)

    @action(detail=True, methods=['post'], url_path='set-default')
    def set_default(self, request, pk=None):
        """
        اکشن اختصاصی برای انتخاب آدرس پیش‌فرض:
        POST /api/customers/addresses/{id}/set-default/
        """
        try:
            address = AddressService.set_default_address(request.user, pk)
            return Response(
                {
                    "detail": "آدرس پیش‌فرض با موفقیت تغییر کرد.",
                    "address": AddressSerializer(address).data
                },
                status=status.HTTP_200_OK
            )
        except (Address.DoesNotExist, Customer.DoesNotExist):
            return Response(
                {"detail": "آدرس یا مشتری یافت نشد."},
                status=status.HTTP_404_NOT_FOUND
            )
    
    
    
```

### File: `backend\apps\notifications\__init__.py`
```python

```

### File: `backend\apps\notifications\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `backend\apps\notifications\apps.py`
```python
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    name = 'apps.notifications'

```

### File: `backend\apps\notifications\models.py`
```python
from django.db import models

# Create your models here.

```

### File: `backend\apps\notifications\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\notifications\views.py`
```python
from django.shortcuts import render

# Create your views here.

```

### File: `backend\apps\orders\__init__.py`
```python

```

### File: `backend\apps\orders\admin.py`
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

### File: `backend\apps\orders\apps.py`
```python
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'apps.orders'

```

### File: `backend\apps\orders\models.py`
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

### File: `backend\apps\orders\serializers.py`
```python
# apps/orders/serializers.py

from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'unit_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'created_at', 'items', 'total_price']

    def get_total_price(self, obj):
        # محاسبه مجموع قیمت فاکتور بر اساس اقلام
        return sum(item.quantity * item.unit_price for item in obj.items.all())


class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    shipping_address = serializers.CharField(min_length=10)


    
```

### File: `backend\apps\orders\services.py`
```python
# apps/orders/services.py

from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.carts.models import Cart
from apps.orders.models import Order, OrderItem
from apps.customers.models import Customer

class OrderService:
    """
    سرویس ارشد مدیریت و پردازش فرآیند ثبت سفارش در پروژه ACRON.
    """

    @classmethod
    def place_order(cls, user, cart_id: str, shipping_address: str) -> Order:
        """
        متد ثبت سفارش با رعایت کامل ساختار مدل‌های Order و OrderItem.
        """
        
        with transaction.atomic():
            
            # ۱. یافتن پروفایل مشتری (Customer) متصل به کاربر جاری
            try:
                customer = Customer.objects.get(user=user)
            except Customer.DoesNotExist:
                raise ValidationError("پروفایل مشتری برای این کاربر یافت نشد.")

            # ۲. واکشی سبد خرید به همراه اقلام آن
            try:
                cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
            except Cart.DoesNotExist:
                raise ValidationError("سبد خرید معتبری یافت نشد.")

            # ۳. بررسی خالی نبودن سبد خرید
            cart_items = cart.items.all()
            if not cart_items:
                raise ValidationError("سبد خرید شما خالی است و امکان ثبت سفارش وجود ندارد.")

            # ۴. ایجاد رکورد اصلی سفارش در دیتابیس (مطابق با مدل Order)
            order = Order.objects.create(
                customer=customer,
                status=Order.OrderStatus.PENDING  # مقدار 'P'
            )

            # ۵. انتقال اقلام به سفارش و فریز کردن قیمت در فیلد unit_price
            for item in cart_items:
                product = item.product
                
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item.quantity,
                    unit_price=product.price  # ذخیره قیمت فریز شده کالا
                )

            # ۶. پاکسازی سبد خرید پس از ثبت موفق سفارش
            cart.delete()

            return order
```

### File: `backend\apps\orders\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\orders\urls.py`
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register('', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]


```

### File: `backend\apps\orders\views.py`
```python
# apps/orders/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer, OrderCreateInputSerializer
from .services import OrderService

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            customer__user=self.request.user
        ).prefetch_related('items__product').order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateInputSerializer
        return OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_id = serializer.validated_data['cart_id']
        shipping_address = serializer.validated_data['shipping_address']

        order = OrderService.place_order(
            user=request.user,
            cart_id=cart_id,
            shipping_address=shipping_address
        )

        output_serializer = OrderSerializer(order)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    # ----------------------------------------------------
    # اندپوینت سفارشی: POST /api/orders/{id}/pay/
    # ----------------------------------------------------
    @action(detail=True, methods=['post'], url_path='pay')
    def pay(self, request, pk=None):
        """
        شبیه‌سازی تایید پرداخت درگاه آنلاین برای یک سفارش مشخص
        """
        order = self.get_object()

        # گارد: اگر سفارش قبلاً پرداخت شده یا لغو شده باشد
        if order.status != 'P':
            return Response(
                {"detail": "این سفارش در وضعیت «در انتظار پرداخت» نیست."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # تغییر وضعیت سفارش به پرداخت موفق
        order.status = 'C'
        order.save()

        return Response(
            {
                "detail": "پرداخت با موفقیت انجام شد.",
                "order": OrderSerializer(order).data
            },
            status=status.HTTP_200_OK
        )


    
```

### File: `backend\apps\payments\__init__.py`
```python

```

### File: `backend\apps\payments\admin.py`
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

### File: `backend\apps\payments\apps.py`
```python
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    name = 'apps.payments'

```

### File: `backend\apps\payments\models.py`
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

### File: `backend\apps\payments\serializers.py`
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

### File: `backend\apps\payments\services.py`
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

### File: `backend\apps\payments\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\payments\urls.py`
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

### File: `backend\apps\payments\views.py`
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

### File: `backend\apps\products\__init__.py`
```python

```

### File: `backend\apps\products\admin.py`
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

### File: `backend\apps\products\apps.py`
```python
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'apps.products'

```

### File: `backend\apps\products\models.py`
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

### File: `backend\apps\products\serializers.py`
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

### File: `backend\apps\products\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\products\urls.py`
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

### File: `backend\apps\products\views.py`
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

### File: `backend\apps\reviews\__init__.py`
```python

```

### File: `backend\apps\reviews\admin.py`
```python
from django.contrib import admin

# Register your models here.

```

### File: `backend\apps\reviews\apps.py`
```python
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    name = 'reviews'

```

### File: `backend\apps\reviews\models.py`
```python
from django.db import models

# Create your models here.

```

### File: `backend\apps\reviews\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\reviews\views.py`
```python
from django.shortcuts import render

# Create your views here.

```

### File: `backend\apps\shipments\__init__.py`
```python

```

### File: `backend\apps\shipments\admin.py`
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

### File: `backend\apps\shipments\apps.py`
```python
from django.apps import AppConfig


class ShipmentsConfig(AppConfig):
    name = 'apps.shipments'

```

### File: `backend\apps\shipments\models.py`
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

### File: `backend\apps\shipments\serializers.py`
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

### File: `backend\apps\shipments\services.py`
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

### File: `backend\apps\shipments\tests.py`
```python
from django.test import TestCase

# Create your tests here.

```

### File: `backend\apps\shipments\urls.py`
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

### File: `backend\apps\shipments\views.py`
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

### File: `backend\config\__init__.py`
```python

```

### File: `backend\config\asgi.py`
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

### File: `backend\config\urls.py`
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
# 🔴 ۱. مسیرهای اختصاصی اپلیکیشن‌ها (باید بالاتر قرار گیرند)
    path('api/carts/', include('apps.carts.urls')),
    path('api/customers/', include('apps.customers.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/orders/', include('apps.orders.urls')),
    
    # 🔴 ۲. مسیر عمومی api (باید پایین‌تر باشد تا تداخل ایجاد نکند)
    path('api/', include('apps.api.urls')),


    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    

    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]



if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()



```

### File: `backend\config\wsgi.py`
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

### File: `backend\config\zxcZXCsettings.txt`
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

### File: `backend\config\settings\__init__.py`
```python
from .development import *


```

### File: `backend\config\settings\base.py`
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
    "corsheaders",


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
    'apps.ai',
    'apps.advisor', # اضافه کردن اپلیکیشن جدید مشاور هوشمند
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

    # Third Party:
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
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


# What is CORS ?
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]



```

### File: `backend\config\settings\development.py`
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

### File: `backend\config\settings\production.py`
```python
# Production settings

# Debug mode should be turned off in production for security reasons.
DEBUG = False

# ALLOWED_HOSTS is a list of strings representing the host/domain names that this Django site can serve.
# In production, you should set this to the actual domain names of your site.
ALLOWED_HOSTS = ['acronproject.com', 'www.acronproject.com', 'acronproject.com', 'www.acronproject.com', 'localhost', '127.0.0.1']




```

### File: `backend\core\__init__.py`
```python

```

### File: `backend\core\exceptions.py`
```python

```

### File: `backend\core\mixins.py`
```python

```

### File: `backend\core\pagination.py`
```python

```

### File: `backend\core\permissions.py`
```python

```

### File: `backend\core\services.py`
```python

```

### File: `frontend\README.md`
```md
# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

```

### File: `frontend\package-lock.json`
```json
{
  "name": "frontend",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "frontend",
      "version": "0.0.0",
      "dependencies": {
        "axios": "^1.19.0",
        "react": "^19.2.7",
        "react-dom": "^19.2.7",
        "react-router-dom": "^7.18.1"
      },
      "devDependencies": {
        "@eslint/js": "^10.0.1",
        "@types/react": "^19.2.17",
        "@types/react-dom": "^19.2.3",
        "@vitejs/plugin-react": "^6.0.3",
        "eslint": "^10.6.0",
        "eslint-plugin-react-hooks": "^7.1.1",
        "eslint-plugin-react-refresh": "^0.5.3",
        "globals": "^17.7.0",
        "vite": "^8.1.1"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.7.tgz",
      "integrity": "sha512-Aup7aUOfpbAUg2ROOJN6Iw5f9DMBlzu0mIkm/malLQFN/YQgO48wCj0Kxa3sEHJvPVFg7siR+qRInwXd2qhQKw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.29.7",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.7.tgz",
      "integrity": "sha512-locTkQyKvwIEgBzVrn8693ebc97F2U8ZHjbXwDXJ5Fn2TCpNwTlKcaKLkdHop5c/icOFE7qt7Q9JC5hnKNa6Gg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/core/-/core-7.29.7.tgz",
      "integrity": "sha512-RgHBCvtjbOK2gXSNBNIkNoEc9qoVEtau3hj8gEqKQuL3HZAibKarWFEI3Lfm6EYKkLalOh8eSrj9b+ch9H/VBA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/generator": "^7.29.7",
        "@babel/helper-compilation-targets": "^7.29.7",
        "@babel/helper-module-transforms": "^7.29.7",
        "@babel/helpers": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/template": "^7.29.7",
        "@babel/traverse": "^7.29.7",
        "@babel/types": "^7.29.7",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/generator/-/generator-7.29.7.tgz",
      "integrity": "sha512-DkXD5OJQaAQIdZ1bt3UZdEnHAn9Imd3IVBdX03UFe+ony9Ojw5pzr9YVKGDY1jt+Gcn/FnGkNf8r+Vj5NOJWtQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.7",
        "@babel/types": "^7.29.7",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.29.7.tgz",
      "integrity": "sha512-wem6WaBj4NaVYVdNhLPPVacES6ZJ+KBBfSkTMD3YZxbP3rm3Di85tJU5ljaUNhaOynt+Aj0xruhYuzQBt8n71g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.29.7",
        "@babel/helper-validator-option": "^7.29.7",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.29.7.tgz",
      "integrity": "sha512-3nQVUAtvkKH9zahfWgw96Jc/uFOmjACE1kQz82E2lqWmHBgjzbNlsC22nuQTfahmWeQtTq5nQ/4Nnd2A1wj4zA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.29.7.tgz",
      "integrity": "sha512-ejHwrQQYcm9xnTivShn2IDOlIzInN34AXskvq9QicvCtEzq1Vzclu/tKF8Jq1Cg8JG2GL6/EmjgsCT7lXepE3g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.29.7.tgz",
      "integrity": "sha512-UPUVSyXbOh627KiCIGQSgwWzGeBKLkaJ9PJEdrngIwMSzxLR4jS4+f1f1jb7VzBbg8nFLaYotvVPFCTqdrmTAg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.29.7",
        "@babel/helper-validator-identifier": "^7.29.7",
        "@babel/traverse": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.29.7.tgz",
      "integrity": "sha512-Pb5ijPrZ89GDH8223L4UP8i6QApWxs04RbPQJTeWDV0/keR2E36MeKnyr6LYmUUvqRRI+Iv87SuF1W6ErINzYw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.29.7.tgz",
      "integrity": "sha512-qehxGkRj55h/ff8EMaJ+cYhyaKlHIxqYDn682wQD7RNp9UujOQsHog2uS0r2vzr4pW+sXf90NeeayjcNaX3fFg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.29.7.tgz",
      "integrity": "sha512-N9ZErrD+yW5geCDtBqnOoxmR8+tNKiGuxKlDpuJxfsqpa2dFcexaziGAE/qoHLiDDreVNMupxGmSoNlyvsA3gw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/helpers/-/helpers-7.29.7.tgz",
      "integrity": "sha512-1k2lAGRMfHTcwuNYcCNUmaUffmQv8KWMfh2iJUUeRlwlwH4FdNG7mfPI10NPfLHJFThE4Tyr4mv7kTNZOiPuBg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/parser/-/parser-7.29.7.tgz",
      "integrity": "sha512-hnORnjP/1P/zFEndoeX+n+t1RwWRJiJpM/jO7FW32Kn9r5+sJB2JWOdYo4L6k78j15eCwY3Gm/7364B1EMwtNg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.7"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/template/-/template-7.29.7.tgz",
      "integrity": "sha512-puq+Gf35oI24FeN11LkoUQFqv9uwNeWpxXZi/Ji3rRIoKAzKnxRaZ+Gkj0vKS9ZCiTESfng1N9LyOyXvo+m+Gg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/types": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.7.tgz",
      "integrity": "sha512-EhlfNQtZ+NK22w5BM61ciuiq1m58ed33Wr1Xan//ZRTy6hgjnwyCffRYwzsGXdASJSUJ1guZILsErh1eQcl+zw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.7",
        "@babel/generator": "^7.29.7",
        "@babel/helper-globals": "^7.29.7",
        "@babel/parser": "^7.29.7",
        "@babel/template": "^7.29.7",
        "@babel/types": "^7.29.7",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/types/-/types-7.29.7.tgz",
      "integrity": "sha512-4zBIxpPzowiZpusoFkyGVwakdRJUyuH5PxQ/PrqghfdFWWasvnCdPfQXHrenDai+gyLARulZjZowCOj6fjT4pA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.29.7",
        "@babel/helper-validator-identifier": "^7.29.7"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@emnapi/core": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.11.1.tgz",
      "integrity": "sha512-RSvbQmHzdKzNsLYa/wHrbc3KN4sYLKAdPZxqiM2HATqv/SBk2/ENSHpvXGaLOMcsAyz0poEGqkmmKYG3OWiJEQ==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/wasi-threads": "1.2.2",
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.11.1",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.11.1.tgz",
      "integrity": "sha512-vgj7R3y3Wgx24IQaGPA/R6YFXLHVMOZ0uVEyIQPaWs+rd1AzfEMXlAC22FYwO1XkKR6NPsq7mUandH8oIRdZFw==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/wasi-threads": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.2.2.tgz",
      "integrity": "sha512-c95qOXkHdydNKhscBTebqEC1CVAZpyqOfVfBzQ1qgzyl3gfeldUjIggDbIZgDKsHLgnsM+igH7TJ/eAasaVuMA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@eslint-community/eslint-utils": {
      "version": "4.9.1",
      "resolved": "https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.9.1.tgz",
      "integrity": "sha512-phrYmNiYppR7znFEdqgfWHXR6NCkZEK7hwWDHZUjit/2/U0r6XvkDl0SYnoM51Hq7FhCGdLDT6zxCCOY1hexsQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "eslint-visitor-keys": "^3.4.3"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      },
      "peerDependencies": {
        "eslint": "^6.0.0 || ^7.0.0 || >=8.0.0"
      }
    },
    "node_modules/@eslint-community/eslint-utils/node_modules/eslint-visitor-keys": {
      "version": "3.4.3",
      "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.3.tgz",
      "integrity": "sha512-wpc+LXeiyiisxPlEkUzU6svyS1frIO3Mgxj1fdy7Pm8Ygzguax2N3Fa/D/ag1WqbOprdI+uY6wMUl8/a2G+iag==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/@eslint-community/regexpp": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz",
      "integrity": "sha512-EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
      }
    },
    "node_modules/@eslint/config-array": {
      "version": "0.23.5",
      "resolved": "https://registry.npmjs.org/@eslint/config-array/-/config-array-0.23.5.tgz",
      "integrity": "sha512-Y3kKLvC1dvTOT+oGlqNQ1XLqK6D1HU2YXPc52NmAlJZbMMWDzGYXMiPRJ8TYD39muD/OTjlZmNJ4ib7dvSrMBA==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@eslint/object-schema": "^3.0.5",
        "debug": "^4.3.1",
        "minimatch": "^10.2.4"
      },
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      }
    },
    "node_modules/@eslint/config-helpers": {
      "version": "0.6.0",
      "resolved": "https://registry.npmjs.org/@eslint/config-helpers/-/config-helpers-0.6.0.tgz",
      "integrity": "sha512-ii6Bw9jJ2zi2cWA2Z+9/QZ/+3DX6kwaV5Q986D/CdP3Lap3w/pgQZ373FV7byY/i7L4IRH/G43I5dz1ClsCbpA==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@eslint/core": "^1.2.1"
      },
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      }
    },
    "node_modules/@eslint/core": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/@eslint/core/-/core-1.2.1.tgz",
      "integrity": "sha512-MwcE1P+AZ4C6DWlpin/OmOA54mmIZ/+xZuJiQd4SyB29oAJjN30UW9wkKNptW2ctp4cEsvhlLY/CsQ1uoHDloQ==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@types/json-schema": "^7.0.15"
      },
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      }
    },
    "node_modules/@eslint/js": {
      "version": "10.0.1",
      "resolved": "https://registry.npmjs.org/@eslint/js/-/js-10.0.1.tgz",
      "integrity": "sha512-zeR9k5pd4gxjZ0abRoIaxdc7I3nDktoXZk2qOv9gCNWx3mVwEn32VRhyLaRsDiJjTs0xq/T8mfPtyuXu7GWBcA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      },
      "funding": {
        "url": "https://eslint.org/donate"
      },
      "peerDependencies": {
        "eslint": "^10.0.0"
      },
      "peerDependenciesMeta": {
        "eslint": {
          "optional": true
        }
      }
    },
    "node_modules/@eslint/object-schema": {
      "version": "3.0.5",
      "resolved": "https://registry.npmjs.org/@eslint/object-schema/-/object-schema-3.0.5.tgz",
      "integrity": "sha512-vqTaUEgxzm+YDSdElad6PiRoX4t8VGDjCtt05zn4nU810UIx/uNEV7/lZJ6KwFThKZOzOxzXy48da+No7HZaMw==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      }
    },
    "node_modules/@eslint/plugin-kit": {
      "version": "0.7.2",
      "resolved": "https://registry.npmjs.org/@eslint/plugin-kit/-/plugin-kit-0.7.2.tgz",
      "integrity": "sha512-+CNAzxglkrpNf/kKywqQfk74QjtceuOE7Qm+AF8miRvPF/wmmK5+OJOgVh3AVTT3RP2mH3+FOaxlE5v72owk0A==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@eslint/core": "^1.2.1",
        "levn": "^0.4.1"
      },
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      }
    },
    "node_modules/@humanfs/core": {
      "version": "0.19.2",
      "resolved": "https://registry.npmjs.org/@humanfs/core/-/core-0.19.2.tgz",
      "integrity": "sha512-UhXNm+CFMWcbChXywFwkmhqjs3PRCmcSa/hfBgLIb7oQ5HNb1wS0icWsGtSAUNgefHeI+eBrA8I1fxmbHsGdvA==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@humanfs/types": "^0.15.0"
      },
      "engines": {
        "node": ">=18.18.0"
      }
    },
    "node_modules/@humanfs/node": {
      "version": "0.16.8",
      "resolved": "https://registry.npmjs.org/@humanfs/node/-/node-0.16.8.tgz",
      "integrity": "sha512-gE1eQNZ3R++kTzFUpdGlpmy8kDZD/MLyHqDwqjkVQI0JMdI1D51sy1H958PNXYkM2rAac7e5/CnIKZrHtPh3BQ==",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@humanfs/core": "^0.19.2",
        "@humanfs/types": "^0.15.0",
        "@humanwhocodes/retry": "^0.4.0"
      },
      "engines": {
        "node": ">=18.18.0"
      }
    },
    "node_modules/@humanfs/types": {
      "version": "0.15.0",
      "resolved": "https://registry.npmjs.org/@humanfs/types/-/types-0.15.0.tgz",
      "integrity": "sha512-ZZ1w0aoQkwuUuC7Yf+7sdeaNfqQiiLcSRbfI08oAxqLtpXQr9AIVX7Ay7HLDuiLYAaFPu8oBYNq/QIi9URHJ3Q==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=18.18.0"
      }
    },
    "node_modules/@humanwhocodes/module-importer": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz",
      "integrity": "sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=12.22"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/nzakas"
      }
    },
    "node_modules/@humanwhocodes/retry": {
      "version": "0.4.3",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/retry/-/retry-0.4.3.tgz",
      "integrity": "sha512-bV0Tgo9K4hfPCek+aMAn81RppFKv2ySDQeMoSZuvTASywNTnVJCArCZE2FWqpvIatKu7VMRLWlR1EazvVhDyhQ==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=18.18"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/nzakas"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/remapping": {
      "version": "2.3.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/remapping/-/remapping-2.3.5.tgz",
      "integrity": "sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/gen-mapping": "^0.3.5",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@napi-rs/wasm-runtime": {
      "version": "1.1.6",
      "resolved": "https://registry.npmjs.org/@napi-rs/wasm-runtime/-/wasm-runtime-1.1.6.tgz",
      "integrity": "sha512-ZLv/JdUfkvOy9eCnnBaGfiO+XimbjebAeO+MRQqD/B+FR1tnRN0tpKSJHRbE8sFfS6aqsXZ67TQjfwfsxULVbg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@tybys/wasm-util": "^0.10.3"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/Brooooooklyn"
      },
      "peerDependencies": {
        "@emnapi/core": "^1.7.1",
        "@emnapi/runtime": "^1.7.1"
      }
    },
    "node_modules/@oxc-project/types": {
      "version": "0.139.0",
      "resolved": "https://registry.npmjs.org/@oxc-project/types/-/types-0.139.0.tgz",
      "integrity": "sha512-r9gHphtCs+1M7J0pw6Sn/hh/Wpa/iQrOOkrNAlVLF/gHq+/CJmHIWKKUUhdWjcD6CIa8idarspCsASiXCXvFUw==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/Boshen"
      }
    },
    "node_modules/@rolldown/binding-android-arm64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-android-arm64/-/binding-android-arm64-1.1.5.tgz",
      "integrity": "sha512-lZg8fqIv2v7FF237bwMgzGZEJvGL79/s5knJ/i6FmsGF4XXlzccZ4jb+TrFIxtSSxFtIpdsgrPZeMk1I9AFcyQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-arm64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-arm64/-/binding-darwin-arm64-1.1.5.tgz",
      "integrity": "sha512-51Bnx9pNiMRKSUNtBfySkNJ9vMU9Hh3I1ozDd6gyPPYzaXCfnptUcEZxXGYFn+ul2dtcMUiqGR1Yai2K10uoTw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-darwin-x64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-darwin-x64/-/binding-darwin-x64-1.1.5.tgz",
      "integrity": "sha512-Tm+gbfC0aHu1tBA/JvKQh32S0K6YgCHkiAF4/W6xX0K0RmNuc94VeK419dJoE65R5aRxmo+noZQSWrAMF6yb6g==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-freebsd-x64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-freebsd-x64/-/binding-freebsd-x64-1.1.5.tgz",
      "integrity": "sha512-JMzDKCCXq93YccG5gz3hvOs1oXRKAf0XYpfOS88e+wZrC8Iugj6j68867vrYZkvpDDpKn/KoKORThmchMpF6TA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm-gnueabihf": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm-gnueabihf/-/binding-linux-arm-gnueabihf-1.1.5.tgz",
      "integrity": "sha512-uML21j2K5TfPGutKxub+M+nLjZIrWjXQ5Grx4lCe/nimTj9B4L63zHpjXLl4y0L3mcm2htEQIb06oCG/szerNw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-gnu/-/binding-linux-arm64-gnu-1.1.5.tgz",
      "integrity": "sha512-navSiuTMogvnQoZoM/v+l3ZWo50/NTwSHSzheABx/RCnmUPaKwq9qSo4Br2OYRs21+Fz8uFqITZM3H4opOB0/Q==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-arm64-musl": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-arm64-musl/-/binding-linux-arm64-musl-1.1.5.tgz",
      "integrity": "sha512-lAryqH7IteztmCXQXk0etKj4wBQ7Gx5S6LjKhsgp9zb8I5bsuvU/2llH1hDQcjsFeqIsovMVN339/8pUDDBXxA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-ppc64-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-ppc64-gnu/-/binding-linux-ppc64-gnu-1.1.5.tgz",
      "integrity": "sha512-fsK/sNBnxzBlL4O1JNrZakVQxPspqpED5dLtNsZS9oOKmtSpdNIzxH2kkol5HYTWJN47sE20ztMJPxfZ89qGOg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-s390x-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-s390x-gnu/-/binding-linux-s390x-gnu-1.1.5.tgz",
      "integrity": "sha512-gLYb4BIadlfTOYT5gO503n8zQjXflgzpD0FcyKh0Mzx3rqCZKnHoJWV9xe1KXUJ5lx2JfcSHr/mhzS0PC/McAA==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-gnu": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-gnu/-/binding-linux-x64-gnu-1.1.5.tgz",
      "integrity": "sha512-FjcpEKUyJygHgs1o50VYNvkt5+7Le/VEdYt0AkRpkL33MnyQfwr8l5mXwMmfmTbyMPr5vJLC+8/Gd9gXnwU1QQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-linux-x64-musl": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-linux-x64-musl/-/binding-linux-x64-musl-1.1.5.tgz",
      "integrity": "sha512-Me+PfPI2TMeOQk0gYWfLQZtTktrmzbr8cDboqX83XKc7UrgAi55gF+2dUkWdxd19n55Essp2yeca+O9N5rBxHg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-openharmony-arm64": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-openharmony-arm64/-/binding-openharmony-arm64-1.1.5.tgz",
      "integrity": "sha512-yc5WrLzXks6zCQfn9Oxr8pORKyl/pF+QjHmW/Qx3qu0oyrrNC+y2JLTU1E2rcWYAmzlnqngWXHQjy51VzW70Vw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-wasm32-wasi": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-wasm32-wasi/-/binding-wasm32-wasi-1.1.5.tgz",
      "integrity": "sha512-VbQGPX2b4r48TAMIM2cjgluIM1HYutm4pcTEJsle7iEP7sB1dFqtPLBVbdLAZCxy1txCcPxf4QFf4v8uvltPqA==",
      "cpu": [
        "wasm32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/core": "1.11.1",
        "@emnapi/runtime": "1.11.1",
        "@napi-rs/wasm-runtime": "^1.1.6"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-win32-arm64-msvc": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-arm64-msvc/-/binding-win32-arm64-msvc-1.1.5.tgz",
      "integrity": "sha512-gHv82k63z4qpV5+Q1y/12KrK0ltWBukVDI8nZcbT7Tt/ZlOIVwppazneq0F93oDxTo3IgAMEDIoQh3E2n6mVsw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/binding-win32-x64-msvc": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/@rolldown/binding-win32-x64-msvc/-/binding-win32-x64-msvc-1.1.5.tgz",
      "integrity": "sha512-tTZuDBPw85tEN5PQi1pnEBzDy0Z49HtScLAbD5t6hyeU92A95pRWaSMw1GZZi/RwgSgUIl0xrSlXIT/9QzvYSA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@rolldown/pluginutils": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/@rolldown/pluginutils/-/pluginutils-1.0.1.tgz",
      "integrity": "sha512-2j9bGt5Jh8hj+vPtgzPtl72j0yRxHAyumoo6TNfAjsLB04UtpSvPbPcDcBMxz7n+9CYB0c1GxQFxYRg2jimqGw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@tybys/wasm-util": {
      "version": "0.10.3",
      "resolved": "https://registry.npmjs.org/@tybys/wasm-util/-/wasm-util-0.10.3.tgz",
      "integrity": "sha512-F3fo1MYrRJYL3zER0OUOmkutjr1Vp23m7OsSgp7nq4SP6OqX6C/56XFIPAl5bt3zaBRjmW7SGz3u/6LwFpYcOg==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@types/esrecurse": {
      "version": "4.3.1",
      "resolved": "https://registry.npmjs.org/@types/esrecurse/-/esrecurse-4.3.1.tgz",
      "integrity": "sha512-xJBAbDifo5hpffDBuHl0Y8ywswbiAp/Wi7Y/GtAgSlZyIABppyurxVueOPE8LUQOxdlgi6Zqce7uoEpqNTeiUw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/estree": {
      "version": "1.0.9",
      "resolved": "https://registry.npmjs.org/@types/estree/-/estree-1.0.9.tgz",
      "integrity": "sha512-GhdPgy1el4/ImP05X05Uw4cw2/M93BCUmnEvWZNStlCzEKME4Fkk+YpoA5OiHNQmoS7Cafb8Xa3Pya8m1Qrzeg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/json-schema": {
      "version": "7.0.15",
      "resolved": "https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz",
      "integrity": "sha512-5+fP8P8MFNC+AyZCDxrB2pkZFPGzqQWUzpSeuuVLvm8VMcorNYavBqoFcxK8bQz4Qsbn4oUEEem4wDLfcysGHA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/react": {
      "version": "19.2.17",
      "resolved": "https://registry.npmjs.org/@types/react/-/react-19.2.17.tgz",
      "integrity": "sha512-MXfmqaVPEVgkBT/aY0aGCkRWWtByiYQXo3xdQ8r5RzuFrPiRn8Gar2tQdXSUQ2GKV3bkXckek89V8wQBY2Q/Aw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "csstype": "^3.2.2"
      }
    },
    "node_modules/@types/react-dom": {
      "version": "19.2.3",
      "resolved": "https://registry.npmjs.org/@types/react-dom/-/react-dom-19.2.3.tgz",
      "integrity": "sha512-jp2L/eY6fn+KgVVQAOqYItbF0VY/YApe5Mz2F0aykSO8gx31bYCZyvSeYxCHKvzHG5eZjc+zyaS5BrBWya2+kQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "@types/react": "^19.2.0"
      }
    },
    "node_modules/@vitejs/plugin-react": {
      "version": "6.0.3",
      "resolved": "https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-6.0.3.tgz",
      "integrity": "sha512-vmFvco5/QuC2f9Oj+wTk0+9XeDFkHxSamwZKYc7MxYwKICfvUvlMhqKI0VuICPltGqh1neqBKDvO4kes1ya8vg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@rolldown/pluginutils": "^1.0.1"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "peerDependencies": {
        "@rolldown/plugin-babel": "^0.1.7 || ^0.2.0",
        "babel-plugin-react-compiler": "^1.0.0",
        "vite": "^8.0.0"
      },
      "peerDependenciesMeta": {
        "@rolldown/plugin-babel": {
          "optional": true
        },
        "babel-plugin-react-compiler": {
          "optional": true
        }
      }
    },
    "node_modules/acorn": {
      "version": "8.17.0",
      "resolved": "https://registry.npmjs.org/acorn/-/acorn-8.17.0.tgz",
      "integrity": "sha512-xRQbDb9BnwDafYNn6Vwl839DYVjqXYb1XVGtWAZ1kcDc6iwAL4hg3B1dZlRiuENFeO2H53gFG3in621AdERVAg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "acorn": "bin/acorn"
      },
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/acorn-jsx": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz",
      "integrity": "sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "acorn": "^6.0.0 || ^7.0.0 || ^8.0.0"
      }
    },
    "node_modules/agent-base": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz",
      "integrity": "sha512-RZNwNclF7+MS/8bDg70amg32dyeZGZxiDuQmZxKLAlQjr3jGyLx+4Kkk58UO7D2QdgFIQCovuSuZESne6RG6XQ==",
      "license": "MIT",
      "dependencies": {
        "debug": "4"
      },
      "engines": {
        "node": ">= 6.0.0"
      }
    },
    "node_modules/ajv": {
      "version": "6.15.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-6.15.0.tgz",
      "integrity": "sha512-fgFx7Hfoq60ytK2c7DhnF8jIvzYgOMxfugjLOSMHjLIPgenqa7S7oaagATUq99mV6IYvN2tRmC0wnTYX6iPbMw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fast-deep-equal": "^3.1.1",
        "fast-json-stable-stringify": "^2.0.0",
        "json-schema-traverse": "^0.4.1",
        "uri-js": "^4.2.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/asynckit": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz",
      "integrity": "sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==",
      "license": "MIT"
    },
    "node_modules/axios": {
      "version": "1.19.0",
      "resolved": "https://registry.npmjs.org/axios/-/axios-1.19.0.tgz",
      "integrity": "sha512-ht/iuYZXEjFxLH/Hkezgd7m6JKlHHXEUSneaDz8uZe1Gj5QZtCnpyDsckvAiEnT89OEbCLmnte4R4sn7P0EKFw==",
      "license": "MIT",
      "dependencies": {
        "follow-redirects": "^1.16.0",
        "form-data": "^4.0.6",
        "https-proxy-agent": "^5.0.1",
        "proxy-from-env": "^2.1.0"
      }
    },
    "node_modules/balanced-match": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-4.0.4.tgz",
      "integrity": "sha512-BLrgEcRTwX2o6gGxGOCNyMvGSp35YofuYzw9h1IMTRmKqttAZZVU67bdb9Pr2vUHA8+j3i2tJfjO6C6+4myGTA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "18 || 20 || >=22"
      }
    },
    "node_modules/baseline-browser-mapping": {
      "version": "2.10.43",
      "resolved": "https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.10.43.tgz",
      "integrity": "sha512-AjYpR78kDWAY3Efj+cDTFH9t9SCoL7OoTp1BOb0mQV7S+6CiLwnWM3FyxhJtdPufDFKzmCSFoUncKjWgJEZTCQ==",
      "dev": true,
      "license": "Apache-2.0",
      "bin": {
        "baseline-browser-mapping": "dist/cli.cjs"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/brace-expansion": {
      "version": "5.0.7",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-5.0.7.tgz",
      "integrity": "sha512-7oFy703dxfY3/NLxC1fh2SUCQ0H9rmAY+5EpDVfXjUTTs+HEwR2nYaqLv+GWcTsumwxPfiz6CzCNkwXwBUwqCA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "balanced-match": "^4.0.2"
      },
      "engines": {
        "node": "18 || 20 || >=22"
      }
    },
    "node_modules/browserslist": {
      "version": "4.28.6",
      "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.28.6.tgz",
      "integrity": "sha512-FQBYNK15VMslhLHpA7+n+n1GOlF1kId2xcCg7/j95f24AOF6VDYMNH4mFxF7KuaTdv627faazpOAjFzMrfJOUw==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "baseline-browser-mapping": "^2.10.42",
        "caniuse-lite": "^1.0.30001803",
        "electron-to-chromium": "^1.5.389",
        "node-releases": "^2.0.51",
        "update-browserslist-db": "^1.2.3"
      },
      "bin": {
        "browserslist": "cli.js"
      },
      "engines": {
        "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
      }
    },
    "node_modules/call-bind-apply-helpers": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz",
      "integrity": "sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/caniuse-lite": {
      "version": "1.0.30001806",
      "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001806.tgz",
      "integrity": "sha512-72Cuvd95zbSYPKq6Fhg8eDJRlzgWDf7/mtoZv6Qe/DYNCEBdNxoA3+rZAU2ZhGCpZlns3EssFavaZomckT5Uuw==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "CC-BY-4.0"
    },
    "node_modules/combined-stream": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz",
      "integrity": "sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==",
      "license": "MIT",
      "dependencies": {
        "delayed-stream": "~1.0.0"
      },
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/convert-source-map": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz",
      "integrity": "sha512-Kvp459HrV2FEJ1CAsi1Ku+MY3kasH19TFykTz2xWmMeq6bk2NU3XXvfJ+Q61m0xktWwt+1HSYf3JZsTms3aRJg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/cookie": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/cookie/-/cookie-1.1.1.tgz",
      "integrity": "sha512-ei8Aos7ja0weRpFzJnEA9UHJ/7XQmqglbRwnf2ATjcB9Wq874VKH9kfjjirM6UhU2/E5fFYadylyhFldcqSidQ==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/express"
      }
    },
    "node_modules/cross-spawn": {
      "version": "7.0.6",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
      "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/csstype": {
      "version": "3.2.3",
      "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz",
      "integrity": "sha512-z1HGKcYy2xA8AGQfwrn0PAy+PB7X/GSj3UVJW9qKyn43xWa+gl5nXmU4qqLMRzWVLFC8KusUX8T/0kCiOYpAIQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/debug": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/debug/-/debug-4.4.3.tgz",
      "integrity": "sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==",
      "license": "MIT",
      "dependencies": {
        "ms": "^2.1.3"
      },
      "engines": {
        "node": ">=6.0"
      },
      "peerDependenciesMeta": {
        "supports-color": {
          "optional": true
        }
      }
    },
    "node_modules/deep-is": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz",
      "integrity": "sha512-oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/delayed-stream": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz",
      "integrity": "sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.4.0"
      }
    },
    "node_modules/detect-libc": {
      "version": "2.1.2",
      "resolved": "https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz",
      "integrity": "sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/dunder-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz",
      "integrity": "sha512-KIN/nDJBQRcXw0MLVhZE9iQHmG68qAVIBg9CqmUYjmQIhgij9U5MFvrqkUL5FbtyyzZuOeOt0zdeRe4UY7ct+A==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.1",
        "es-errors": "^1.3.0",
        "gopd": "^1.2.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/electron-to-chromium": {
      "version": "1.5.393",
      "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.393.tgz",
      "integrity": "sha512-kiDJdIUawuEIcp9XoICKp1iTYDEbgguIPq526N1Q7jIQDeQ3CqoMx71025PI/7E48Ddtw2HuWsVjY7afEgNxmg==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/es-define-property": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz",
      "integrity": "sha512-e3nRfgfUZ4rNGL232gUgX06QNyyez04KdjFrF+LTRoOXmrOgFKDg4BCdsjW8EnT69eqdYGmRpJwiPVYNrCaW3g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-errors": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz",
      "integrity": "sha512-Zf5H2Kxt2xjTvbJvP2ZWLEICxA6j+hAmMzIlypy4xcBg1vKVnx89Wy0GbS+kf5cwCVFFzdCFh2XSCFNULS6csw==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-object-atoms": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.2.tgz",
      "integrity": "sha512-HWcBoN6NileqtSydK2FqHbS/LoDd2pqrnQHLyJzBj4kOp/ky2MWMN694xOfkK8/SnUsW2DH7EfyVlydKCsm1Zw==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/es-set-tostringtag": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz",
      "integrity": "sha512-j6vWzfrGVfyXxge+O0x5sh6cvxAog0a/4Rdd2K36zCMV5eJ+/+tOAngRO8cODMNWbVRdVlmGZQL2YS3yR8bIUA==",
      "license": "MIT",
      "dependencies": {
        "es-errors": "^1.3.0",
        "get-intrinsic": "^1.2.6",
        "has-tostringtag": "^1.0.2",
        "hasown": "^2.0.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/escalade": {
      "version": "3.2.0",
      "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
      "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/escape-string-regexp": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz",
      "integrity": "sha512-TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/eslint": {
      "version": "10.7.0",
      "resolved": "https://registry.npmjs.org/eslint/-/eslint-10.7.0.tgz",
      "integrity": "sha512-GVTD7s1vdIl6UYvAfriOPeY1Df8LIZjfofLvHwde+erDHGGuHyuM6xoxRxmHiebhYuD2p1vN4wWh0XzPARSGDQ==",
      "dev": true,
      "license": "MIT",
      "workspaces": [
        "packages/*"
      ],
      "dependencies": {
        "@eslint-community/eslint-utils": "^4.8.0",
        "@eslint-community/regexpp": "^4.12.2",
        "@eslint/config-array": "^0.23.5",
        "@eslint/config-helpers": "^0.6.0",
        "@eslint/core": "^1.2.1",
        "@eslint/plugin-kit": "^0.7.2",
        "@humanfs/node": "^0.16.6",
        "@humanwhocodes/module-importer": "^1.0.1",
        "@humanwhocodes/retry": "^0.4.2",
        "@types/estree": "^1.0.6",
        "ajv": "^6.14.0",
        "cross-spawn": "^7.0.6",
        "debug": "^4.3.2",
        "escape-string-regexp": "^4.0.0",
        "eslint-scope": "^9.1.2",
        "eslint-visitor-keys": "^5.0.1",
        "espree": "^11.2.0",
        "esquery": "^1.7.0",
        "esutils": "^2.0.2",
        "fast-deep-equal": "^3.1.3",
        "file-entry-cache": "^8.0.0",
        "find-up": "^5.0.0",
        "glob-parent": "^6.0.2",
        "ignore": "^5.2.0",
        "imurmurhash": "^0.1.4",
        "is-glob": "^4.0.0",
        "json-stable-stringify-without-jsonify": "^1.0.1",
        "minimatch": "^10.2.4",
        "natural-compare": "^1.4.0",
        "optionator": "^0.9.3"
      },
      "bin": {
        "eslint": "bin/eslint.js"
      },
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      },
      "funding": {
        "url": "https://eslint.org/donate"
      },
      "peerDependencies": {
        "jiti": "*"
      },
      "peerDependenciesMeta": {
        "jiti": {
          "optional": true
        }
      }
    },
    "node_modules/eslint-plugin-react-hooks": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/eslint-plugin-react-hooks/-/eslint-plugin-react-hooks-7.1.1.tgz",
      "integrity": "sha512-f2I7Gw6JbvCexzIInuSbZpfdQ44D7iqdWX01FKLvrPgqxoE7oMj8clOfto8U6vYiz4yd5oKu39rRSVOe1zRu0g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/core": "^7.24.4",
        "@babel/parser": "^7.24.4",
        "hermes-parser": "^0.25.1",
        "zod": "^3.25.0 || ^4.0.0",
        "zod-validation-error": "^3.5.0 || ^4.0.0"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "eslint": "^3.0.0 || ^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0-0 || ^9.0.0 || ^10.0.0"
      }
    },
    "node_modules/eslint-plugin-react-refresh": {
      "version": "0.5.3",
      "resolved": "https://registry.npmjs.org/eslint-plugin-react-refresh/-/eslint-plugin-react-refresh-0.5.3.tgz",
      "integrity": "sha512-5EMmLCV98Pi4o/f/3DP/v/tNqLHMIc9I8LKClNDWhZ9JTho89/kQcitCXQBMG7sAfVRK0Ie3T2EDOzp1YXYiVA==",
      "dev": true,
      "license": "MIT",
      "peerDependencies": {
        "eslint": "^9 || ^10"
      }
    },
    "node_modules/eslint-scope": {
      "version": "9.1.2",
      "resolved": "https://registry.npmjs.org/eslint-scope/-/eslint-scope-9.1.2.tgz",
      "integrity": "sha512-xS90H51cKw0jltxmvmHy2Iai1LIqrfbw57b79w/J7MfvDfkIkFZ+kj6zC3BjtUwh150HsSSdxXZcsuv72miDFQ==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "@types/esrecurse": "^4.3.1",
        "@types/estree": "^1.0.8",
        "esrecurse": "^4.3.0",
        "estraverse": "^5.2.0"
      },
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/eslint-visitor-keys": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-5.0.1.tgz",
      "integrity": "sha512-tD40eHxA35h0PEIZNeIjkHoDR4YjjJp34biM0mDvplBe//mB+IHCqHDGV7pxF+7MklTvighcCPPZC7ynWyjdTA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/espree": {
      "version": "11.2.0",
      "resolved": "https://registry.npmjs.org/espree/-/espree-11.2.0.tgz",
      "integrity": "sha512-7p3DrVEIopW1B1avAGLuCSh1jubc01H2JHc8B4qqGblmg5gI9yumBgACjWo4JlIc04ufug4xJ3SQI8HkS/Rgzw==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "acorn": "^8.16.0",
        "acorn-jsx": "^5.3.2",
        "eslint-visitor-keys": "^5.0.1"
      },
      "engines": {
        "node": "^20.19.0 || ^22.13.0 || >=24"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/esquery": {
      "version": "1.7.0",
      "resolved": "https://registry.npmjs.org/esquery/-/esquery-1.7.0.tgz",
      "integrity": "sha512-Ap6G0WQwcU/LHsvLwON1fAQX9Zp0A2Y6Y/cJBl9r/JbW90Zyg4/zbG6zzKa2OTALELarYHmKu0GhpM5EO+7T0g==",
      "dev": true,
      "license": "BSD-3-Clause",
      "dependencies": {
        "estraverse": "^5.1.0"
      },
      "engines": {
        "node": ">=0.10"
      }
    },
    "node_modules/esrecurse": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz",
      "integrity": "sha512-KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "estraverse": "^5.2.0"
      },
      "engines": {
        "node": ">=4.0"
      }
    },
    "node_modules/estraverse": {
      "version": "5.3.0",
      "resolved": "https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz",
      "integrity": "sha512-MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==",
      "dev": true,
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=4.0"
      }
    },
    "node_modules/esutils": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz",
      "integrity": "sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==",
      "dev": true,
      "license": "BSD-2-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/fast-deep-equal": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz",
      "integrity": "sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/fast-json-stable-stringify": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz",
      "integrity": "sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/fast-levenshtein": {
      "version": "2.0.6",
      "resolved": "https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz",
      "integrity": "sha512-DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/fdir": {
      "version": "6.5.0",
      "resolved": "https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz",
      "integrity": "sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12.0.0"
      },
      "peerDependencies": {
        "picomatch": "^3 || ^4"
      },
      "peerDependenciesMeta": {
        "picomatch": {
          "optional": true
        }
      }
    },
    "node_modules/file-entry-cache": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/file-entry-cache/-/file-entry-cache-8.0.0.tgz",
      "integrity": "sha512-XXTUwCvisa5oacNGRP9SfNtYBNAMi+RPwBFmblZEF7N7swHYQS6/Zfk7SRwx4D5j3CH211YNRco1DEMNVfZCnQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "flat-cache": "^4.0.0"
      },
      "engines": {
        "node": ">=16.0.0"
      }
    },
    "node_modules/find-up": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz",
      "integrity": "sha512-78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "locate-path": "^6.0.0",
        "path-exists": "^4.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/flat-cache": {
      "version": "4.0.1",
      "resolved": "https://registry.npmjs.org/flat-cache/-/flat-cache-4.0.1.tgz",
      "integrity": "sha512-f7ccFPK3SXFHpx15UIGyRJ/FJQctuKZ0zVuN3frBo4HnK3cay9VEW0R6yPYFHC0AgqhukPzKjq22t5DmAyqGyw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "flatted": "^3.2.9",
        "keyv": "^4.5.4"
      },
      "engines": {
        "node": ">=16"
      }
    },
    "node_modules/flatted": {
      "version": "3.4.2",
      "resolved": "https://registry.npmjs.org/flatted/-/flatted-3.4.2.tgz",
      "integrity": "sha512-PjDse7RzhcPkIJwy5t7KPWQSZ9cAbzQXcafsetQoD7sOJRQlGikNbx7yZp2OotDnJyrDcbyRq3Ttb18iYOqkxA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/follow-redirects": {
      "version": "1.16.0",
      "resolved": "https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.16.0.tgz",
      "integrity": "sha512-y5rN/uOsadFT/JfYwhxRS5R7Qce+g3zG97+JrtFZlC9klX/W5hD7iiLzScI4nZqUS7DNUdhPgw4xI8W2LuXlUw==",
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "license": "MIT",
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    },
    "node_modules/form-data": {
      "version": "4.0.6",
      "resolved": "https://registry.npmjs.org/form-data/-/form-data-4.0.6.tgz",
      "integrity": "sha512-vKatAh4SlVfgbv+YtmhiRjhEMJsYpsG1Y2rMQtR+SVSbytsSD1YGzDIcrAJmdFec88u/+VoGmxnl+80gL1tRCQ==",
      "license": "MIT",
      "dependencies": {
        "asynckit": "^0.4.0",
        "combined-stream": "^1.0.8",
        "es-set-tostringtag": "^2.1.0",
        "hasown": "^2.0.4",
        "mime-types": "^2.1.35"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
      }
    },
    "node_modules/function-bind": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
      "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/gensync": {
      "version": "1.0.0-beta.2",
      "resolved": "https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz",
      "integrity": "sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/get-intrinsic": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz",
      "integrity": "sha512-9fSjSaos/fRIVIp+xSJlE6lfwhES7LNtKaCBIamHsjr2na1BiABJPo0mOjjz8GJDURarmCPGqaiVg5mfjb98CQ==",
      "license": "MIT",
      "dependencies": {
        "call-bind-apply-helpers": "^1.0.2",
        "es-define-property": "^1.0.1",
        "es-errors": "^1.3.0",
        "es-object-atoms": "^1.1.1",
        "function-bind": "^1.1.2",
        "get-proto": "^1.0.1",
        "gopd": "^1.2.0",
        "has-symbols": "^1.1.0",
        "hasown": "^2.0.2",
        "math-intrinsics": "^1.1.0"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/get-proto": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz",
      "integrity": "sha512-sTSfBjoXBp89JvIKIefqw7U2CCebsc74kiY6awiGogKtoSGbgjYE/G/+l9sF3MWFPNc9IcoOC4ODfKHfxFmp0g==",
      "license": "MIT",
      "dependencies": {
        "dunder-proto": "^1.0.1",
        "es-object-atoms": "^1.0.0"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/glob-parent": {
      "version": "6.0.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz",
      "integrity": "sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "is-glob": "^4.0.3"
      },
      "engines": {
        "node": ">=10.13.0"
      }
    },
    "node_modules/globals": {
      "version": "17.7.0",
      "resolved": "https://registry.npmjs.org/globals/-/globals-17.7.0.tgz",
      "integrity": "sha512-Czmyns5dUsq4seFBR/Kdydhmo8y9kC79hiSkPn0YcGtNnYWnrgt0vjrSjx9tspoDGWm2CMarffRuLjM4xUz8xg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/gopd": {
      "version": "1.2.0",
      "resolved": "https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz",
      "integrity": "sha512-ZUKRh6/kUFoAiTAtTYPZJ3hw9wNxx+BIBOijnlG9PnrJsCcSjs1wyyD6vJpaYtgnzDrKYRSqf3OO6Rfa93xsRg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-symbols": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz",
      "integrity": "sha512-1cDNdwJ2Jaohmb3sg4OmKaMBwuC48sYni5HUw2DvsC8LjGTLK9h+eb1X6RyuOHe4hT0ULCW68iomhjUoKUqlPQ==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/has-tostringtag": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz",
      "integrity": "sha512-NqADB8VjPFLM2V0VvHUewwwsw0ZWBaIdgo+ieHtK3hasLz4qeCRjYcqfB6AQrBggRKppKF8L52/VqdVsO47Dlw==",
      "license": "MIT",
      "dependencies": {
        "has-symbols": "^1.0.3"
      },
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/hasown": {
      "version": "2.0.4",
      "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.4.tgz",
      "integrity": "sha512-T2UbfbBEF32wiepXIsMlTW9+dDYC6wMh/t/vYA4tuOMKqWz/n3vr1NFSxQiyP+zk2mXsoMA/i/7qV6LKut1t1A==",
      "license": "MIT",
      "dependencies": {
        "function-bind": "^1.1.2"
      },
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/hermes-estree": {
      "version": "0.25.1",
      "resolved": "https://registry.npmjs.org/hermes-estree/-/hermes-estree-0.25.1.tgz",
      "integrity": "sha512-0wUoCcLp+5Ev5pDW2OriHC2MJCbwLwuRx+gAqMTOkGKJJiBCLjtrvy4PWUGn6MIVefecRpzoOZ/UV6iGdOr+Cw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/hermes-parser": {
      "version": "0.25.1",
      "resolved": "https://registry.npmjs.org/hermes-parser/-/hermes-parser-0.25.1.tgz",
      "integrity": "sha512-6pEjquH3rqaI6cYAXYPcz9MS4rY6R4ngRgrgfDshRptUZIc3lw0MCIJIGDj9++mfySOuPTHB4nrSW99BCvOPIA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "hermes-estree": "0.25.1"
      }
    },
    "node_modules/https-proxy-agent": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.1.tgz",
      "integrity": "sha512-dFcAjpTQFgoLMzC2VwU+C/CbS7uRL0lWmxDITmqm7C+7F0Odmj6s9l6alZc6AELXhrnggM2CeWSXHGOdX2YtwA==",
      "license": "MIT",
      "dependencies": {
        "agent-base": "6",
        "debug": "4"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/ignore": {
      "version": "5.3.2",
      "resolved": "https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz",
      "integrity": "sha512-hsBTNUqQTDwkWtcdYI2i06Y/nUBEsNEDJKjWdigLvegy8kDuJAS8uRlpkkcQpyEXL0Z/pjDy5HBmMjRCJ2gq+g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 4"
      }
    },
    "node_modules/imurmurhash": {
      "version": "0.1.4",
      "resolved": "https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz",
      "integrity": "sha512-JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.8.19"
      }
    },
    "node_modules/is-extglob": {
      "version": "2.1.1",
      "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
      "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/is-glob": {
      "version": "4.0.3",
      "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
      "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "is-extglob": "^2.1.1"
      },
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/isexe": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz",
      "integrity": "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/js-tokens": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
      "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/jsesc": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz",
      "integrity": "sha512-/sM3dO2FOzXjKQhJuo0Q173wf2KOo8t4I8vHy6lF9poUp7bKT0/NHE8fPX23PwfhnykfqnC2xRxOnVw5XuGIaA==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "jsesc": "bin/jsesc"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/json-buffer": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/json-buffer/-/json-buffer-3.0.1.tgz",
      "integrity": "sha512-4bV5BfR2mqfQTJm+V5tPPdf+ZpuhiIvTuAB5g8kcrXOZpTT/QwwVRWBywX1ozr6lEuPdbHxwaJlm9G6mI2sfSQ==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/json-schema-traverse": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz",
      "integrity": "sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/json-stable-stringify-without-jsonify": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz",
      "integrity": "sha512-Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/json5": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/json5/-/json5-2.2.3.tgz",
      "integrity": "sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==",
      "dev": true,
      "license": "MIT",
      "bin": {
        "json5": "lib/cli.js"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/keyv": {
      "version": "4.5.4",
      "resolved": "https://registry.npmjs.org/keyv/-/keyv-4.5.4.tgz",
      "integrity": "sha512-oxVHkHR/EJf2CNXnWxRLW6mg7JyCCUcG0DtEGmL2ctUo1PNTin1PUil+r/+4r5MpVgC/fn1kjsx7mjSujKqIpw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "json-buffer": "3.0.1"
      }
    },
    "node_modules/levn": {
      "version": "0.4.1",
      "resolved": "https://registry.npmjs.org/levn/-/levn-0.4.1.tgz",
      "integrity": "sha512-+bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "prelude-ls": "^1.2.1",
        "type-check": "~0.4.0"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/lightningcss": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss/-/lightningcss-1.32.0.tgz",
      "integrity": "sha512-NXYBzinNrblfraPGyrbPoD19C1h9lfI/1mzgWYvXUTe414Gz/X1FD2XBZSZM7rRTrMA8JL3OtAaGifrIKhQ5yQ==",
      "dev": true,
      "license": "MPL-2.0",
      "dependencies": {
        "detect-libc": "^2.0.3"
      },
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      },
      "optionalDependencies": {
        "lightningcss-android-arm64": "1.32.0",
        "lightningcss-darwin-arm64": "1.32.0",
        "lightningcss-darwin-x64": "1.32.0",
        "lightningcss-freebsd-x64": "1.32.0",
        "lightningcss-linux-arm-gnueabihf": "1.32.0",
        "lightningcss-linux-arm64-gnu": "1.32.0",
        "lightningcss-linux-arm64-musl": "1.32.0",
        "lightningcss-linux-x64-gnu": "1.32.0",
        "lightningcss-linux-x64-musl": "1.32.0",
        "lightningcss-win32-arm64-msvc": "1.32.0",
        "lightningcss-win32-x64-msvc": "1.32.0"
      }
    },
    "node_modules/lightningcss-android-arm64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-android-arm64/-/lightningcss-android-arm64-1.32.0.tgz",
      "integrity": "sha512-YK7/ClTt4kAK0vo6w3X+Pnm0D2cf2vPHbhOXdoNti1Ga0al1P4TBZhwjATvjNwLEBCnKvjJc2jQgHXH0NEwlAg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-darwin-arm64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-arm64/-/lightningcss-darwin-arm64-1.32.0.tgz",
      "integrity": "sha512-RzeG9Ju5bag2Bv1/lwlVJvBE3q6TtXskdZLLCyfg5pt+HLz9BqlICO7LZM7VHNTTn/5PRhHFBSjk5lc4cmscPQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-darwin-x64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-darwin-x64/-/lightningcss-darwin-x64-1.32.0.tgz",
      "integrity": "sha512-U+QsBp2m/s2wqpUYT/6wnlagdZbtZdndSmut/NJqlCcMLTWp5muCrID+K5UJ6jqD2BFshejCYXniPDbNh73V8w==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-freebsd-x64": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-freebsd-x64/-/lightningcss-freebsd-x64-1.32.0.tgz",
      "integrity": "sha512-JCTigedEksZk3tHTTthnMdVfGf61Fky8Ji2E4YjUTEQX14xiy/lTzXnu1vwiZe3bYe0q+SpsSH/CTeDXK6WHig==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm-gnueabihf": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm-gnueabihf/-/lightningcss-linux-arm-gnueabihf-1.32.0.tgz",
      "integrity": "sha512-x6rnnpRa2GL0zQOkt6rts3YDPzduLpWvwAF6EMhXFVZXD4tPrBkEFqzGowzCsIWsPjqSK+tyNEODUBXeeVHSkw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm64-gnu": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-gnu/-/lightningcss-linux-arm64-gnu-1.32.0.tgz",
      "integrity": "sha512-0nnMyoyOLRJXfbMOilaSRcLH3Jw5z9HDNGfT/gwCPgaDjnx0i8w7vBzFLFR1f6CMLKF8gVbebmkUN3fa/kQJpQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-arm64-musl": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-arm64-musl/-/lightningcss-linux-arm64-musl-1.32.0.tgz",
      "integrity": "sha512-UpQkoenr4UJEzgVIYpI80lDFvRmPVg6oqboNHfoH4CQIfNA+HOrZ7Mo7KZP02dC6LjghPQJeBsvXhJod/wnIBg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-x64-gnu": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-gnu/-/lightningcss-linux-x64-gnu-1.32.0.tgz",
      "integrity": "sha512-V7Qr52IhZmdKPVr+Vtw8o+WLsQJYCTd8loIfpDaMRWGUZfBOYEJeyJIkqGIDMZPwPx24pUMfwSxxI8phr/MbOA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "glibc"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-linux-x64-musl": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-linux-x64-musl/-/lightningcss-linux-x64-musl-1.32.0.tgz",
      "integrity": "sha512-bYcLp+Vb0awsiXg/80uCRezCYHNg1/l3mt0gzHnWV9XP1W5sKa5/TCdGWaR/zBM2PeF/HbsQv/j2URNOiVuxWg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "libc": [
        "musl"
      ],
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-win32-arm64-msvc": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-arm64-msvc/-/lightningcss-win32-arm64-msvc-1.32.0.tgz",
      "integrity": "sha512-8SbC8BR40pS6baCM8sbtYDSwEVQd4JlFTOlaD3gWGHfThTcABnNDBda6eTZeqbofalIJhFx0qKzgHJmcPTnGdw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/lightningcss-win32-x64-msvc": {
      "version": "1.32.0",
      "resolved": "https://registry.npmjs.org/lightningcss-win32-x64-msvc/-/lightningcss-win32-x64-msvc-1.32.0.tgz",
      "integrity": "sha512-Amq9B/SoZYdDi1kFrojnoqPLxYhQ4Wo5XiL8EVJrVsB8ARoC1PWW6VGtT0WKCemjy8aC+louJnjS7U18x3b06Q==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MPL-2.0",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">= 12.0.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/parcel"
      }
    },
    "node_modules/locate-path": {
      "version": "6.0.0",
      "resolved": "https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz",
      "integrity": "sha512-iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "p-locate": "^5.0.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/lru-cache": {
      "version": "5.1.1",
      "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz",
      "integrity": "sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "yallist": "^3.0.2"
      }
    },
    "node_modules/math-intrinsics": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz",
      "integrity": "sha512-/IXtbwEk5HTPyEwyKX6hGkYXxM9nbj64B+ilVJnC/R6B0pH5G4V3b0pVbL7DBj4tkhBAppbQUlf6F6Xl9LHu1g==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.4"
      }
    },
    "node_modules/mime-db": {
      "version": "1.52.0",
      "resolved": "https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz",
      "integrity": "sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==",
      "license": "MIT",
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/mime-types": {
      "version": "2.1.35",
      "resolved": "https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz",
      "integrity": "sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==",
      "license": "MIT",
      "dependencies": {
        "mime-db": "1.52.0"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/minimatch": {
      "version": "10.2.5",
      "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-10.2.5.tgz",
      "integrity": "sha512-MULkVLfKGYDFYejP07QOurDLLQpcjk7Fw+7jXS2R2czRQzR56yHRveU5NDJEOviH+hETZKSkIk5c+T23GjFUMg==",
      "dev": true,
      "license": "BlueOak-1.0.0",
      "dependencies": {
        "brace-expansion": "^5.0.5"
      },
      "engines": {
        "node": "18 || 20 || >=22"
      },
      "funding": {
        "url": "https://github.com/sponsors/isaacs"
      }
    },
    "node_modules/ms": {
      "version": "2.1.3",
      "resolved": "https://registry.npmjs.org/ms/-/ms-2.1.3.tgz",
      "integrity": "sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==",
      "license": "MIT"
    },
    "node_modules/nanoid": {
      "version": "3.3.16",
      "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.16.tgz",
      "integrity": "sha512-bzlKTyNJ7+LdGIIwy8ijFpIqEQIvafahV7eYykJ8Cvh42EdJeODoJ6gUJXpQJvej1BddH8OqTXZNE/KfbWAu8Q==",
      "dev": true,
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "bin": {
        "nanoid": "bin/nanoid.cjs"
      },
      "engines": {
        "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
      }
    },
    "node_modules/natural-compare": {
      "version": "1.4.0",
      "resolved": "https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz",
      "integrity": "sha512-OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/node-releases": {
      "version": "2.0.51",
      "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.51.tgz",
      "integrity": "sha512-wRNIrw4DmVLKQlbgOMdkMx27Wrpzes2hh5Jtbi2bjPd+4wJstWIqP5A+lscnqbm0xxmT5Bpg8Lec5ItEBwx6BQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/optionator": {
      "version": "0.9.4",
      "resolved": "https://registry.npmjs.org/optionator/-/optionator-0.9.4.tgz",
      "integrity": "sha512-6IpQ7mKUxRcZNLIObR0hz7lxsapSSIYNZJwXPGeF0mTVqGKFIXj1DQcMoT22S3ROcLyY/rz0PWaWZ9ayWmad9g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "deep-is": "^0.1.3",
        "fast-levenshtein": "^2.0.6",
        "levn": "^0.4.1",
        "prelude-ls": "^1.2.1",
        "type-check": "^0.4.0",
        "word-wrap": "^1.2.5"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/p-limit": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz",
      "integrity": "sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "yocto-queue": "^0.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/p-locate": {
      "version": "5.0.0",
      "resolved": "https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz",
      "integrity": "sha512-LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "p-limit": "^3.0.2"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/path-exists": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz",
      "integrity": "sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/path-key": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz",
      "integrity": "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/picocolors": {
      "version": "1.1.1",
      "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
      "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/picomatch": {
      "version": "4.0.5",
      "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-4.0.5.tgz",
      "integrity": "sha512-RvwwcruNjI1ncT5xRakeyS9Lf8lcItv34KD+aif+VH9kduAyfYBipGh12274xtenIPZ119/R9BdTBa8gAwSh0A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/jonschlinkert"
      }
    },
    "node_modules/postcss": {
      "version": "8.5.19",
      "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.19.tgz",
      "integrity": "sha512-Mz8SaolMd8nB+G13WkORcxQKHZ/NE4xXevtkJHVuG+guo9/wYKlIMTKAqGdEmYOXR2ijPjTYNHssizdaVSUNdQ==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/postcss/"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/postcss"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "nanoid": "^3.3.12",
        "picocolors": "^1.1.1",
        "source-map-js": "^1.2.1"
      },
      "engines": {
        "node": "^10 || ^12 || >=14"
      }
    },
    "node_modules/prelude-ls": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.2.1.tgz",
      "integrity": "sha512-vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/proxy-from-env": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-2.1.0.tgz",
      "integrity": "sha512-cJ+oHTW1VAEa8cJslgmUZrc+sjRKgAKl3Zyse6+PV38hZe/V6Z14TbCuXcan9F9ghlz4QrFr2c92TNF82UkYHA==",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/punycode": {
      "version": "2.3.1",
      "resolved": "https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz",
      "integrity": "sha512-vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/react": {
      "version": "19.2.7",
      "resolved": "https://registry.npmjs.org/react/-/react-19.2.7.tgz",
      "integrity": "sha512-HNe9WslTbXmFK8o8cmwgAeJFSBvt1bPdHCVKtaaV+WlAN36mpT4hcRpwbf3fY56ar2oIXzsBpOAiIRHAdY0OlQ==",
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/react-dom": {
      "version": "19.2.7",
      "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-19.2.7.tgz",
      "integrity": "sha512-t0BRVXvbiE/o20Hfw669rLbMCDWtYZLvmJigy2f0MxsXF+71pxhR3xOkspmsO8h3ZlNzyibAmtCa3l4lYKk6gQ==",
      "license": "MIT",
      "dependencies": {
        "scheduler": "^0.27.0"
      },
      "peerDependencies": {
        "react": "^19.2.7"
      }
    },
    "node_modules/react-router": {
      "version": "7.18.1",
      "resolved": "https://registry.npmjs.org/react-router/-/react-router-7.18.1.tgz",
      "integrity": "sha512-GDLgg3i3uM0aeJO3Fm+TCS+sDQ7gu12T6x0qdTEzcwqEfleci7JwugVNIF3U//0FWKnJT7ptG+20B2jfDqnZAg==",
      "license": "MIT",
      "dependencies": {
        "cookie": "^1.0.1",
        "set-cookie-parser": "^2.6.0"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "react": ">=18",
        "react-dom": ">=18"
      },
      "peerDependenciesMeta": {
        "react-dom": {
          "optional": true
        }
      }
    },
    "node_modules/react-router-dom": {
      "version": "7.18.1",
      "resolved": "https://registry.npmjs.org/react-router-dom/-/react-router-dom-7.18.1.tgz",
      "integrity": "sha512-KaZh+X/6UtEp28x51AUYZDMg9NGoz2ja3dNHa+ta/tk40vCzKhQ/RypCWBMLbmDr6//E24Vv5uPsrqXFozdkAg==",
      "license": "MIT",
      "dependencies": {
        "react-router": "7.18.1"
      },
      "engines": {
        "node": ">=20.0.0"
      },
      "peerDependencies": {
        "react": ">=18",
        "react-dom": ">=18"
      }
    },
    "node_modules/rolldown": {
      "version": "1.1.5",
      "resolved": "https://registry.npmjs.org/rolldown/-/rolldown-1.1.5.tgz",
      "integrity": "sha512-t9z29cJjXf/vxQ8dyhCSpt6H6aSwHTk8cT5I3iy6SMXuFpk5mB6PL6XfC8PCwrPTx93udwKUm9HRteAlTGBLiA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@oxc-project/types": "=0.139.0",
        "@rolldown/pluginutils": "^1.0.0"
      },
      "bin": {
        "rolldown": "bin/cli.mjs"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "optionalDependencies": {
        "@rolldown/binding-android-arm64": "1.1.5",
        "@rolldown/binding-darwin-arm64": "1.1.5",
        "@rolldown/binding-darwin-x64": "1.1.5",
        "@rolldown/binding-freebsd-x64": "1.1.5",
        "@rolldown/binding-linux-arm-gnueabihf": "1.1.5",
        "@rolldown/binding-linux-arm64-gnu": "1.1.5",
        "@rolldown/binding-linux-arm64-musl": "1.1.5",
        "@rolldown/binding-linux-ppc64-gnu": "1.1.5",
        "@rolldown/binding-linux-s390x-gnu": "1.1.5",
        "@rolldown/binding-linux-x64-gnu": "1.1.5",
        "@rolldown/binding-linux-x64-musl": "1.1.5",
        "@rolldown/binding-openharmony-arm64": "1.1.5",
        "@rolldown/binding-wasm32-wasi": "1.1.5",
        "@rolldown/binding-win32-arm64-msvc": "1.1.5",
        "@rolldown/binding-win32-x64-msvc": "1.1.5"
      }
    },
    "node_modules/scheduler": {
      "version": "0.27.0",
      "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.27.0.tgz",
      "integrity": "sha512-eNv+WrVbKu1f3vbYJT/xtiF5syA5HPIMtf9IgY/nKg0sWqzAUEvqY/xm7OcZc/qafLx/iO9FgOmeSAp4v5ti/Q==",
      "license": "MIT"
    },
    "node_modules/semver": {
      "version": "6.3.1",
      "resolved": "https://registry.npmjs.org/semver/-/semver-6.3.1.tgz",
      "integrity": "sha512-BR7VvDCVHO+q2xBEWskxS6DJE1qRnb7DxzUrogb71CWoSficBxYsiAGd+Kl0mmq/MprG9yArRkyrQxTO6XjMzA==",
      "dev": true,
      "license": "ISC",
      "bin": {
        "semver": "bin/semver.js"
      }
    },
    "node_modules/set-cookie-parser": {
      "version": "2.7.2",
      "resolved": "https://registry.npmjs.org/set-cookie-parser/-/set-cookie-parser-2.7.2.tgz",
      "integrity": "sha512-oeM1lpU/UvhTxw+g3cIfxXHyJRc/uidd3yK1P242gzHds0udQBYzs3y8j4gCCW+ZJ7ad0yctld8RYO+bdurlvw==",
      "license": "MIT"
    },
    "node_modules/shebang-command": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz",
      "integrity": "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "shebang-regex": "^3.0.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/shebang-regex": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz",
      "integrity": "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/source-map-js": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
      "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
      "dev": true,
      "license": "BSD-3-Clause",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/tinyglobby": {
      "version": "0.2.17",
      "resolved": "https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.17.tgz",
      "integrity": "sha512-wXR/dYpcqKmfWpEdZjiKJOwCNFndD0DMnrW/cYjVGttEkBfVgcLFHoNrlj47mjOVic9yyNu65alsgF4NQyTa2g==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "fdir": "^6.5.0",
        "picomatch": "^4.0.4"
      },
      "engines": {
        "node": ">=12.0.0"
      },
      "funding": {
        "url": "https://github.com/sponsors/SuperchupuDev"
      }
    },
    "node_modules/tslib": {
      "version": "2.8.1",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
      "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
      "dev": true,
      "license": "0BSD",
      "optional": true
    },
    "node_modules/type-check": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/type-check/-/type-check-0.4.0.tgz",
      "integrity": "sha512-XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "prelude-ls": "^1.2.1"
      },
      "engines": {
        "node": ">= 0.8.0"
      }
    },
    "node_modules/update-browserslist-db": {
      "version": "1.2.3",
      "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz",
      "integrity": "sha512-Js0m9cx+qOgDxo0eMiFGEueWztz+d4+M3rGlmKPT+T4IS/jP4ylw3Nwpu6cpTTP8R1MAC1kF4VbdLt3ARf209w==",
      "dev": true,
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "escalade": "^3.2.0",
        "picocolors": "^1.1.1"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/uri-js": {
      "version": "4.4.1",
      "resolved": "https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz",
      "integrity": "sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==",
      "dev": true,
      "license": "BSD-2-Clause",
      "dependencies": {
        "punycode": "^2.1.0"
      }
    },
    "node_modules/vite": {
      "version": "8.1.5",
      "resolved": "https://registry.npmjs.org/vite/-/vite-8.1.5.tgz",
      "integrity": "sha512-7ULLwsCdYx/nRyrpiEwvqb5TFHrMVZyBt+rg/OAXT7rgj/z+DtTDyKFeLAdDkubDVDKD8jOsndmy7m55XcfUsw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "lightningcss": "^1.32.0",
        "picomatch": "^4.0.5",
        "postcss": "^8.5.17",
        "rolldown": "~1.1.5",
        "tinyglobby": "^0.2.17"
      },
      "bin": {
        "vite": "bin/vite.js"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      },
      "funding": {
        "url": "https://github.com/vitejs/vite?sponsor=1"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.3"
      },
      "peerDependencies": {
        "@types/node": "^20.19.0 || >=22.12.0",
        "@vitejs/devtools": "^0.3.0",
        "esbuild": "^0.27.0 || ^0.28.0",
        "jiti": ">=1.21.0",
        "less": "^4.0.0",
        "sass": "^1.70.0",
        "sass-embedded": "^1.70.0",
        "stylus": ">=0.54.8",
        "sugarss": "^5.0.0",
        "terser": "^5.16.0",
        "tsx": "^4.8.1",
        "yaml": "^2.4.2"
      },
      "peerDependenciesMeta": {
        "@types/node": {
          "optional": true
        },
        "@vitejs/devtools": {
          "optional": true
        },
        "esbuild": {
          "optional": true
        },
        "jiti": {
          "optional": true
        },
        "less": {
          "optional": true
        },
        "sass": {
          "optional": true
        },
        "sass-embedded": {
          "optional": true
        },
        "stylus": {
          "optional": true
        },
        "sugarss": {
          "optional": true
        },
        "terser": {
          "optional": true
        },
        "tsx": {
          "optional": true
        },
        "yaml": {
          "optional": true
        }
      }
    },
    "node_modules/which": {
      "version": "2.0.2",
      "resolved": "https://registry.npmjs.org/which/-/which-2.0.2.tgz",
      "integrity": "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==",
      "dev": true,
      "license": "ISC",
      "dependencies": {
        "isexe": "^2.0.0"
      },
      "bin": {
        "node-which": "bin/node-which"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/word-wrap": {
      "version": "1.2.5",
      "resolved": "https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.5.tgz",
      "integrity": "sha512-BN22B5eaMMI9UMtjrGd5g5eCYPpCPDUy0FJXbYsaT5zYxjFOckS53SQDE3pWkVoWpHXVb3BrYcEN4Twa55B5cA==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=0.10.0"
      }
    },
    "node_modules/yallist": {
      "version": "3.1.1",
      "resolved": "https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz",
      "integrity": "sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==",
      "dev": true,
      "license": "ISC"
    },
    "node_modules/yocto-queue": {
      "version": "0.1.0",
      "resolved": "https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz",
      "integrity": "sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/zod": {
      "version": "4.4.3",
      "resolved": "https://registry.npmjs.org/zod/-/zod-4.4.3.tgz",
      "integrity": "sha512-ytENFjIJFl2UwYglde2jchW2Hwm4GJFLDiSXWdTrJQBIN9Fcyp7n4DhxJEiWNAJMV1/BqWfW/kkg71UDcHJyTQ==",
      "dev": true,
      "license": "MIT",
      "funding": {
        "url": "https://github.com/sponsors/colinhacks"
      }
    },
    "node_modules/zod-validation-error": {
      "version": "4.0.2",
      "resolved": "https://registry.npmjs.org/zod-validation-error/-/zod-validation-error-4.0.2.tgz",
      "integrity": "sha512-Q6/nZLe6jxuU80qb/4uJ4t5v2VEZ44lzQjPDhYJNztRQ4wyWc6VF3D3Kb/fAuPetZQnhS3hnajCf9CsWesghLQ==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=18.0.0"
      },
      "peerDependencies": {
        "zod": "^3.25.0 || ^4.0.0"
      }
    }
  }
}

```

### File: `frontend\package.json`
```json
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.19.0",
    "react": "^19.2.7",
    "react-dom": "^19.2.7",
    "react-router-dom": "^7.18.1"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@types/react": "^19.2.17",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^6.0.3",
    "eslint": "^10.6.0",
    "eslint-plugin-react-hooks": "^7.1.1",
    "eslint-plugin-react-refresh": "^0.5.3",
    "globals": "^17.7.0",
    "vite": "^8.1.1"
  }
}

```
