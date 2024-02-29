from rest_framework import serializers
from .models import Product, PriceHistory, Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer

    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'category', 'price', 'supplier')
        depth = 1


class PriceHistorySerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = PriceHistory
        fields = ('id', 'old_price', 'new_price', 'alter_date', 'product')
        depth = 2
