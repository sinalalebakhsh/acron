from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import serializers as rest_serializers


from . import serializers


# 🔐 API محافظت‌شده
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)




# --- Serializer ---
class APIDirectorySerializer(rest_serializers.Serializer):
    """
    یک سریالایزر برای اعتبارسنجی و فرمت‌دهی لیست مسیرهای API.
    """
    authentication = rest_serializers.DictField(child=rest_serializers.URLField())
    user_management = rest_serializers.DictField(child=rest_serializers.URLField())
    resources = rest_serializers.DictField(child=rest_serializers.URLField())


# --- View ---
@api_view(['GET'])
@permission_classes([AllowAny]) # 🔓 دسترسی آزاد برای همه کاربران
def api_root_view(request):
    """
    نقطه ورود API که مسیرهای موجود را لیست می‌کند.
    """
    # ساخت دیتای خام شامل لینک‌های قابل کلیک
    raw_data = {
        "authentication": {
            "token": request.build_absolute_uri('token/'),
            "token_refresh": request.build_absolute_uri('token/refresh/'),
        },
        "user_management": {
            "me": request.build_absolute_uri('me/'),
        },
        "resources": {
            "customers": request.build_absolute_uri('customers/'),
            "products": request.build_absolute_uri('products/'),
        }
    }
    
    # عبور دادن دیتا از سریالایزر (طبق درخواست شما)
    serializer = APIDirectorySerializer(data=raw_data)
    serializer.is_valid(raise_exception=True)
    
    # بازگرداندن پاسخ که توسط DRF به صورت گرافیکی رندر می‌شود
    return Response(serializer.validated_data)



