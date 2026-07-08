from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import AllowAny


from .models import Cart, CartItem

from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer

@extend_schema_view(
    create=extend_schema(summary="ساخت سبد خرید جدید", tags=['Carts']),
    retrieve=extend_schema(summary="دریافت محتویات سبد خرید", tags=['Carts']),
    destroy=extend_schema(summary="حذف کامل سبد خرید", tags=['Carts']),
)
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    """
    ویو برای مدیریت خودِ سبد خرید (بدون آیتم‌ها).
    توجه: متد List حذف شده است زیرا هیچ کاربری نباید لیست سبد خرید دیگران را ببیند.
    """
    # این خط را اضافه کنید تا قفل شکسته شود
    permission_classes = [AllowAny]
    
    
    # بهینه‌سازی کوئری دیتابیس برای جلوگیری از مشکل N+1 در دریافت آیتم‌های سبد
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer


@extend_schema_view(
    create=extend_schema(summary="افزودن محصول به سبد خرید", tags=['Cart Items']),
    partial_update=extend_schema(summary="تغییر تعداد یک محصول در سبد", tags=['Cart Items']),
    destroy=extend_schema(summary="حذف یک محصول از سبد خرید", tags=['Cart Items']),
)
class CartItemViewSet(ModelViewSet):
    """
    ویو برای مدیریت آیتم‌های داخل سبد خرید.
    """
    # این خط را اضافه کنید تا قفل شکسته شود
    permission_classes = [AllowAny]


    # جلوگیری از استفاده از متد PUT (ما فقط به PATCH برای تغییر تعداد نیاز داریم)
    http_method_names = ['post', 'patch', 'delete']
    
    queryset = CartItem.objects.select_related('product').all()

    # جادوی DRF: انتخاب سریالایزر به صورت دینامیک بر اساس نوع درخواست (Method)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        
        return CartItemSerializer




