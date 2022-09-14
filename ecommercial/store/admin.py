from itertools import product
from django.contrib import admin
from .models import Product
# Register your models here.


# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'product_name','price','stock','category','modified_date','is_available',
        
#         )
#     prepopulated_fields = {'slug' : ('product_name',)} # comma must be provided because the tuple only has a single item 

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Product)