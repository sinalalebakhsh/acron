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



