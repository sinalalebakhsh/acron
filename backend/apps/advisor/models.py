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



        