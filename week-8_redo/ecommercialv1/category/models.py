from django.db import models
from django.urls import reverse 
import uuid
# things to learn from here 
# what is slug and how to use it properly.
# details of meta class 


# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField( unique=True, default= uuid.uuid1) #should be the url of the category and it should be unique, this field should be auto generated because we use SlugField for this slug, to properly use this feature we need to configure the admin.py file 
    description = models.TextField(max_length=255, blank=True) # blank= True means this field is optional, which can be empty. 
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True) # this should be the location where the photos will be uploaded into.
    offer_status = models.BooleanField(default=False)
    
    # used to fix the typo error in admin page.
    class Meta:   # with the meta class we are editing the category name and other things. 
        #  db_table = 'category'
         verbose_name = 'category'
         verbose_name_plural = 'categories'  # to fix the name which is give in the admin dashboard 
    
    # with this function we can bring back the url of a particular category 
    # def get_url(self):
        # return reverse('products_by_category', args=[self.slug])# here we will mention the name of <slug:category_slug> in Stor urls.py file, we are also passing slug in list as arguments 
    
    # creating string way representation of the model ?
    def __str__(self):
        return self.category_name
    