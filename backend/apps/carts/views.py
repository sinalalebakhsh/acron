from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.customers.models import Customer
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.create()
        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            customer, _ = Customer.objects.get_or_create(user=request.user)
            cart, _ = Cart.objects.get_or_create(customer=customer)
        else:
            cart = Cart.objects.create()

        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='mine', permission_classes=[IsAuthenticated])
    def mine(self, request):
        customer, _ = Customer.objects.get_or_create(user=request.user)
        cart, _ = Cart.objects.get_or_create(customer=customer)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class CartItemViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post', 'patch', 'delete']
    queryset = CartItem.objects.select_related('product').all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer