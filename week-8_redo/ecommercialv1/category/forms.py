from .models import Categories as Category
from django.forms import  ModelForm, TextInput, ClearableFileInput


class CategoryForm(ModelForm):
    
        class Meta:
            model   = Category
            fields  = ['category_name','description','cat_image','offer_status']
            widgets ={
                'cat_image': ClearableFileInput(attrs={"class":"form-control-file","style":"width:80%"})
            }
            
        def  __init__(self, *arg, **kwargs):                            # using a constructor am applying style to each field of the above form (applying class form-control to every field it can also be done in mata class just like on the above class i have created password field and applied a widget for it to apply form control to it )
            super(CategoryForm, self).__init__(*arg, **kwargs)
            self.fields['category_name'].widget.attrs['placeholder'] = 'Enter Category Name'
            self.fields['description'].widget.attrs['placeholder'] = 'Description'
            self.fields['offer_status'].widget.attrs['placeholder']= 'offer_status'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] ='form-control'