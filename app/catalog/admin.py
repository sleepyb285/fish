from django.contrib import admin
from .models import Fish,Provider,Category
# Register your models here.
class FishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Provider)
admin.site.register(Fish, FishAdmin)