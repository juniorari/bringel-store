from django.db import models
# from utils.faker_ecommerce import ProviderEcommerce


# class Supplier(models.Model):
#     name = models.CharField(max_length=250)
#     email = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)

#     class Meta:
#         verbose_name = 'Fornecedor'
#         verbose_name_plural = 'Fornecedores'

#     def __str__(self):
#         return f'{self.name}'


# class Product(models.Model):
#     name = models.CharField(max_length=250)
#     sku = models.CharField(max_length=10)
#     category = models.CharField(max_length=50,
# choices=ProviderEcommerce.categories())
#     price = models.FloatField(default=0.0)
#     supplier = models.ForeignKey(
#         "Supplier", on_delete=models.SET_NULL, null=True)

#     class Meta:
#         verbose_name = 'Produto'
#         verbose_name_plural = 'Produtos'

#     def __str__(self):
#         return f'{self.sku} - {self.name}'


# class RatingProduct(models.Model):
#     product = models.ForeignKey(
#         "Product", on_delete=models.SET_NULL, null=True)
#     client = models.ForeignKey(
#         "Client", on_delete=models.SET_NULL, null=True)
#     rating = models.PositiveIntegerField()

#     def __str__(self):
#         return f'{self.product.name} - {self.client.name}'

#     class Meta:
#         verbose_name = 'Avaliação'
#         verbose_name_plural = 'Avaliações'


class Client(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nome Completo')
    username = models.CharField(
        max_length=250, unique=True, verbose_name='Usuário')
    email = models.CharField(max_length=250, unique=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    password = models.CharField(max_length=150, verbose_name='Senha')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.name}'
