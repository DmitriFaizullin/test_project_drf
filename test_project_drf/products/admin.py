from django.contrib import admin

from .models import Category, Subcategory, Products


class SubcategoryInline(admin.TabularInline):
    """Для отображения подкатегорий в категории."""
    model = Subcategory
    extra = 0
    readonly_fields = ('name', 'slug')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админ-модель для управления категориями."""
    inlines = [SubcategoryInline]
    list_display_links = ('name',)
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class ProductsInline(admin.TabularInline):
    """Для отображения товаров в подкатегории."""
    model = Products
    extra = 0
    readonly_fields = ('name', 'slug', 'price')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    """Админ-модель для управления категориями."""
    inlines = [ProductsInline]
    list_display_links = ('name',)
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    """Админ-модель для управления продуктами."""
    list_display_links = ('name',)
    list_display = ('pk', 'name', 'slug', 'price')
    search_fields = ('name',)
    list_filter = ('name',)
    list_editable = ('price',)
