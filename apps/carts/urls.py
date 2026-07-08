from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
# ثبت ویوست سبد خرید (آی‌دی این مسیر از نوع UUID خواهد بود)
router.register('carts', CartViewSet, basename='carts')

# ثبت ویوست آیتم‌های سبد خرید
router.register('cart-items', CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', include(router.urls)),
]



