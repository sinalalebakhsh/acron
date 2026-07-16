from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated


from .models import Customer, Address

from .serializers import CustomerProfileSerializer, AddressSerializer,CustomerSerializer



class CustomerMeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomerSerializer(request.user.customer)
        return Response(serializer.data)

    def patch(self, request):
        serializer = CustomerSerializer(request.user.customer,data=request.data,partial=True)
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
        # این متد جادویی باعث می‌شود نیازی به ارسال ID در URL نباشد.
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
        # در زمان ساخت آدرس جدید، فیلد customer به صورت خودکار با کاربر فعلی پر می‌شود
        customer, created = Customer.objects.get_or_create(user=self.request.user)
        serializer.save(customer=customer)




