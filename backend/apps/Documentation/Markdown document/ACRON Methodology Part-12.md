# ACRON Methodology Part-12

<aside>
📢

در Part-11 ، **فاز 9:  MCP - Model Context Protocol  تمام پروژه به دو پوشه backend و frontend منتقل شد تا پتانسیل مغیاس پذیری مناسب تری برای بزرگ شدن پروژه داشته باشد.**

</aside>

# فاز **9:  MCP - Model Context Protocol**

---

Agent می‌تواند به سؤال‌هایی مثل این پاسخ بدهد:

- پروژه ACRON چیست؟
- معماری آن چگونه است؟
- چه قابلیت‌هایی دارد؟
- توسعه‌دهنده پروژه چه تخصص‌هایی دارد؟
- وضعیت پروژه چیست؟
- چگونه می‌توان مشارکت کرد؟
- چگونه می‌توان قرارداد بست؟
- این پروژه چه تفاوتی با پروژه‌های دیگر دارد؟
- وضعیت سفارش چیست؟ (در آینده)
- وضعیت مرسوله چیست؟ (در آینده)
- چه APIهایی وجود دارد؟ (در آینده)

## قدم اول: ساخت ساختار اپلیکیشن `advisor`

> 1- ابتدا باید ساختار فولدرها را در پروژه ایجاد کنیم. در ترمینال خود (در محیط مجازی فعال پروژه) دستور زیر را اجرا کن: 
دقت کن که داخل فولدر backend باشی
> 
> 
> ```python
> python manage.py startapp advisor apps/advisor
> ```
> 

پس از اجرای این دستور، پوشه `apps/advisor/` ساخته می‌شود. حالا باید جنگو را متوجه حضور این اپلیکیشن کنیم.

**چرا؟** جنگو برای اینکه بتواند مدل‌های این اپلیکیشن را در دیتابیس بسازد و مسیرهای آن را بشناسد، باید نام آن را در لیست `INSTALLED_APPS` ببیند. از آنجا که ما از ساختار ماژولار استفاده می‌کنیم و اپ‌ها داخل پوشه `apps` هستند، نام آن را به صورت `'apps.advisor'` وارد می‌کنیم.

> 2- فایل `apps/advisor/apps.py` را باز کن و مطمئن شو که کلاس تنظیمات به این صورت تعریف شده است:
> 
> 
> ```python
> # apps/advisor/apps.py
> 
> from django.apps import AppConfig
> 
> class AdvisorConfig(AppConfig):
>     default_auto_field = 'django.db.models.BigAutoField'
>     name = 'apps.advisor' # حتماً باید پیشوند apps داشته باشد تا با ساختار پروژه همخوانی داشته باشد
> ```
> 

> 3-  حالا فایل تنظیمات پایه یعنی `config/settings/base.py` را باز کن و اپلیکیشن جدیدمان را در `INSTALLED_APPS` ثبت کن:
> 
> 
> ```python
> # config/settings/base.py
> 
> INSTALLED_APPS = [
>     # ... اپلیکیشن‌های قبلی جنگو و پکیج‌ها ...
>     
>     # اپلیکیشن‌های اختصاصی پروژه ACRON
>     'apps.accounts',
>     'apps.customers',
>     'apps.products',
>     'apps.carts',
>     'apps.orders',
>     'apps.payments',
>     'apps.shipments',
>     'apps.ai',
>     'apps.advisor', # اضافه کردن اپلیکیشن جدید مشاور هوشمند
> ]
> ```
> 

#### قدم دوم: طراحی مدل‌های دیتابیس (`models.py`)

برای اینکه این سیستم کاملاً تجاری و واقعی باشد، ما نباید فقط یک ورودی بگیریم و جواب بدهیم و تمام! ما نیاز داریم گفتگوها را ذخیره کنیم تا:

1. کارفرماها بتوانند یک نشست گفتگو (Session) داشته باشند و سوالات متوالی بپرسند (حفظ Context گفتگو).
2. تو به عنوان صاحب پروژه بتوانی در پنل ادمین ببینی چه کسانی با مشاور تو چت کرده‌اند و علایق کارفرماها چیست.

برای این کار دو مدل طراحی می‌کنیم:

1. `Conversation`: نماینده یک جلسه گفتگوی یکتا بین یک کاربر/کارفرما و مشاور هوشمند.
2. `Message`: نماینده هر پیام رد و بدل شده (پیام کاربر و پاسخ هوش مصنوعی).

> 4-  فایل `apps/advisor/models.py` را باز کن و کدهای زیر را بنویس.
> 
> 
> ```python
> # apps/advisor/models.py
> 
> from django.db import models
> from django.conf import settings
> import uuid
> 
> class Conversation(models.Model):
>     """
>     هر نمونه از این کلاس، نشان‌دهنده یک جلسه چت (Chat Session) است.
>     کاربران (حتی بدون لاگین یا با لاگین) می‌توانند یک چت جدید شروع کنند.
>     برای امنیت و غیرقابل حدس بودن جلسات چت، کلید اصلی را UUID قرار می‌دهیم.
>     """
>     # استفاده از UUID به جای کلید عددی (ID) برای جلوگیری از دسترسی غیرمجاز دیگران به تاریخچه چت‌ها
>     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
>     
>     # اگر کاربر لاگین کرده باشد، او را به این گفتگو متصل می‌کنیم. اگر مهمان باشد، Null می‌ماند.
>     user = models.ForeignKey(
>         settings.AUTH_USER_MODEL,
>         on_delete=models.SET_NULL,
>         null=True,
>         blank=True,
>         related_name='advisor_conversations',
>         verbose_name="کاربر"
>     )
>     
>     # ذخیره آی‌پی یا یک کلید شناسایی فرانت‌اند برای تحلیل بهتر رفتار کاربران غیرلاگین
>     visitor_session_key = models.CharField(
>         max_length=255, 
>         null=True, 
>         blank=True, 
>         verbose_name="کلید نشست بازدیدکننده"
>     )
>     
>     created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ شروع گفتگو")
>     updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین فعالیت")
> 
>     class Meta:
>         ordering = ['-updated_at']
>         verbose_name = "گفتگوی مشاور"
>         verbose_name_plural = "گفتگوهای مشاور"
> 
>     def __str__(self):
>         user_str = self.user.username if self.user else f"مهمان ({self.id.hex[:8]})"
>         return f"گفتگو با {user_str} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
> 
> class Message(models.Model):
>     """
>     هر سطر از این جدول، یک پیام (یا سوال از طرف کاربر یا پاسخ از طرف هوش مصنوعی) را ذخیره می‌کند.
>     """
>     ROLE_CHOICES = [
>         ('user', 'کاربر'),
>         ('assistant', 'دستیار هوش مصنوعی'),
>     ]
> 
>     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
>     
>     # اتصال پیام به گفتگوی مربوطه؛ اگر گفتگو پاک شود، تمام پیام‌های آن نیز پاک خواهند شد (CASCADE)
>     conversation = models.ForeignKey(
>         Conversation,
>         on_delete=models.CASCADE,
>         related_name='messages',
>         verbose_name="گفتگو"
>     )
>     
>     # نقش ارسال‌کننده پیام (آیا کاربر سوال پرسیده یا هوش مصنوعی پاسخ داده؟)
>     role = models.CharField(
>         max_length=10,
>         choices=ROLE_CHOICES,
>         verbose_name="نقش ارسال‌کننده"
>     )
>     
>     # متن اصلی پیام
>     content = models.TextField(verbose_name="محتوای پیام")
>     
>     # تحلیل لحن پیام کاربر (مثلاً فنی، عامیانه، رسمی، بیزینسی) که توسط لایه سرویس تشخیص داده شده است
>     detected_tone = models.CharField(
>         max_length=50,
>         null=True,
>         blank=True,
>         verbose_name="لحن شناسایی‌شده"
>     )
>     
>     created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال")
> 
>     class Meta:
>         ordering = ['created_at'] # پیام‌ها باید به ترتیب زمان ارسال نمایش داده شوند تا رشته گفتگو درست بماند
>         verbose_name = "پیام"
>         verbose_name_plural = "پیام‌ها"
> 
>     def __str__(self):
>         return f"{self.get_role_display()}: {self.content[:50]}..."
> ```
> 

**چرا این ساختار دیتابیس؟ (تحلیل معماری)**
ما از الگوی رایج چت‌بات‌های پیشرفته استفاده کردیم. تفکیک گفتگو (`Conversation`) از پیام‌ها (`Message`) به ما اجازه می‌دهد که یک سیستم چت چندمرحله‌ای بسازیم. این کار جلوی فرستادن کل تاریخچه در قالب یک پیام طولانی و بی‌ساختار از سمت کلاینت را می‌گیرد. جنگو با استفاده از رابطه `ForeignKey` بین این دو مدل، مدیریت زنجیره چت را به عهده می‌گیرد.

> 5- حالا دستورات ساخت و اعمال مهاجرت‌ها (Migrations) را در ترمینال بزن تا جداول در دیتابیس MySQL ساخته شوند:
> 
> 
> ```python
> python manage.py makemigrations advisor
> python manage.py migrate
> ```
> 

خروجی شبیه زیر خواهد بود:

```jsx
$python manage.py makemigrations advisor
Migrations for 'advisor':
  apps\advisor\migrations\0001_initial.py
    + Create model Conversation
    + Create model Message

$python manage.py migrate advisor
Operations to perform:
  Apply all migrations: advisor
Running migrations:
  Applying advisor.0001_initial... OK

```

قدم سوم: طراحی ادمین برای مدیریت و مانیتورینگ گفتگوها (`admin.py`)

به عنوان یک توسعه‌دهنده، باید همیشه ابزار مانیتورینگ مناسب در پنل مدیریت جنگو (Django Admin) داشته باشی تا بتوانی بدون نیاز به کوئری زدن مستقیم به دیتابیس، وضعیت چت‌ها را تحلیل کنی.

> 6- فایل `apps/advisor/admin.py` را باز کن و کدهای زیر را قرار بده:
> 
> 
> ```python
> # apps/advisor/admin.py
> 
> from django.contrib import admin
> from .models import Conversation, Message
> 
> class MessageInline(admin.TabularInline):
>     """
>     این کلاس به ما اجازه می‌دهد که پیام‌های هر گفتگو را به صورت مستقیم 
>     و در داخل صفحه همان گفتگو در پنل ادمین مشاهده کنیم (Inline).
>     """
>     model = Message
>     extra = 0 # تعداد ردیف‌های خالی اضافی برای ایجاد پیام جدید را صفر می‌گذاریم
>     readonly_fields = ['role', 'content', 'detected_tone', 'created_at']
>     can_delete = False # برای حفظ تاریخچه‌ها، امکان حذف دستی پیام‌ها از داخل ادمین گفتگو را می‌بندیم
> 
> @admin.register(Conversation)
> class ConversationAdmin(admin.ModelAdmin):
>     """
>     تنظیمات مدیریت گفتگوها در پنل ادمین.
>     """
>     list_display = ['id', 'get_user_or_guest', 'created_at', 'updated_at']
>     list_filter = ['created_at', 'updated_at']
>     search_fields = ['user__username', 'visitor_session_key']
>     inlines = [MessageInline] # نمایش پیام‌های مرتبط در پایین صفحه گفتگو
> 
>     def get_user_or_guest(self, obj):
>         if obj.user:
>             return obj.user.username
>         return f"مهمان ({obj.visitor_session_key or 'نامشخص'})"
>     get_user_or_guest.short_description = "کاربر / مهمان"
> 
> @admin.register(Message)
> class MessageAdmin(admin.ModelAdmin):
>     """
>     تنظیمات مدیریت تک پیام‌ها در پنل ادمین.
>     """
>     list_display = ['id', 'conversation_link', 'role', 'short_content', 'detected_tone', 'created_at']
>     list_filter = ['role', 'detected_tone', 'created_at']
>     search_fields = ['content', 'conversation__id']
>     readonly_fields = ['created_at']
> 
>     def short_content(self, obj):
>         return obj.content[:75] + "..." if len(obj.content) > 75 else obj.content
>     short_content.short_description = "خلاصه متن"
> 
>     def conversation_link(self, obj):
>         # ایجاد یک لینک مستقیم به گفتگوی مادر در پنل ادمین
>         from django.urls import reverse
>         from django.utils.html import format_html
>         link = reverse("admin:advisor_conversation_change", args=[obj.conversation.id])
>         return format_html('<a href="{}">مشاهده گفتگو ({})</a>', link, obj.conversation.id.hex[:8])
>     conversation_link.short_description = "لینک گفتگو"
> ```
> 

قدم چهارم: قلب سیستم هوشمند؛ لایه سرویس (`services.py`)

<aside>
📢

### برای دوری از Vibe Coding، ما تمام کارهای مربوط به فراخوانی مدل زبان (LLM)، تزریق کانتکست‌های رزومه (سینا لاله بخش)و معماری ACRON، و تحلیل لحن کاربر را در یک **لایه سرویس (Service Layer)** مجزا می‌نویسیم.

</aside>

**چرا؟ (Why):** در معماری تمیز (Clean Architecture)، کنترلر یا View جنگو نباید مستقیماً با کلاینت‌های خارجی (مثل کتابخانه‌های API هوش مصنوعی) سر و کله بزند. ویو فقط ورودی را می‌گیرد، به سرویس می‌دهد و خروجی را بازمی‌گرداند. این کار باعث می‌شود کدهای ما قابلیت تست‌نویسی بسیار بالا (Testability) داشته باشند و اگر فردا خواستیم ارائه‌دهنده سرویس هوش مصنوعی را عوض کنیم، نیازی به تغییر کدهای بخش API و سریالایزر نباشد.

> 7- بیایید فایلی به نام `services.py` در پوشه `apps/advisor/` بسازیم.
> 

ما کانتکست سیستم (System Prompt) را به گونه‌ای طراحی می‌کنیم که شامل اطلاعات رزومه‌ات (از PDF و PPTX) و اطلاعات پروژه ACRON (از فایل‌های مستندات پروژه) باشد. همچنین به هوش مصنوعی دستور می‌دهیم که لحن سوال کاربر را شناسایی کند، به زبان و ادبیات خودش پاسخ دهد و آن لحن را در فیلد مجزایی برگرداند.

برای اینکه کد ما بدون نیاز به کلیدهای API گران‌قیمت یا پیچیده کار کند، یک شبیه‌ساز سرویس هوش مصنوعی هوشمند (Mock/Real LLM Service) می‌نویسیم که ساختار پرامپت‌نویسی بسیار پیشرفته‌ای دارد. در دنیای واقعی، تو می‌توانی از SDK رسمی `google-generativeai` یا هر کلاینت دیگری استفاده کنی. در اینجا من نحوه مدیریت پرامپت سیستم و چگونگی کوئری زدن را پیاده‌سازی می‌کنم تا مفهوم معماری را عمیقاً درک کنی.

> 8- داخل فایل [services.py](http://services.py) در apps/advisor این کد را بنویس:
این قطعه کد به دلیل حجم زیاد داخل Notion اجازه ساخت کد باز که بشود کپی کنید وجود ندارد. اصل فایل را دانلود کنید. سپس در مسیر replace کنید.
> 
> 
> [services.py](services.py)
> 

قدم پنجم: طراحی سریالایزرها (`serializers.py`)

برای اینکه داده‌های ورودی کلاینت را اعتبارسنجی کنیم و داده‌های خروجی را به فرمت استاندارد JSON تبدیل کنیم، نیاز به Serializer داریم.

**چرا؟ (Why):** جنگو داده‌های دیتابیس را به صورت آبجکت پایتونی نگه می‌دارد. مرورگر یا اپلیکیشن‌های موبایل نمی‌توانند آبجکت پایتون را بفهمند؛ آن‌ها نیاز به فرمت استاندارد JSON دارند. سریالایزر وظیفه تبدیل این آبجکت‌ها به JSON (Serialization) و برعکس، یعنی تبدیل ورودی کاربر به داده معتبر پایتون (Deserialization) را بر عهده دارد.

> 9- فایل جدیدی به نام `serializers.py` در مسیر `apps/advisor/` بساز و کدهای زیر را در آن قرار بده:
> 

> 10- در فایل serializers این کد را بنویس:
> 
> 
> ```python
> # apps/advisor/serializers.py
> 
> from rest_framework import serializers
> from .models import Conversation, Message
> 
> class MessageSerializer(serializers.ModelSerializer):
>     """
>     سریالایزر برای نمایش پیام‌های داخل یک گفتگو.
>     """
>     role_display = serializers.CharField(source='get_role_display', read_only=True)
> 
>     class Meta:
>         model = Message
>         fields = [
>             'id',
>             'role',
>             'role_display',
>             'content',
>             'detected_tone',
>             'created_at'
>         ]
>         read_only_fields = ['id', 'role_display', 'detected_tone', 'created_at']
> 
> class ConversationSerializer(serializers.ModelSerializer):
>     """
>     سریالایزر برای ساخت گفتگو و واکشی اطلاعات کلی آن.
>     """
>     # نمایش پیام‌های مرتبط با گفتگو به صورت Nested (تو در تو)
>     messages = MessageSerializer(many=True, read_only=True)
>     user_username = serializers.CharField(source='user.username', read_only=True)
> 
>     class Meta:
>         model = Conversation
>         fields = [
>             'id',
>             'user',
>             'user_username',
>             'visitor_session_key',
>             'messages',
>             'created_at',
>             'updated_at'
>         ]
>         read_only_fields = ['id', 'user', 'user_username', 'created_at', 'updated_at']
> 
> class AskAdvisorInputSerializer(serializers.Serializer):
>     """
>     سریالایزر اختصاصی برای دریافت ورودی سوال کاربر.
>     این کلاس به صورت مستقیم به مدل وصل نیست و فقط وظیفه ولیدیشن ورودی خام API را دارد.
>     """
>     question = serializers.CharField(
>         required=True, 
>         min_length=3, 
>         error_messages={
>             'required': 'لطفاً سوال خود را بفرستید.',
>             'min_length': 'سوال شما باید حداقل ۳ کاراکتر باشد.'
>         }
>     )
> ```
> 

قدم ششم: طراحی کنترلر و ویوها (`views.py`)

حالا نوبت به لایه کنترلر یا همان API Views می‌رسد. ما دو کار اصلی را در API خود پیاده‌سازی می‌کنیم:

1. **ساخت گفتگو جدید یا بازخوانی گفتگوهای قبلی** (با استفاده از `ModelViewSet` در DRF).
2. **ارسال سوال به مشاور هوشمند** روی یک چت خاص (با تعریف یک `action` اختصاصی روی ViewSet).

> 11- فایل `apps/advisor/views.py` را باز کن و کدهای زیر را بنویس:
> 
> 
> ```python
> # apps/advisor/views.py
> 
> from rest_framework import viewsets, status
> from rest_framework.decorators import action
> from rest_framework.response import Response
> from rest_framework.permissions import AllowAny
> from drf_spectacular.utils import extend_schema, OpenApiResponse
> 
> from .models import Conversation
> from .serializers import ConversationSerializer, AskAdvisorInputSerializer, MessageSerializer
> from .services import AdvisorAIService
> 
> class AdvisorViewSet(viewsets.ModelViewSet):
>     """
>     مجموعه وب‌سرویس‌های مدیریت گفتگو و ارتباط با مشاور هوشمند پروژه ACRON و سینا لاله بخش.
>     این مسیر نیاز به لاگین اجباری ندارد تا همه کارفرمایان بتوانند به راحتی با مشاور چت کنند.
>     """
>     permission_classes = [AllowAny]
>     queryset = Conversation.objects.prefetch_related('messages').all()
>     serializer_class = ConversationSerializer
>     
>     # برای امنیت، متدهای ویرایش و حذف کلی گفتگوها را در سطح عمومی API غیرفعال می‌کنیم
>     http_method_names = ['get', 'post', 'delete']
> 
>     def perform_create(self, serializer):
>         """
>         هنگام ایجاد یک گفتگوی جدید، اگر کاربر لاگین کرده باشد، او را ثبت می‌کنیم.
>         همچنین آی‌پی یا سشن بازدیدکننده را نیز برای بررسی‌های بعدی ذخیره می‌کنیم.
>         """
>         user = self.request.user if self.request.user.is_authenticated else None
>         
>         # گرفتن آی‌پی ساده کاربر به عنوان کلید سشن مهمان
>         x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
>         if x_forwarded_for:
>             ip = x_forwarded_for.split(',')[0]
>         else:
>             ip = self.request.META.get('REMOTE_ADDR')
>             
>         serializer.save(user=user, visitor_session_key=ip)
> 
>     @extend_schema(
>         summary="ارسال سوال به مشاور هوشمند پروژه",
>         description="با ارسال شناسه گفتگو و سوال خود، پاسخ هوشمند و متقاعدکننده منطبق با لحن خود را دریافت کنید.",
>         request=AskAdvisorInputSerializer,
>         responses={
>             200: OpenApiResponse(response=MessageSerializer, description="پاسخ هوش مصنوعی تولید و ذخیره شد."),
>             400: OpenApiResponse(description="ورودی نامعتبر است.")
>         }
>     )
>     @action(detail=True, methods=['post'], url_path='ask')
>     def ask(self, request, pk=None):
>         """
>         مسیر اختصاصی: POST /api/advisor/{conversation_uuid}/ask/
>         این متد سوال کاربر را دریافت کرده، به لایه سرویس منتقل می‌کند و پاسخ هوشمند را برمی‌گرداند.
>         """
>         # ۱. لود کردن گفتگوی مربوطه از دیتابیس
>         conversation = self.get_object()
>         
>         # ۲. بررسی و اعتبارسنجی ورودی سوال با سریالایزر اختصاصی
>         input_serializer = AskAdvisorInputSerializer(data=request.data)
>         if not input_serializer.is_valid():
>             return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>             
>         user_question = input_serializer.validated_data['question']
>         
>         # ۳. فراخوانی لایه سرویس برای ارتباط با مدل زبانی و ذخیره‌سازی پیام‌ها
>         ai_response_message = AdvisorAIService.generate_response(
>             conversation_id=conversation.id,
>             user_message_content=user_question
>         )
>         
>         # ۴. سریالایز کردن پاسخ نهایی هوش مصنوعی برای ارسال به کلاینت
>         output_serializer = MessageSerializer(ai_response_message)
>         return Response(output_serializer.data, status=status.HTTP_200_OK)
> ```
> 

قدم هفتم: مسیریابی و ثبت آدرس‌ها (`urls.py`)

حالا باید آدرس‌های این اپلیکیشن جدید را تعریف کرده و به آدرس‌دهی کل پروژه (Root URLconf) متصل کنیم.

> 12- فایل جدیدی به نام `urls.py` در مسیر `apps/advisor/` بساز و کدهای زیر را وارد کن:
> 
> 
> ```python
> # apps/advisor/urls.py
> 
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import AdvisorViewSet
> 
> # استفاده از DefaultRouter برای ساخت خودکار مسیرهای استاندارد RESTful
> router = DefaultRouter()
> router.register(r'advisor', AdvisorViewSet, basename='advisor')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

> 13- حالا فایل مسیریابی کل APIهای پروژه یعنی `apps/api/urls.py` را باز کن و مسیرهای اپلیکیشن `advisor` را به آن اضافه کن:
> 
> 
> ```python
> # apps/api/urls.py
> 
> from django.urls import include, path
> 
> urlpatterns = [
>     # ... مسیرهای قبلی پروژه ...
>     path('accounts/', include('apps.accounts.urls')),
>     path('customers/', include('apps.customers.urls')),
>     path('products/', include('apps.products.urls')),
>     path('carts/', include('apps.carts.urls')),
>     path('orders/', include('apps.orders.urls')),
>     path('payments/', include('apps.payments.urls')),
>     
>     # اضافه کردن مسیرهای مشاور هوشمند جدید
>     path('', include('apps.advisor.urls')),
> ]
> ```
> 

چرخه‌ی کامل تست و اجرای قدم به قدم پروژه (چگونه تست کنیم؟)

1- اجرای سرور:

```python
python manage.py runserver
```

**2- باز کردن مستندات Swagger:**

مرورگر خود را باز کن و به آدرس زیر برو:

`http://127.0.0.1:8000/api/schema/swagger-ui/`
حالا باید بخش جدید مربوط به وب‌سرویس‌های `advisor` را در آنجا ببینی!

3- **ساختن گفتگو (Chat Session):**

- در Swagger متد `POST /api/advisor/` را پیدا کن.
- بدنه درخواست (Request Body) را خالی بگذار و روی **Execute** بزن.
- **نتیجه:** یک پاسخ با وضعیت `201 Created` می‌گیری که شامل یک شناسه طولانی منحصر به فرد (`id`) مثل `3fa85f64-5717-4562-b3fc-2c963f66afa6` است. این شناسه گفتگو (Conversation ID) را کپی کن.

4- **پرسیدن سوال با لحن رسمی (کارفرما):**

- متد `POST /api/advisor/{id}/ask/` را باز کن.
- در بخش پارامترها، شناسه‌ای که کپی کردی را در بخش `id` قرار بده.
- در بخش بدنه درخواست، سوالی کاملاً رسمی بنویس:

```python
{
  "question": "با سلام، لطفا بفرمایید آقای سینا لاله بخش چه تخصص‌های کلیدی در حوزه بهینه‌سازی دیتابیس جنگو دارند و شرایط همکاری با ایشان چگونه است؟"
}
```

- دکمه **Execute** را بزن.
- **نتیجه جادویی:** هوش مصنوعی لحن شما را **Business / Formal** تشخیص می‌دهد و پاسخی کاملاً محترمانه، رسمی و شرکتی که متقاعدکننده است بازمی‌گرداند.

**5- پرسیدن سوال با لحن دوستانه و عامیانه (یک رفیق یا یوتیوبر):**

- با همان `id` گفتگو، سوال دیگری بفرست:

```jsx
{
  "question": "سلام داداش، دمت گرم. این سینا لاله بخش که میگن کیه؟ کارش چطوریه؟ خیلی کارش درسته؟"
}
```

- دکمه **Execute** را بزن.
- **نتیجه جادویی:** سیستم متوجه صمیمیت سوال می‌شود، لحن را به **Friendly / Informal** تغییر می‌دهد و با همان ادبیات صمیمی و پرانرژی پاسخ می‌دهد تا کارفرما احساس راحتی کامل کند.

6- **پرسیدن سوال کاملاً فنی (یک مهندس نرم‌افزار):**

- یک سوال فنی ارسال کن:

```jsx
{
  "question": "پروژه ACRON چطور کار می‌کنه؟ نحوه استفاده از UUID در سبد خرید و معماری لایه پرداخت اونو برام توضیح بده."
}
```

- دکمه **Execute** را بزن.
- **نتیجه جادویی:** پاسخ با رویکرد عمیق مهندسی ارائه شده و نحوه ساختاردهی دامنه‌های پروژه را با تکیه بر متدولوژی ACRON شرح می‌دهد.

7- **بررسی در پنل ادمین:**
به آدرس `http://127.0.0.1:8000/admin/` برو. بخش **Advisor Conversations** و **Messages** را باز کن. تمام این گفتگوها، پیام‌های رد و بدل شده، لحن شناسایی شده و جزییات بازدیدکننده به زیبایی در آنجا مانیتور می‌شوند.

### خلاصه مفاهیم آموزشی این فاز (جهت یادگیری عمیق شما)

به عنوان یک دانشجو با ذهنیت ارشد (Senior Mindset)، بیایید مفاهیم حیاتی که در این فاز یاد گرفتیم را مرور کنیم:

- **مزیت UUID بر Integer:** اگر از شناسه عددی استفاده می‌کردیم، کارفرماها می‌توانستند با تغییر شناسه گفتگو در آدرس بار، چت‌های دیگران را بخوانند. استفاده از `uuid4` امنیت حریم خصوصی گفتگوها را تضمین می‌کند.
- **مزیت Separation of Concerns (تفکیک وظایف):** ما کدهای مربوط به هوش مصنوعی و ساخت پرامپت‌ها را در فایل `services.py` نوشتیم. این کار باعث شد که لایه View ما سبک بماند و فقط وظیفه هدایت ترافیک شبکه را به عهده داشته باشد. این الگو به نگهداری آسان‌تر پروژه‌های بزرگ کمک شایانی می‌کند.
- **مزیت Nested Serializer:** ما با قرار دادن `MessageSerializer` به صورت لیست در داخل `ConversationSerializer` توانستیم کل سابقه گفتگو را به صورت ساختاریافته در یک درخواست GET خروجی بگیریم.

<aside>
📢

# پایان Part-12

</aside>