from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
from product.models import RatingProduct
from bringel.pagination import CustomResultsSetPagination


class ClientAPIList(ListAPIView):
    """
    Get all clients
    Valid filters on parameters: name, username, email, cpf
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        qs = super().get_queryset()

        name = self.request.query_params.get('name', '')
        email = self.request.query_params.get('email', '')
        username = self.request.query_params.get('username', '')
        cpf = self.request.query_params.get('cpf', '')

        if (name != ''):
            qs = qs.filter(name__icontains=name)
        if (email != ''):
            qs = qs.filter(email__icontains=email)
        if (username != ''):
            qs = qs.filter(username__icontains=username)
        if (cpf != ''):
            qs = qs.filter(cpf__icontains=cpf)

        return qs


@api_view(['GET'])
def getClient(request, pk):
    try:
        user = Client.objects.get(id=pk)
        serializer = ClientSerializer(user, many=False)
        return Response(serializer.data)
    except Client.DoesNotExist:
        return Response({"error": "Cliente não existe"},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addClient(request):
    serializer = ClientSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def updateClient(request, pk):
    try:
        user = Client.objects.get(id=pk)
        serializer = ClientSerializer(instance=user, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Client.DoesNotExist:
        return Response({"error": "Cliente não existe"},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteClient(request, pk):
    try:
        user = Client.objects.get(id=pk)
        user.delete()
        return Response({"success": "Cliente apagado com sucesso!"})
    except Client.DoesNotExist:
        return Response({"error": "Cliente não existe"},
                        status=status.HTTP_404_NOT_FOUND)
    except RuntimeError:
        return Response({"error": "Erro desconhecido"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def sugestionClient(request, pk):
    """
    Algoritmo de Recomendações:
    Gera uma lista com no máximo 10 produtos, baseados nas sugestões
    de produtos feitas pelo Cliente.
    1 - Seleciona as 5 categorias que o cliente mais fez avaliações
    2 - Dessas categorias, faz uma busca randomica de produtos
    """
    try:
        user = Client.objects.get(id=pk)

        sql = f' \
            SELECT * FROM product_product \
            WHERE category IN ( \
                SELECT category \
                FROM product_ratingproduct pr \
                JOIN product_product pp ON pp.id = pr.product_id \
                WHERE client_id = {user.id} \
                GROUP BY category, rating \
                ORDER BY rating desc LIMIT 5 \
            ) \
            ORDER BY random() LIMIT 10'

        qs = RatingProduct.objects.raw(sql)[:10]

        print(f'PK => {pk}')

        lista = []
        for p in qs:
            lista.append(
                {"id": p.id, "product": p.name, "category": p.category})

        return Response({"data": lista})

    except Client.DoesNotExist:
        return Response({"error": "Cliente não existe"},
                        status=status.HTTP_404_NOT_FOUND)
    except RuntimeError:
        return Response({"error": "Erro desconhecido"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
