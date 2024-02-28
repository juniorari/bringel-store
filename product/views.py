from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def getProducts(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data, many=True)
    return Response(serializer.data)
