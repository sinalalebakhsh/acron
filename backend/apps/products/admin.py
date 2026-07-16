from django.contrib import admin

from .models import Category, Brand, Product, ProductMedia # مدل‌های جدید اضافه شدند


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # ۱. مشخص کردن ستون‌هایی که در لیست ادمین نمایش داده می‌شوند
    list_display = ['name', 'slug', 'parent']

    # ۲. جادوی پر شدن خودکار اسلاگ بر اساس نام
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



# ۱. ساخت کلاس اینلاین برای گالری فرعی
class ProductMediaInline(admin.TabularInline):
    model = ProductMedia
    extra = 1          # تعداد ردیف‌های خالی که به صورت پیش‌فرض نمایش داده می‌شود
    max_num = 10       # قفل کردن فرانت‌اند ادمین روی حداکثر ۱۰ فایل فرعی


# ۲. ساخت کلاس مدیریت اصلی محصول
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # الف) ستون‌های نمایشی در جدول لیست محصولات
    list_display = ['name', 'brand', 'category', 'price', 'inventory', 'created_at']
    
    # ب) باکس فیلتر در سمت راست پنل ادمین
    list_filter = ['category', 'brand', 'created_at']
    
    # ج) باکس جستجوی پیشرفته
    search_fields = ['name', 'description']
    
    # د) پر شدن خودکار اسلاگ محصول بر اساس نام آن
    prepopulated_fields = {'slug': ('name',)}
    
    # هـ) تزریق گالری فرعی به انتهای صفحه محصول
    inlines = [ProductMediaInline]



