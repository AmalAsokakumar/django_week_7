from django.contrib import admin
from .models import Categories as Category



class categoryAdmin(admin.ModelAdmin):
    list_display= ('category_name', 'slug','cat_image')
    prepopulated_fields={'slug':('category_name',)}
# Register your models here.
admin.site.register(Category, categoryAdmin)
