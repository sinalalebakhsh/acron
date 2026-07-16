from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'user',
        'phone_number',
        'birth_date',
    ]

    search_fields = [
        'user__username',
        'phone_number',
    ]