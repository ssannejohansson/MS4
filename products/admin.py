from django.contrib import admin
from .models import Product, ProductVariant, Category

# Register your models here.


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline]
    list_display = (
        'sku',
        'name',
        'category',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
