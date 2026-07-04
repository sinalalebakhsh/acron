from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from .models import Product

from .import serializers  

class ProductListView(ListAPIView):
    """
    API دریافت لیست تمام محصولات فروشگاه
    آزاد برای تمام کاربران (بدون نیاز به لاگین)
    """
    permission_classes = [AllowAny] # همه می‌توانند محصولات را ببینند
    serializer_class = ProductSerializer
    
    # QuerySet کاملاً بهینه‌سازی شده برای جلوگیری از مشکل N+1
    queryset = Product.objects.select_related(
        'category', 
        'brand'
    ).prefetch_related(
        'media_gallery'
    ).all()



