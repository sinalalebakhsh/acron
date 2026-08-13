from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),

    # -------------------------
    # Domain APIs
    # -------------------------

    path(
        "api/carts/",
        include("apps.carts.urls"),
    ),

    path(
        "api/customers/",
        include("apps.customers.urls"),
    ),

    path(
        "api/products/",
        include("apps.products.urls"),
    ),

    path(
        "api/orders/",
        include("apps.orders.urls"),
    ),

    # -------------------------
    # General API
    # -------------------------

    path(
        "api/",
        include("apps.api.urls"),
    ),

    # -------------------------
    # API Documentation
    # -------------------------

    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),

    path(
        "api/redoc/",
        SpectacularRedocView.as_view(
            url_name="schema"
        ),
        name="redoc",
    ),
]


if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

    