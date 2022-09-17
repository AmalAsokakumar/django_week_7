from django.contrib import admin
from .models import Brands as Brand

# Register your models here.
class brandAdmin(admin.ModelAdmin):
    list_display =('brand_name', 'slug','brand_image')
    prepopulated_fields= {'slug':('brand_name',)}
admin.site.register(Brand, brandAdmin)