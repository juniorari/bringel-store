from rest_framework import serializers
from .models import Client
from django.contrib.auth.hashers import make_password
from utils.validacpf import valida_cpf


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'username', 'email', 'cpf',)

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(ClientSerializer, self).create(validated_data)

    def validate_cpf(self, cpf):
        if len(cpf) == 11:
            raise serializers.ValidationError("O CPF deve estar com a máscara")

        if len(cpf) != 14:
            raise serializers.ValidationError("O CPF deve ter 14 dígitos")

        if not valida_cpf(cpf):
            raise serializers.ValidationError(f'O CPF {cpf} é inválido')

        return cpf
