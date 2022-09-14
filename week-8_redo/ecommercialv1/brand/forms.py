from .models import Brand as brand
from django.forms import ModelForm, TextInput, ClearableFileInput


class BrandForm(ModelForm):
    
    class Meta:
        model   = brand 
        fields  = ['brand_name','description','brand_image','offer_status']
        widgets ={
                'brand_image': ClearableFileInput(attrs={"class":"form-control-file","style":"width:80%"})
            }
            
        def  __init__(self, *arg, **kwargs):                            # using a constructor am applying style to each field of the above form (applying class form-control to every field it can also be done in mata class just like on the above class i have created password field and applied a widget for it to apply form control to it )
            super(BrandForm, self).__init__(*arg, **kwargs)
            self.fields['brand_name'].widget.attrs['placeholder']  = 'Enter Brand Name'
            self.fields['description'].widget.attrs['placeholder'] = 'Description'
            self.fields['offer_status'].widget.attrs['placeholder']= 'offer_status'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] ='form-control'