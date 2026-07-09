# This file defines the URL patterns for the orders app, 
# specifically for managing customer profiles and addresses. 
# It uses Django's path function to define URL routes and 
# includes a router from the Django REST framework 
# to automatically generate URL patterns for the AddressViewSet.
from django.urls import path, include

# Import the DefaultRouter from the Django REST framework, 
# which will be used to automatically generate URL patterns for the viewsets.
from rest_framework.routers import DefaultRouter

# Import the views that will handle the requests for customer profile and address management
from .views import CustomerProfileView, AddressViewSet

# Create a router and register the viewsets with it
router = DefaultRouter()
"""
The default router extends the SimpleRouter, but also adds in a default
API root view, and adds format suffix patterns to the URLs.
"""

# Register the AddressViewSet with the router, which will automatically generate the URL patterns for the viewset.
router.register('addresses', AddressViewSet, basename='addresses')

urlpatterns = [
    # URL pattern for viewing and editing the customer's own profile
    path('profile/', CustomerProfileView.as_view(), name='customer-profile'),

    # The router automatically generates the URL patterns 
    # for the AddressViewSet, including list, create, retrieve, update, and delete actions.
    path('', include(router.urls)),
]



