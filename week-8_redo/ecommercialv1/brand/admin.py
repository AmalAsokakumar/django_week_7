from django.contrib import admin
from .models import Brand

# Register your models here.
class brandAdmin(admin.ModelAdmin):
    list_display =('brand_name', 'brand_slug','brand_image')
    prepopulated_fields= {'brand_slug':('brand_name',)}
admin.site.register(Brand, brandAdmin)