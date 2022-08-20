from django.contrib import admin
from .models import *
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_published')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name", "price")}

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'context')
    search_fields = ('key', 'context')
    list_editable = ('context',)

@admin.display(description="Firm URL")
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'show_firm_url', 'isdelivery', 'isfinish')
    list_filter = ("isfinish", )

    def show_firm_url(self, obj):
        return format_html(f"<a href='{obj.link}' target='_blank'>Открыть заказ</a>")

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Sales)
admin.site.register(Review)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(SitePhoto)
