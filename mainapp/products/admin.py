from django.contrib import admin


# Register your models here.
# Import the new model that you are working on. and register it
from .models import Product
admin.site.register(Product)
