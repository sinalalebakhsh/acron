from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, CustomerProfileView

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = [
    path('profile/', CustomerProfileView.as_view(), name='user-profile'),
    path('', include(router.urls)),
]
