# This file defines the URL patterns for the API app,
# which includes endpoints for managing carts, customers, products, orders, and payments.
from django.urls import include, path


# Importing TokenObtainPairView and TokenRefreshView from rest_framework_simplejwt.views,
# to handle JWT authentication for obtaining and refreshing tokens.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Importing views from the current module,
# which contains the logic for handling various API endpoints.
from . import views



urlpatterns = [
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API
    path('', include('apps.carts.urls')), 
    # orders
    path('', include('apps.orders.urls')), 
    # اضافه کردن مسیرهای مشاور هوشمند جدید
    path('', include('apps.advisor.urls')),
    # 🔑 JWT Authentication
    # 🔐 protected route
    path('me/', views.me),
    #  customers
    path('customers/', include('apps.customers.urls')), # مسیر مشتریان
    #  products
    path('products/', include('apps.products.urls')), # مسیر محصولات اضافه شد!
    # payments
    path('payments/', include('apps.payments.urls')), # مسیر پرداخت اضافه شد!
    # shipments
    path('shipments/', include('apps.shipments.urls')), # مسیر مرسولات اضافه شد!

]