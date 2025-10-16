from django.contrib import admin

from .models import Cart, CustomUser


class CartInline(admin.TabularInline):  # или admin.StackedInline
    """Inline для отображения товаров в корзине пользователя."""
    model = Cart
    extra = 0
    readonly_fields = ('product', 'quantity', 'total_price')

    def total_price(self, obj):
        return f"{obj.total_price} руб."
    total_price.short_description = 'Общая стоимость'

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CustomUser)
class CategoryAdmin(admin.ModelAdmin):
    """Админ-модель для управления пользователями."""
    inlines = [CartInline]
    list_display_links = ('username',)
    list_display = ('pk', 'username', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('email', 'last_name', 'username')
    list_filter = ('is_superuser', 'is_active',)
