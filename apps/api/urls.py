from django.urls import path
from django.http import HttpResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def api_root(request):
    return HttpResponse("API is working 🚀")


urlpatterns = [
    path('', api_root),

    # 🔐 JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]