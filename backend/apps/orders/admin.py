from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    # فاکتور نهایی نباید توسط ادمین دستکاری شود تا جلوی فساد مالی گرفته شود
    readonly_fields = ['product', 'quantity', 'unit_price']
    can_delete = False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['id', 'customer__user__username']
    inlines = [OrderItemInline]
    
    # سفارشات ثبت شده نباید خودسرانه حذف شوند
    def has_delete_permission(self, request, obj=None):
        return False


