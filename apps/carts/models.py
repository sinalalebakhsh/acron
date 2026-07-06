from django.db import models

import uuid

from apps.products.models import Product


class Cart(models.Model):
    # الف) جایگزینی 
    # ID
    #  عددی با 
    # UUID
    #  به عنوان کلید اصلی امنیتی
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    # ب) اتصال آیتم به سبد خرید
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    
    # ج) اتصال آیتم به محصول
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    
    # د) تعداد محصول در سبد
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        # هـ) جلوگیری از ساخت دو ردیف برای یک محصول تکراری در یک سبد
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"# Create your models here.
