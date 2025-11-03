from django.contrib import admin

from store.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productName', 'price', 'stock', 'category', 'updated_date', 'is_available')
    prepopulated_fields = {"slug": ("productName",)}
    list_filter = ('category',)
    search_fields = ('productName',)


admin.site.register(Product, ProductAdmin)