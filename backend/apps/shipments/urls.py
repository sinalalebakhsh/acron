from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerShipmentViewSet

router = DefaultRouter()
router.register('track', CustomerShipmentViewSet, basename='shipment-track')

urlpatterns = [
    path('', include(router.urls)),
]


