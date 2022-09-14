from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create account model 
class accounts():
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    username    = models.CharField(max_length=50, unique=True)
    email       = models.EmailField(max_length=100, unique=True)
    phone       = models.CharField(max_length=50)
    
    #required fields are, mandatory while creating a user creation model 
    
    date_joined     = models.DateField(auto_now_add=True)
    last_login      = models.DateField(auto_now=True)
    is_super_admin   = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD  =['username', 'first_name','last_name']
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):  # admin has all the permissions do all the changes 
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    
    