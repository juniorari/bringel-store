from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def welcome(request):
    content = {"message": "Bem vindo à Bringel Store!"}
    return JsonResponse(content)


def error(request):
    content = {"error": "Rota inválida!"}
    return JsonResponse(content)
