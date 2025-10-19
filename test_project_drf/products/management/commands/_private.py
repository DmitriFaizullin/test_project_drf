from django.contrib.auth import get_user_model

from products.models import Category, Subcategory, Products
from users.models import Cart

User = get_user_model()


class CommandMixin():
    """Миксин для класса Command, обработчика загрузки csv-файлов."""

    def load_users(self):
        """Загрузка пользователей."""
        for number_str, colls in enumerate(self.csvreader):
            try:
                User.objects.update_or_create(**colls)
            except Exception as error:
                self.stdout.write(self.style.WARNING(
                    f'Строка {number_str} не загружена: {error}'))

    def load_category(self):
        """Загрузка категорий."""
        for number_str, colls in enumerate(self.csvreader):
            try:
                Category.objects.update_or_create(**colls)
            except Exception as error:
                self.stdout.write(self.style.WARNING(
                    f'Строка {number_str} не загружена: {error}'))

    def load_subcategory(self):
        """Загрузка подкатегорий."""
        for number_str, colls in enumerate(self.csvreader):
            try:
                Subcategory.objects.update_or_create(**colls)
            except Exception as error:
                self.stdout.write(self.style.WARNING(
                    f'Строка {number_str} не загружена: {error}'))

    def load_products(self):
        """Загрузка товаров."""
        for number_str, colls in enumerate(self.csvreader):
            try:
                Products.objects.update_or_create(**colls)
            except Exception as error:
                self.stdout.write(self.style.WARNING(
                    f'Строка {number_str} не загружена: {error}'))

    def load_cart(self):
        """Загрузка корзины."""
        for number_str, colls in enumerate(self.csvreader):
            try:
                Cart.objects.update_or_create(**colls)
            except Exception as error:
                self.stdout.write(self.style.WARNING(
                    f'Строка {number_str} не загружена: {error}'))

    TABLE_HANDLER = {
        'users': load_users,
        'categories': load_category,
        'subcategories': load_subcategory,
        'products': load_products,
        'cart': load_cart,
    }
