# Generated by Django 5.0.2 on 2024-02-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(blank=True, max_length=250, unique=True, verbose_name='Usuário'),
        ),
    ]
