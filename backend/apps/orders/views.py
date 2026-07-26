# apps/orders/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer, OrderCreateInputSerializer
from .services import OrderService

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # فیلتر سفارشات بر اساس کاربر جاری از طریق رابط Customer
        return Order.objects.filter(
            customer__user=self.request.user
        ).prefetch_related('items__product').order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateInputSerializer
        return OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_id = serializer.validated_data['cart_id']
        shipping_address = serializer.validated_data['shipping_address']

        order = OrderService.place_order(
            user=request.user,
            cart_id=cart_id,
            shipping_address=shipping_address
        )

        output_serializer = OrderSerializer(order)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


    