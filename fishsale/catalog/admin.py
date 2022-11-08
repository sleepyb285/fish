from django.contrib import admin
from .models import Category, Product, Location
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    prepopulated_fields = {"slug": ("name",)}
    pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    pass

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

admin.site.register(Location)


