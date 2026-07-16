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



