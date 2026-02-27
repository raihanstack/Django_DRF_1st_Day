from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'featured']
    list_editable = ['price', 'featured']
    list_display_links = ['id', 'title']

admin.site.register(Product, ProductAdmin)