# This is a Django viewset for handling payment-related actions, 
# including initiating payments and simulating bank callbacks for testing purposes.
from rest_framework.viewsets import GenericViewSet

# Importing necessary modules from Django REST framework,
# for handling HTTP responses, actions, and permissions.
from rest_framework.response import Response

# Importing decorators and permissions to manage access control for the viewset actions.
from rest_framework.decorators import action

# Why are we importing IsAuthenticated and AllowAny?
# We import IsAuthenticated to ensure that only authenticated users can initiate payments,
from rest_framework.permissions import IsAuthenticated, AllowAny

# Why are we importing extend_schema?
# We import extend_schema from drf_spectacular to provide detailed API documentation for the view
from drf_spectacular.utils import extend_schema

# Why are we importing serializers and services?
# We import serializers to validate and serialize the incoming request data for initiating payments
from .serializers import InitiatePaymentSerializer, MockBankCallbackSerializer

# Why are we importing PaymentService?
# We import PaymentService to handle the business logic related to payment processing,
from .services import PaymentService

# What is the purpose of the PaymentViewSet class?
# The PaymentViewSet class 
# is a Django viewset that provides endpoints for initiating payments and simulating bank callbacks.
class PaymentViewSet(GenericViewSet):
    
    @extend_schema(request=InitiatePaymentSerializer, summary="درخواست تولید لینک پرداخت", tags=['Payments'])
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def initiate(self, request):
        serializer = InitiatePaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        order_id = serializer.validated_data['order_id']
        
        # ارسال به هسته مرکزی پرداخت
        url, trx_id = PaymentService.initiate_payment(order_id, request.user)
        
        return Response({
            "message": "لینک پرداخت با موفقیت تولید شد.",
            "gateway_url": url,
            "transaction_id": trx_id
        })

    @extend_schema(request=MockBankCallbackSerializer, summary="شبیه‌ساز درگاه بانک (تست)", tags=['Payments'])
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def mock_verify(self, request):
        """
        این ویو نقش بانک را بازی می‌کند. 
        در دنیای واقعی، بانک پس از پرداخت کاربر، اطلاعات را به یک URL مشابه این می‌فرستد.
        """
        serializer = MockBankCallbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        trx_id = serializer.validated_data['transaction_id']
        is_successful = serializer.validated_data['is_successful']
        
        payment = PaymentService.verify_mock_payment(trx_id, is_successful)
        
        return Response({
            "payment_status": payment.get_status_display(),
            "order_status": payment.order.get_status_display()
        })



