from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Product
from .serializers import ProductSerializer
from api.pagination import CustomResultsSetPagination


@api_view(['GET'])
def getProducts(request):
    data = Product.objects.all()
    paginator = CustomResultsSetPagination()
    result_page = paginator.paginate_queryset(data, request)
    serializer = ProductSerializer(result_page, data, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProduct(request, pk):
    try:
        user = Product.objects.get(id=pk)
        serializer = ProductSerializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response({"error": "Producte não existe"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def updateProduct(request, pk):
    try:
        user = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=user, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"error": "Producte não existe"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteProduct(request, pk):
    try:
        user = Product.objects.get(id=pk)
        user.delete()
        return Response({"success": "Usuário apagado com sucesso!"})
    except Product.DoesNotExist as error:
        return Response({"error": "Cliente não existe"}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({"error": "Erro desconhecido"}, status=status.HTTP)
