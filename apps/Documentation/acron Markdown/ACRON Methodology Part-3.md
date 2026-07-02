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