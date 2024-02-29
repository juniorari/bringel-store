from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from client.models import Client
from product.models import RatingProduct, Product
from product.serializers import RatingProductSerializer  # noqa: E501
from bringel.pagination import CustomResultsSetPagination
from django.http import JsonResponse


class RatingProductAPIList(ListAPIView):
    """
    Get all price history from a product
    """
    queryset = RatingProduct.objects.all()
    serializer_class = RatingProductSerializer
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        qs = super().get_queryset()
        qs = qs.filter(product_id=pk)
        return qs


@api_view(['POST'])
def addRating(request):

    client = request.data.get('client_id', '')
    if (client == '' or not client.isnumeric()):
        return JsonResponse({'detail': 'O cliente deve ser válido'}, status=400)  # noqa: E501

    product = request.data.get('product_id', '')
    if (product == '' or not client.isnumeric()):
        return JsonResponse({'detail': 'O Produto deve ser válido'}, status=400)  # noqa: E501

    rating = request.data.get('rating', '')
    if (rating == '' or not rating.isnumeric()):
        return JsonResponse({'detail': 'O valor de rating informado é inválido'}, status=400)  # noqa: E501

    if (0 < int(rating) > 5):
        return JsonResponse({'detail': 'O valor de rating deve ser entre 0 e 5'}, status=400)  # noqa: E501

    client = get_object_or_404(Client, pk=client)
    product = get_object_or_404(Product, pk=product)

    RatingProduct.objects.create(
        product_id=product.id,
        client_id=client.id,
        rating=rating
    )

    return JsonResponse({'data': 'Registro incluído com sucesso'}, status=status.HTTP_201_CREATED)  # noqa: E501
