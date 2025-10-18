from django.urls import include, path
from rest_framework import routers

from .views import CartViewSet, ProductViewSet

product_router = routers.DefaultRouter()

product_router.register('products', ProductViewSet, basename='products')
product_router.register('cart', CartViewSet, basename='cart')
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include(product_router.urls)),
]
