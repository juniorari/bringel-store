from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from client.models import Client
from .serializers import ClientSerializer
from bringel.pagination import CustomResultsSetPagination


@api_view(['GET'])
def getClients(request):
    """
    Get all clients
    Valid filters on parameters: name, username, email, cpf
    """
    users = Client.objects.filter()
    name = request.GET.get('name')
    email = request.GET.get('email')
    username = request.GET.get('username')
    cpf = request.GET.get('cpf')
    if name:
        users = users.filter(Q(name__icontains=name))

    if email:
        users = users.filter(Q(email__icontains=email))

    if username:
        users = users.filter(Q(username__icontains=username))

    if cpf:
        users = users.filter(Q(cpf__icontains=cpf))

    paginator = CustomResultsSetPagination()
    result_page = paginator.paginate_queryset(users, request)
    serializer = ClientSerializer(result_page, many=True,
                                  context={'request': request})
    return Response(serializer.data)


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
        return Response({"success": "Usuário apagado com sucesso!"})
    except Client.DoesNotExist:
        return Response({"error": "Cliente não existe"},
                        status=status.HTTP_404_NOT_FOUND)
    except RuntimeError:
        return Response({"error": "Erro desconhecido"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
