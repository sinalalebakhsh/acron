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





