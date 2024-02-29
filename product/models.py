from django.db import models
from utils.faker_ecommerce import ProviderEcommerce
from client.models import Client


class Supplier(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=250, blank=True)
    sku = models.CharField(max_length=10, blank=True)
    category = models.CharField(
        max_length=50, choices=ProviderEcommerce.categories())
    price = models.FloatField(default=0.0, blank=True)
    supplier = models.ForeignKey(
        "Supplier", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.sku} - {self.name}'


class RatingProduct(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(
        Client, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} - {self.client.name}'

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'


class PriceHistory(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True)
    old_price = models.FloatField(default=0.0)
    new_price = models.FloatField(default=0.0)
    alter_date = models.DateTimeField(auto_now_add=True)
