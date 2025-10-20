from rest_framework import serializers

from products.models import Category, Products, Subcategory
from users.models import Cart


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор для подкатегорий"""
    image = serializers.SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = ('name', 'slug', 'image')

    def get_image(self, obj):
        return obj.get_image_url()


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий с подкатегориями"""
    subcategories = SubcategorySerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategories')

    def get_image(self, obj):
        return obj.get_image_url()


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для товаров."""
    category = serializers.CharField(source='subcategory.category.name')
    subcategory = serializers.CharField(source='subcategory.name')
    images = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ('name', 'slug', 'category', 'subcategory', 'price', 'images')

    def get_images(self, obj):
        return obj.get_image_urls()


class CartAddSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления товара в корзину."""
    class Meta:
        model = Cart
        fields = ('product', 'quantity')

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "Количество должно быть не менее 1")
        return value

    def validate(self, data):
        user = self.context['request'].user
        product = data['product']

        if Cart.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError({
                "product": "Товар уже находится в корзине"
            })
        return data


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('quantity',)

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Количество не может быть отрицательным")
        return value


class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('product', 'quantity', 'total_price')

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
