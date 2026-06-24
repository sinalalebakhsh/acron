from django.urls import path
from django.http import HttpResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import me


def api_root(request):
    return HttpResponse("API is working 🚀")


urlpatterns = [
    path('', api_root),

    # JWT
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    # 🔐 protected route
    path('me/', me),
]