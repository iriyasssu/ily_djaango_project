from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at', 'price')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
