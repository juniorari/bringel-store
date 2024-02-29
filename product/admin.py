from django.contrib import admin
from .models import Product, Supplier, RatingProduct, PriceHistory


admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(RatingProduct)
admin.site.register(PriceHistory)
