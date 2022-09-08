from django.contrib import admin
from .models import category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)} # here we are using a tuple ('category_name') which only contain only value hence we use ','
    list_display = ('category_name','slug') # these two fields will be shown when we access this table without actually opening that row. these data will be show in the data table rows 

admin.site.register(category, CategoryAdmin)