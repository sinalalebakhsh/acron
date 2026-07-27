from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import action

from .models import Customer, Address
from .serializers import CustomerProfileSerializer, AddressSerializer, CustomerSerializer
from .services import AddressService


class CustomerMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customer, _ = Customer.objects.get_or_create(user=request.user)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def patch(self, request):
        customer, _ = Customer.objects.get_or_create(user=request.user)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CustomerProfileView(RetrieveUpdateAPIView):
    """
    این ویو برای مشاهده و ویرایش پروفایل کاربری خود شخص است.
    """
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # این متد باعث می‌شود نیازی به ارسال ID در URL نباشد.
        # کاربر بر اساس توکنی که می‌فرستد، فقط پروفایل خودش را دریافت می‌کند.
        customer, created = Customer.objects.get_or_create(user=self.request.user)
        return customer


class AddressViewSet(ModelViewSet):
    """
    مدیریت آدرس‌های پستی کاربر
    """
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # هر کاربر فقط آدرس‌های خودش را می‌بیند
        return Address.objects.filter(customer__user=self.request.user)

    def perform_create(self, serializer):
        customer, _ = Customer.objects.get_or_create(user=self.request.user)
        
        # اگر این اولین آدرس کاربر باشد، به صورت خودکار پیش‌فرض می‌شود
        is_first = not Address.objects.filter(customer=customer).exists()
        
        # اگر کاربر آدرس جدید را پیش‌فرض انتخاب کرده یا اولین آدرسش است
        if serializer.validated_data.get('is_default', False) or is_first:
            Address.objects.filter(customer=customer, is_default=True).update(is_default=False)
            serializer.save(customer=customer, is_default=True)
        else:
            serializer.save(customer=customer)

    @action(detail=True, methods=['post'], url_path='set-default')
    def set_default(self, request, pk=None):
        """
        اکشن اختصاصی برای انتخاب آدرس پیش‌فرض:
        POST /api/customers/addresses/{id}/set-default/
        """
        try:
            address = AddressService.set_default_address(request.user, pk)
            return Response(
                {
                    "detail": "آدرس پیش‌فرض با موفقیت تغییر کرد.",
                    "address": AddressSerializer(address).data
                },
                status=status.HTTP_200_OK
            )
        except (Address.DoesNotExist, Customer.DoesNotExist):
            return Response(
                {"detail": "آدرس یا مشتری یافت نشد."},
                status=status.HTTP_404_NOT_FOUND
            )
    
    
    