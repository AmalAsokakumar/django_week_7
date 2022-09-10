from django.db import models
from category.models import category    # here w are using category as foreign key so we need to include it. 

# Create your models here.

# for further reference
# 1  _ difference b/w  auto_add_now and auto_add. 




class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=255, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to = 'photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(category, on_delete=models.CASCADE) # (model_name, what to do when we delete this category) here the entair Field will be deleted when delete this particular field. 
    created_date    = models.DateTimeField(auto_now_add =True)
    modified_date   = models.DateTimeField(auto_now =True) 
    
    def __str__(self):
        return self.product_name
    