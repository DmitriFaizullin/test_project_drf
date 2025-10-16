from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    """Модель для категорий товаров."""
    name = models.CharField('Название', max_length=30)
    slug = models.SlugField('Слаг', max_length=30, unique=True)
    image = models.ImageField(
        upload_to='categories/images/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Модель для подкатегорий товаров."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='Подкатегория'
    )
    name = models.CharField('Название', max_length=30)
    slug = models.SlugField('Слаг', max_length=30, unique=True)
    image = models.ImageField(
        'Изображение',
        upload_to='subcategories/images/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Products(models.Model):
    """Модель для товаров."""
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Подкатегория'
    )
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('Слаг', max_length=100, unique=True)
    price = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    image_small = models.ImageField(
        'Изображение (малое)',
        upload_to='products/images/small/',
        null=True,
        blank=True
    )
    image_medium = models.ImageField(
        'Изображение (среднее)',
        upload_to='products/images/medium/',
        null=True,
        blank=True
    )
    image_large = models.ImageField(
        'Изображение (большое)',
        upload_to='products/images/large/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self):
        return self.name
