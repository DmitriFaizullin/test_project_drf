from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from .views import CartViewSet, ProductViewSet, CategoryViewSet

product_router = routers.DefaultRouter()

product_router.register('products', ProductViewSet, basename='products')
product_router.register('categories', CategoryViewSet, basename='categories')
product_router.register('cart', CartViewSet, basename='cart')
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('', include(product_router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
