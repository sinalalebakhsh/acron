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


