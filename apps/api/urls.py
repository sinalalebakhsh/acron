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

    # This is the URL pattern for the carts app, 
    # which includes endpoints for managing shopping carts.
    # اضافه کردن مسیر سبد خرید به قلب 
    # API
    path('', include('apps.carts.urls')), 
    # # 📌 مسیر اصلی که لیست تمام API ها را نشان می‌دهد
    # path('', views.api_root_view, name='api-root'),


    # This is the URL pattern for the authentication endpoints, 
    # which includes endpoints for obtaining and refreshing JWT tokens.
    # 🔑 JWT Authentication
    # JWT
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),



    # This is the URL pattern for the user-related endpoints, 
    # which includes endpoints for managing user profiles and authentication.
    # 🔐 protected route
    path('me/', views.me),


    # This is the URL pattern for the customers app, 
    # which includes endpoints for managing customer-related actions.
    #  customers
    path('customers/', include('apps.customers.urls')), # مسیر مشتریان

    # This is the URL pattern for the products app, 
    # which includes endpoints for managing products.
    #  products
    path('products/', include('apps.products.urls')), # مسیر محصولات اضافه شد!

    # This is the URL pattern for the orders app, 
    # which includes endpoints for managing orders.
    # orders
    path('', include('apps.orders.urls')), # اضافه شدن مسیر سفارشات


    # This is the URL pattern for the payments app, 
    # which includes endpoints for initiating payments and simulating bank callbacks.
    # It uses the include function to include the URL patterns defined 
    # in the   apps/payments/urls.py file.
    # This allows the payments app to have its own set of URL patterns, 
    # payments
    path('payments/', include('apps.payments.urls')), # مسیر پرداخت اضافه شد!


]