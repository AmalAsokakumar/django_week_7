#we should add this context_processor in settings.py templates section.
# we should modify the templates to accept the context_processors

# we are going to list out all our categories using a context preprocessor, through we can easily move between different categories 
# this should be created in a file called context_processor.py in category app.  in here this file will be a simple python function.  


# this python function takes a request as an argument and returns a dictionary of data 
from .models import category

def menu_links(request):
    
    links = category.objects.all() # first we fetch all the categories form the category app as a 'list'.
    return dict(links=links) # here we are returning the links as a dictionary 
    