from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from products.models import Category, Products
from users.models import Cart
from .serializers import (CartUpdateSerializer,
                          CategorySerializer,
                          ProductSerializer,
                          CartAddSerializer,
                          CartDetailSerializer)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для чтения товаров."""
    queryset = Products.objects.select_related(
        'subcategory',
        'subcategory__category'
    ).all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для просмотра категорий с подкатегориями."""
    queryset = Category.objects.prefetch_related('subcategories').all()
    serializer_class = CategorySerializer


class CartViewSet(viewsets.ModelViewSet):
    """ViewSet для управление корзиной."""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CartAddSerializer
    http_method_names = ['get', 'post', 'delete', 'put']

    def get_queryset(self):
        if self.action == 'list':
            print(self.action)
            return Cart.objects.filter(user=self.request.user).select_related(
                'product',
                'product__subcategory',
                'product__subcategory__category'
            )
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return CartDetailSerializer
        elif self.action == 'update':
            return CartUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total_quantity = sum(item.quantity for item in queryset)
        total_amount = sum(
            item.quantity * item.product.price for item in queryset)
        return Response({'products': serializer.data,
                         'total_quantity': total_quantity,
                         'total_amount': total_amount})

    @action(detail=False, methods=['delete'])
    def clear(self, request):
        self.get_queryset().delete()
        return Response({"message": "корзина очищена"})
