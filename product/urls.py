from django.urls import path
from . import views
from rating.views import RatingProductAPIList, addRating

app_name = 'product'

# CRUD Product
urlpatterns = [
    path('', views.ProductAPIList.as_view(), name='products'),
    path('price-history/<int:pk>', views.PriceHistoryAPIList.as_view(),
         name='history_price_product'),
    path('create', views.addProduct, name='create_product'),
    path('list/<int:pk>', views.getProduct, name='read_product'),
    path('update/<int:pk>', views.updateProduct, name='update_product'),
    path('delete/<int:pk>', views.deleteProduct, name='delete_product'),
]

# Rating Products
urlpatterns += [
    path('rating/list/<int:pk>', RatingProductAPIList.as_view(),
         name='rating_product'),
    path('rating/create', addRating, name='rating_create'),
]

# Suppliers
# urlpatterns += [
#     path('rating/list/<int:pk>', RatingProductAPIList.as_view(),
#          name='rating_product'),
#     path('rating/create', addRating, name='rating_create'),
# ]
