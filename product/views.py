from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer
from bringel.pagination import CustomResultsSetPagination


@api_view(['GET'])
def getProducts(request):
    """
    Get all Products
    Valid filters on parameters: name, sku, category, supplier_id
    """
    data = Product.objects.filter()
    name = request.GET.get('name')
    sku = request.GET.get('sku')
    category = request.GET.get('category')
    supplier_id = request.GET.get('supplier_id')
    if name:
        data = data.filter(Q(name__icontains=name))

    if sku:
        data = data.filter(Q(sku__icontains=sku))

    if category:
        data = data.filter(Q(category__icontains=category))

    if supplier_id and supplier_id.isnumeric():
        data = data.filter(supplier_id=supplier_id)

    paginator = CustomResultsSetPagination()
    result_page = paginator.paginate_queryset(data, request)
    serializer = ProductSerializer(
        result_page, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    try:
        user = Product.objects.get(id=pk)
        serializer = ProductSerializer(user, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "Producte não existe"},
                        status=status.HTTP_404_NOT_FOUND)


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
    except Product.DoesNotExist:
        return Response({"error": "Producte não existe"},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteProduct(request, pk):
    try:
        user = Product.objects.get(id=pk)
        user.delete()
        return Response({"success": "Usuário apagado com sucesso!"})
    except Product.DoesNotExist:
        return Response({"error": "Cliente não existe"},
                        status=status.HTTP_404_NOT_FOUND)
    except RuntimeError:
        return Response({"error": "Erro desconhecido"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
