from django.contrib import admin
from .models import Fish,Provider,Category,Attribute,FilterInfo, Feedback, Location
# Register your models here.

class FilterInfoInLine(admin.TabularInline):
    model = FilterInfo
    extra = 0

class FishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [FilterInfoInLine]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ProviderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AttributeAdmin(admin.ModelAdmin):
    inlines = [FilterInfoInLine]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Fish, FishAdmin)
admin.site.register(Attribute,AttributeAdmin)
admin.site.register(Feedback)
admin.site.register(Location)



