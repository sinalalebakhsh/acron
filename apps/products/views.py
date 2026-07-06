from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Product
from .serializers import ProductSerializer

# تعریف 
# Swagger
#  فقط یک‌بار در بالای 
# ViewSet
@extend_schema_view(
    list=extend_schema(
        summary="دریافت لیست محصولات",
        description="لیست تمامی محصولات به همراه برند، دسته‌بندی و گالری تصاویر.",
        tags=['Products Catalog'],
    ),
    retrieve=extend_schema(
        summary="دریافت جزئیات محصول",
        description="اطلاعات کامل یک محصول بر اساس Slug.",
        tags=['Products Catalog'],
    )
)
class ProductViewSet(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    
    queryset = Product.objects.select_related(
        'category', 
        'brand'
    ).prefetch_related(
        'media_gallery'
    ).all()



    