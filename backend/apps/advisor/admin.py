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

