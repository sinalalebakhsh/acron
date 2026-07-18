# apps/orders/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer, OrderCreateInputSerializer
from .services import OrderService

class OrderViewSet(viewsets.ModelViewSet):
    """
    کنترلر (View) مدیریت سفارشات.
    با رعایت معماری تمیز، این ویو فاقد هرگونه منطق تجاری سنگین دیتابیسی است.
    """
    permission_classes = [IsAuthenticated] # فقط کاربران لاگین شده به سفارشات دسترسی دارند
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        برگرداندن لیست سفارشات متعلق به خود کاربر لاگین شده به ترتیب جدیدترین‌ها.
        """
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

    def create(self, request, *args, **kwargs):
        """
        اکشن ساخت سفارش (POST /api/orders/)
        """
        # ۱. اعتبارسنجی ورودی‌های خام (شناسه سبد خرید و آدرس ارسال) با استفاده از سریالایزر اختصاصی ورودی
        input_serializer = OrderCreateInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        
        # استخراج داده‌های تایید شده از سریالایزر
        cart_id = input_serializer.validated_data['cart_id']
        shipping_address = input_serializer.validated_data['shipping_address']

        # ۲. ارجاع کار به لایه سرویس (قلب تپنده منطق تجاری)
        # تمام فرآیندهای سنگین اتمیک، کسر انبار و فریز قیمت در اینجا و خارج از دید کنترلر رخ می‌دهد.
        order = OrderService.place_order(
            user=request.user,
            cart_id=cart_id,
            shipping_address=shipping_address
        )

        # ۳. آماده‌سازی خروجی استاندارد JSON با استفاده از سریالایزر اصلی سفارش
        output_serializer = self.get_serializer(order)
        
        # برگرداندن پاسخ نهایی با وضعیت 201 Created به کلاینت
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


