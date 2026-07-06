from django.urls import include, path
from django.http import HttpResponse


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views



urlpatterns = [
    # 📌 مسیر اصلی که لیست تمام API ها را نشان می‌دهد
    path('', views.api_root_view, name='api-root'),

    # JWT
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    # 🔐 protected route
    path('me/', views.me),
    
    #  customers
    path('customers/', include('apps.customers.urls')), # مسیر مشتریان

    #  products
    path('products/', include('apps.products.urls')), # مسیر محصولات اضافه شد!



]