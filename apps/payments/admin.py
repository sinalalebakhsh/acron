from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'order', 'amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['transaction_id', 'order__id']
    
    # تمام فیلدهای مالی را برای ادمین Read-Only می‌کنیم تا امنیت حفظ شود
    readonly_fields = ['transaction_id', 'order', 'amount', 'status', 'created_at', 'updated_at']

    def has_add_permission(self, request):
        return False # ادمین نباید بتواند دستی تراکنش مالی خلق کند

    def has_delete_permission(self, request, obj=None):
        return False # تراکنش مالی هرگز نباید حذف شود


