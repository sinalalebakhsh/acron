# apps/orders/views.py

# this file contains views for managing customer profiles and addresses in the orders app.

# It uses Django REST framework's generic views and viewsets to handle HTTP requests.
from rest_framework.viewsets import ModelViewSet

# Import the RetrieveUpdateAPIView from the Django REST framework, 
# which allows for retrieving and updating a model instance.
from rest_framework.generics import RetrieveUpdateAPIView

# Import the IsAuthenticated permission class from the Django REST framework,
# which restricts access to authenticated users only.
from rest_framework.permissions import IsAuthenticated

# Import the Customer and Address models from the current app's models module.
from .models import Customer, Address

# Import the serializers for customer profile and address management from the current app's serializers module.
from .serializers import CustomerProfileSerializer, AddressSerializer

# Define a view for managing the customer's own profile.
class CustomerProfileView(RetrieveUpdateAPIView):
    """
    این ویو برای مشاهده و ویرایش پروفایل کاربری خود شخص است.
    This view is for viewing and editing a person's own user profile.
    # this view uses the CustomerProfileSerializer to serialize and deserialize data.
    """

    # serializer_class specifies the serializer to be used for this view.
    serializer_class = CustomerProfileSerializer

    # Restrict access to authenticated users only.
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # این متد جادویی باعث می‌شود نیازی به ارسال ID در URL نباشد.
        # کاربر بر اساس توکنی که می‌فرستد، فقط پروفایل خودش را دریافت می‌کند.
        # This magic method eliminates the need to send the ID in the URL.
        # The user only gets their own profile based on the token they send.
        customer, created = Customer.objects.get_or_create(user=self.request.user)
        return customer

# Define a viewset for managing user mailing addresses.
class AddressViewSet(ModelViewSet):
    """
    مدیریت آدرس‌های پستی کاربر
    Manage user mailing addresses
    """
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # هر کاربر فقط آدرس‌های خودش را می‌بیند
        # Each user only sees their own addresses
        return Address.objects.filter(customer__user=self.request.user)

    def perform_create(self, serializer):
        # در زمان ساخت آدرس جدید، فیلد customer به صورت خودکار با کاربر فعلی پر می‌شود
        # When creating a new address, the customer field is automatically filled with the current user
        customer, created = Customer.objects.get_or_create(user=self.request.user)
        serializer.save(customer=customer)




