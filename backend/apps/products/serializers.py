from rest_framework import serializers

from . import models

# ۱. سریالایزر دسته‌بندی
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'slug']

# ۲. سریالایزر برند
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ['id', 'name', 'slug', 'image']

# ۳. سریالایزر گالری مدیا
class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductMedia
        fields = ['id', 'media_type', 'file']

# ۴. سریالایزر اصلی محصول (Master Serializer)
class ProductSerializer(serializers.ModelSerializer):
    # الف) Nested Serializers برای فیلدهای کلید خارجی (ForeignKey)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    
    # ب) Nested Serializer برای رابطه معکوس (گالری)
    media_gallery = ProductMediaSerializer(many=True, read_only=True)
 
    class Meta:
        model = models.Product
        fields = [
            'id', 
            'name', 
            'slug', 
            'description', 
            'price', 
            'inventory', 
            'main_image',
            'category', 
            'brand', 
            'media_gallery', # اضافه کردن گالری به خروجی نهایی
            'created_at'
        ]



