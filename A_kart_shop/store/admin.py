from django.contrib import admin
from .models import Category, Product, SubCategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Displays ID and name in the list view
    search_fields = ('name',)  # Enables search by name

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')  # Displays ID, name, and parent category
    list_filter = ('parent',)  # Adds filter for parent category in the sidebar
    search_fields = ('name',)  # Enables search by name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'sub_category')  # Fields to display
    list_filter = ('category', 'sub_category')  # Filters for categories
    search_fields = ('name', 'description')  # Search by name and description
    ordering = ('-price',)  # Orders products by price in descending order

