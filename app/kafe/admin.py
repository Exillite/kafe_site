from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_published')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name", "price")}

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'context')
    search_fields = ('key', 'context')
    list_editable = ('context',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'link', 'isdelivery', 'isfinish')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Sales)
admin.site.register(Review)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(SitePhoto)
