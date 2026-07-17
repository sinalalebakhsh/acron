# apps/advisor/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvisorViewSet

# استفاده از DefaultRouter برای ساخت خودکار مسیرهای استاندارد RESTful
router = DefaultRouter()
router.register(r'advisor', AdvisorViewSet, basename='advisor')

urlpatterns = [
    path('', include(router.urls)),
]



