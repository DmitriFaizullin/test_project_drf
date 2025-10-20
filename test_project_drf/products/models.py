from django.db import models
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    """Базовая модель для категорий и подкатегорий."""
    name = models.CharField('Название', max_length=30)
    slug = models.SlugField('Слаг', max_length=30, unique=True)
    image = None

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_image_url(self):
        return self.image.url if self.image else None


class Category(BaseModel):
    """Модель для категорий товаров."""
    image = models.ImageField(
        upload_to='categories/images/',
        null=True,
        blank=True
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(BaseModel):
    """Модель для подкатегорий товаров."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='Подкатегория'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='subcategories/images/',
        null=True,
        blank=True
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


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

    def get_image_urls(self):
        return [
            self.image_small.url if self.image_small else None,
            self.image_medium.url if self.image_medium else None,
            self.image_large.url if self.image_large else None
        ]
