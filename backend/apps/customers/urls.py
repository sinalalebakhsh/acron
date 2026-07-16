from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerProfileView, AddressViewSet

router = DefaultRouter()
router.register('addresses', AddressViewSet, basename='addresses')

urlpatterns = [
    path('profile/', CustomerProfileView.as_view(), name='customer-profile'),
    path('', include(router.urls)),
]



