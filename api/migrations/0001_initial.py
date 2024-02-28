# Generated by Django 5.0.2 on 2024-02-28 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nome Completo')),
                ('username', models.CharField(max_length=250, unique=True, verbose_name='Usuário')),
                ('email', models.CharField(max_length=250, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('password', models.CharField(max_length=150, verbose_name='Senha')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('sku', models.CharField(max_length=10)),
                ('categorie', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='RatingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.client')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.supplier'),
        ),
    ]