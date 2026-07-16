from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'status', 'carrier', 'tracking_number', 'created_at']
    list_filter = ['status', 'carrier', 'created_at']
    search_fields = ['order__id', 'tracking_number']
    
    # سفارش مربوطه نباید در انبار جابجا شود
    readonly_fields = ['order', 'created_at', 'shipped_at', 'delivered_at']
    
    fieldsets = (
        ("اطلاعات پایه سفارش", {
            'fields': ('order', 'created_at')
        }),
        ("وضعیت لجستیک و انبارداری", {
            'fields': ('status', 'carrier', 'tracking_number')
        }),
        ("زمان‌بندی‌های ارسال", {
            'fields': ('shipped_at', 'delivered_at'),
            'classes': ('collapse',) # این بخش را پنهان میکند تا صفحه شلوغ نشود
        }),
    )



