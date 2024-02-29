from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=250, blank=True,
                            verbose_name='Nome Completo')
    username = models.CharField(max_length=250, unique=True,
                                blank=True, verbose_name='Usuário')
    email = models.CharField(max_length=250, blank=True, unique=True)
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    password = models.CharField(max_length=150, verbose_name='Senha')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.name}'
