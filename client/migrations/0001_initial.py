# Generated by Django 5.0.2 on 2024-02-29 03:54

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
    ]
