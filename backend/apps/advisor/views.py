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
    




