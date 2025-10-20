from django.contrib import admin

from .models import Category, Subcategory, Products


class BaseInline(admin.TabularInline):
    """Базовый inline для админки."""
    extra = 0
    readonly_fields = ('name', 'slug')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SubcategoryInline(BaseInline):
    """Для отображения подкатегорий в категории."""
    model = Subcategory


class ProductsInline(BaseInline):
    """Для отображения товаров в подкатегории."""
    model = Products
    readonly_fields = ('name', 'slug', 'price')


class BaseAdmin(admin.ModelAdmin):
    """Базовый класс для настройки админки."""
    list_display_links = ('name',)
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    """Админ-модель для управления категориями."""
    inlines = [SubcategoryInline]


@admin.register(Subcategory)
class SubcategoryAdmin(BaseAdmin):
    """Админ-модель для управления подкатегориями."""
    inlines = [ProductsInline]


@admin.register(Products)
class ProductAdmin(BaseAdmin):
    """Админ-модель для управления продуктами."""
    list_display = ('pk', 'name', 'slug', 'price')
    list_editable = ('price',)
