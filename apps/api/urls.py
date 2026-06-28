from django.urls import include, path
from django.http import HttpResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


def api_root(request):
    return HttpResponse("API ROOT is under development 🚀")


urlpatterns = [
    path('', api_root),

    # JWT
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    # 🔐 protected route
    path('me/', views.me),
    path('secret/', views.secret_api),

    path('customers/', include('apps.customers.urls')),

]