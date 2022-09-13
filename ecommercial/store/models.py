from django.db import models
from category.models import category    # here w are using category as foreign key so we need to include it. 
from django.urls import reverse 
# from brand.models import brand 
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
    # brand           = models.ForeignKey(brand, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add =True)
    modified_date   = models.DateTimeField(auto_now =True) 
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])# here we have 2 arguments product slugs and categories slug. here self means this product and category is mentioned above and slug is from  category app ( we can access them because these fields are interconnected with : foreignkey . )   and second slug is this products slug.
    def __str__(self):
        return self.product_name
    