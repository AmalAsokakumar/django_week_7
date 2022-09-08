from distutils.command.upload import upload
from turtle import update
from django.db import models

# things to learn from here 
# what is slug and how to use it properly.
# details of meta class 


# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True) #should be the url of the category and it should be unique, this field should be auto generated because we use SlugField for this slug, to properly use this feature we need to configure the admin.py file 
    description = models.TextField(max_length=255, blank=True) # blank= True means this field is optional, which can be empty. 
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) # this should be the location where the photos will be uploaded into.
    
    # used to fix the typo error in admin page.
    class Meta:   # with the meta class we are editing the category name and other things. 
         verbose_name = 'category'
         verbose_name_plural = 'categories'  # to fix the name which is give in the admin dashboard 
    # creating string way representation of the model ?
    def __str__(self):
        return self.category_name
    