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