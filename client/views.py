from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Client
from .serializers import ClientSerializer
from api.pagination import CustomResultsSetPagination


@api_view(['GET'])
def getClients(request):
    users = Client.objects.all()
    paginator = CustomResultsSetPagination()
    result_page = paginator.paginate_queryset(users, request)
    serializer = ClientSerializer(result_page, many=True, context={'request':request})
    return Response(serializer.data)

    
@api_view(['GET'])
def getClient(request, pk):
    try:
        user = Client.objects.get(id=pk)
        serializer = ClientSerializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response({"error": "Cliente não existe"}, status=status.HTTP_404_NOT_FOUND)


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
    except:
        return Response({"error": "Cliente não existe"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteClient(request, pk):
    try:
        user = Client.objects.get(id=pk)
        user.delete()
        return Response({"success": "Usuário apagado com sucesso!"})
    except Client.DoesNotExist as error:
        return Response({"error": "Cliente não existe"}, status=status.HTTP_404_NOT_FOUND)
    except:
        print('NameError, ImportError')
        return Response({"error": "Erro desconhecido"}, status=status.HTTP)
