# This file defines the URL patterns for the payments app, 
# which includes endpoints for initiating payments and simulating bank callbacks.
from django.urls import path, include

# Importing DefaultRouter from Django REST framework,
# to automatically generate URL patterns for the PaymentViewSet.
from rest_framework.routers import DefaultRouter

# This import statement brings in the PaymentViewSet class,
# from the views module of the payments app, 
# which contains the logic for handling payment-related actions.
from .views import PaymentViewSet

# This block of code sets up a router for the payments app,
# registering the PaymentViewSet with the router under the 'payments' prefix.
router = DefaultRouter()
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
]



