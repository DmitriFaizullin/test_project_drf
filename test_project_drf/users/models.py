from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

from products.models import Products


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""
    cart_products = models.ManyToManyField(
        Products,
        through='Cart',
        through_fields=('user', 'product'),
        related_name='in_user_cart',
        verbose_name='Товары в корзине',
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)


class Cart(models.Model):
    "Модель корзины товаров."
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='cart_entries',
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(
        'Количество',
        default=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.quantity})'

    @property
    def total_price(self):
        return self.product.price * self.quantity
