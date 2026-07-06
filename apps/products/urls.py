from rest_framework.routers import DefaultRouter


from .views import ProductViewSet

# استفاده از روتر برای تولید خودکار 
# URL
# ها
router = DefaultRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = router.urls


