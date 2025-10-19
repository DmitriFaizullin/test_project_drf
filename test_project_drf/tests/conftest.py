import pytest
from django.contrib.auth import get_user_model

from products.models import Category, Products, Subcategory
from .constants import CATEGORY_DATA, PRODUCT_DATA, SUBCATEGORY_DATA, USER_DATA


User = get_user_model()


@pytest.fixture
def user_data():
    """Фикстура с валидными данными пользователя."""
    return USER_DATA


@pytest.fixture
def existing_user():
    """Фикстура создает существующего пользователя в базе."""
    User.objects.create_user(**USER_DATA)
    return USER_DATA


@pytest.fixture
def user_credentials():
    """Данные пользователя для аутентификации."""
    return USER_DATA


@pytest.fixture
def create_test_category():
    """Создает тестовые данные категории."""
    return Category.objects.create(**CATEGORY_DATA)


@pytest.fixture
def create_test_subcategory(create_test_category):
    """Создает тестовые данные подкатегории."""
    return Subcategory.objects.create(
        category=create_test_category,
        **SUBCATEGORY_DATA)


@pytest.fixture
def create_test_product(create_test_subcategory):
    """Создает тестовые данные продукта."""
    Products.objects.create(
        subcategory=create_test_subcategory,
        **PRODUCT_DATA)
