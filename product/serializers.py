from rest_framework import serializers
from .models import Product, PriceHistory, Supplier, RatingProduct
from client.models import Client


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['name', 'email', 'address']


class ProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'category', 'price', 'supplier']
        # depth = 1


class ProductSerializerAddUpdate(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'category', 'price', 'supplier']


class ProductHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'sku', 'category']


class PriceHistorySerializer(serializers.ModelSerializer):
    product = ProductHistorySerializer()

    class Meta:
        model = PriceHistory
        fields = ['old_price', 'new_price', 'alter_date', 'product']


class ClientCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['name']


class ProductCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['name']


class RatingProductSerializer(serializers.ModelSerializer):
    product = ProductCustomSerializer()
    client = ClientCustomSerializer()

    class Meta:
        model = RatingProduct
        fields = ['id', 'rating', 'product', 'client']
        depth = 2  # expande todas as FK
