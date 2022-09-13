from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        # 'class' : 'form-control',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'confirm password',
        # 'class' : 'form-control',
    }))
    class Meta:
        model = Account 
        fields = ['first_name','last_name','phone_number','email','password']  # here am mentioning all the required files from the models.py accounts section. 
    # here we are planning to generate username for the user hence its not mentioned. 
   
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean() #super function is used to change the way this class is being saved. 
        password  = cleaned_data.get('password')
        confirmed_password = cleaned_data.get('confirmed_password')
        # check if both password fields are same.
        
        if password != confirmed_password:
            raise forms.ValidationError("password does not match!")
        
        
    def  __init__(self, *arg, **kwargs):                            # using a constructor am applying style to each field of the above form (applying class form-control to every field it can also be done in mata class just like on the above class i have created password field and applied a widget for it to apply form control to it )
            super(RegistrationForm, self).__init__(*arg, **kwargs)
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
            self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
            self.fields['phone_number'].widget.attrs['placeholder']= 'Enter your Phone Number'
            for field in self.fields:
                self.fields[field].widget.attrs['class'] ='form-control'
                
   