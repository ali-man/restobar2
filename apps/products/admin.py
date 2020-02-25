from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from apps.products.models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class SpecificationAdmin(admin.TabularInline):
    model = Specification
    extra = 4


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'sort']
    list_editable = ['sort']
    sortable_by = ['sort']
    mptt_level_indent = 20


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'new_price', 'leasing_price', 'category']
    list_display_links = ['name']
    list_editable = ['price', 'new_price', 'leasing_price']
    inlines = [ProductImageInline, SpecificationAdmin]
    fields = [
        ('category', 'manufacturer', 'country'),
        ('name', 'shipping', 'warranty'),
        ('price', 'new_price', 'leasing_price'),
        ('serving', 'types_drinks', 'ingredients'),
        ('desc_short',
        'desc_full',
        'menu'),
    ]


class OtherInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu_name']
    list_display_links = ['title']
    list_editable = ['menu_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OtherInfo, OtherInfoAdmin)
