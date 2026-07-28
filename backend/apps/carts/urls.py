from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()

# 🔴 ثبت cart-items قبل از '' ضروری است تا تداخل URL ایجاد نشود
router.register('cart-items', CartItemViewSet, basename='cart-items')
router.register('', CartViewSet, basename='carts')

urlpatterns = [
    path('', include(router.urls)),
]