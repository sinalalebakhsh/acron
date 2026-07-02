from django.db import models


class Category(models.Model):
    # دسته‌بندی والد (برای ساختار درختی)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name='children'
    )
    
    name = models.CharField(max_length=255)
    
    # اسلاگ برای 
    # URL
    # های سئو-محور
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    
    description = models.TextField(blank=True)
    
    # تصویر دسته‌بندی
    image = models.ImageField(upload_to='categories/%Y/%m/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='brands/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.name


      
        
