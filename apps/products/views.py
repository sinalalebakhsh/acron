from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


from . import models
from . import serializers  

from drf_spectacular.utils import extend_schema, extend_schema_view # این خط اضافه شد


# استفاده از دکوراتور برای شخصی‌سازی مستندات این View
@extend_schema_view(
    get=extend_schema(
        summary="دریافت لیست محصولات فروشگاه",
        description="این متد لیست تمامی محصولات را به همراه اطلاعات برند، دسته‌بندی و گالری تصاویر برمی‌گرداند. این مسیر کاملاً بهینه‌سازی شده (بدون مشکل N+1) است و نیازی به توکن احراز هویت ندارد.",
        tags=['Products Catalog'], # دسته‌بندی API در سایدبار Swagger
    )
)
class ProductListView(ListAPIView):
    """
    API
    دریافت لیست تمام محصولات فروشگاه
    آزاد برای تمام کاربران (بدون نیاز به لاگین)
    """
    permission_classes = [AllowAny] # همه می‌توانند محصولات را ببینند
    serializer_class = serializers.ProductSerializer
    
    # QuerySet
    # کاملاً بهینه‌سازی شده برای جلوگیری از مشکل 
    # N+1
    queryset = models.Product.objects.select_related(
        'category', 
        'brand'
    ).prefetch_related(
        'media_gallery'
    ).all()



