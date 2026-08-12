from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    # JWT Authentication
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Protected current-user endpoint
    path(
        "me/",
        views.me,
        name="api-me",
    ),

    # Other API domains
    path(
        "payments/",
        include("apps.payments.urls"),
    ),

    path(
        "shipments/",
        include("apps.shipments.urls"),
    ),

    path(
        "advisor/",
        include("apps.advisor.urls"),
    ),
]