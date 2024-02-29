from django.contrib import admin
from .models import Supplier, Product, RatingProduct, Client

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(RatingProduct)
admin.site.register(Client)
