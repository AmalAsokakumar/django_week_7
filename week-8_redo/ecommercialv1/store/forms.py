from .models import Product 
from django.forms import  ModelForm, TextInput, ClearableFileInput



class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields= ['product_name',
                 'slug',
                 'description',
                 'price',
                 'images',
                 'stock',
                 'is_available',
                 'offer_status', 
                 'category',
                 'brand',
                ]
        widgets = {
            'images' :  ClearableFileInput(attrs={"class":"form-control-file","style":"width:80%"})
        }