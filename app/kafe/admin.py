from django.contrib import admin
from .models import *


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sales)
admin.site.register(Review)
admin.site.register(SiteSettings)