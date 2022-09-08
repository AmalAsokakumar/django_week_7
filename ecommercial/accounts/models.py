from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # 

# in this app we are creating custom user model because we wanted to login to the system using email instead of the username which is default in case of the django. so we are creating a custom user model. 
# look more in the custom user model creation in details. 
# we should mention that we are using a custom user model in django settings file. 


# Create your models here.
class MyAccountManager(BaseUserManager):
    # here we haven't create turned on any active flag which will only turned on when the otp verification is completed.
    
    # this def function is used to create a new user in
    def create_user(self, first_name, last_name, username, email, password=None): # this function is used to create users with the data obtained from registration form.
        # if the expected fields are not present we should raise an error, 
        if not email: # if email id is not present 
            return ValueError('User must have an email address')
        if not username: # if username is not present 
            return ValueError('User must have a username')
        user =self.model(
            email= self.normalize_email(email),  # to make the Capital letter email address to small letter (to make it case insensitive)
            username= username,
            first_name= first_name,
            last_name= last_name,
        )
        user.set_password(password)  # this is an in build function to set password 
        user.save(using=self._db) # 
        return user   # that is all there is to create a new user. 
        
        
    def create_superuser(self, first_name, last_name, email, username, password): # user lower
        user = self.create_user(  # user is created using all the variable form the detail which is present in the self.(such as first_name, last_name, email, username, password)
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        #because the created user is a super user so we are enabling all the permission true 
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)  # here we are saving user data in a default database.
        return user
    

 
 
 
 # creating a model for the account 
 
 
 
 # why do we need to create a forms.py just for the password field why cant it be created here. 
class Account(AbstractBaseUser): # here we are extending this class by inheriting from the AbstractBaseUser  # this is where we are going to store all the users information
    first_name      = models.CharField(max_length=50)  
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)
    
    # required_fields, these 6 fields are mandatory when we are creating custom user model,
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)
    
    
    # to login in using email address 
    USERNAME_FIELD = 'email'   # to set username field as email 
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = MyAccountManager() # to let the account know thar we are using the MyAccountManager to create user and superusers. 
    
    def __str(self):  # when we just return the account object inside the template, this should return the email address 
        return self.email
    
    # if the user is the admin he has the power to modify all the changes
    def has_perm(self, perm, obj=None): # must to use field when we are using a custom user model 
        return self.is_admin
    
    
    def has_module_perms(self, add_label):
        return True
    
    