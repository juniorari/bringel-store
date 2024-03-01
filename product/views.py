from rest_framework.decorators import api_view, authentication_classes, permission_classes  # noqa: E501
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Product, PriceHistory
from .serializers import ProductSerializer, ProductSerializerAddUpdate, PriceHistorySerializer  # noqa: E501
from bringel.pagination import CustomResultsSetPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser  # noqa: E501
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductAPIList(ListAPIView):
    """
    Get all Products
    Valid filters on parameters: name, category, sku, supplier_id
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

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


class PriceHistoryAPIList(ListAPIView):
    """
    Get all price history from a product
    """
    queryset = PriceHistory.objects.all()
    serializer_class = PriceHistorySerializer
    pagination_class = CustomResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        qs = super().get_queryset()
        qs = qs.filter(product_id=pk)
        return qs


@api_view(['GET'])
@authentication_classes([JWTAuthentication])  # correct auth class
@permission_classes([IsAuthenticated])
def getProduct(request, pk):
    try:
        data = Product.objects.get(id=pk)
        serializer = ProductSerializer(data, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "Produto não existe"},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])  # correct auth class
@permission_classes([IsAuthenticated])
def addProduct(request):
    serializer = ProductSerializerAddUpdate(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])  # correct auth class
@permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    try:
        data = Product.objects.get(id=pk)
        old_price = data.price
        serializer = ProductSerializerAddUpdate(
            instance=data, data=request.data)

        serializer.is_valid(raise_exception=True)
        new_price = request.data.get('price', '')
        serializer.save()

        if (old_price != new_price):
            PriceHistory.objects.create(
                product_id=data.id,
                old_price=old_price,
                new_price=new_price
            )

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"error": "Produto não existe"},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])  # correct auth class
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    try:
        data = Product.objects.get(id=pk)
        data.delete()
        return Response({"success": "Produto apagado com sucesso!"})
    except Product.DoesNotExist:
        return Response({"error": "Produto não existe"},
                        status=status.HTTP_404_NOT_FOUND)
    except RuntimeError:
        return Response({"error": "Erro desconhecido"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
