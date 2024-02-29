from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from bringel.pagination import CustomResultsSetPagination


class ProductAPIList(ListAPIView):
    """
    Get all Products
    Valid filters on parameters: name, category, sku, supplier_id
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        qs = super().get_queryset()

        name = self.request.query_params.get('name', '')
        sku = self.request.query_params.get('sku', '')
        category = self.request.query_params.get('category', '')
        supplier_id = self.request.query_params.get('supplier_id', '')

        if (name != ''):
            qs = qs.filter(name__icontains=name)
        if (sku != ''):
            qs = qs.filter(sku__icontains=sku)
        if (category != ''):
            qs = qs.filter(category__icontains=category)
        if (supplier_id != '' and supplier_id.isnumeric()):
            qs = qs.filter(supplier_id=supplier_id)

        return qs


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
        return Response({"success": "Produto apagado com sucesso!"})
    except Product.DoesNotExist:
        return Response({"error": "Produto não existe"},
                        status=status.HTTP_404_NOT_FOUND)
    except RuntimeError:
        return Response({"error": "Erro desconhecido"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
