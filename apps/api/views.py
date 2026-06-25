from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers


# 🔐 API محافظت‌شده
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)
    return Response({
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email,
        
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret_api(request):
    return Response({
        "message": "secret"
    })

