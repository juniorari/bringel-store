from django.urls import path
from . import views

app_name = 'product'

# CRUD Product
urlpatterns = [
    path('', views.ProductAPIList.as_view(), name='products'),
    path('create', views.addProduct, name='createproduct'),
    path('<str:pk>', views.getProduct, name='readproduct'),
    path('update/<str:pk>', views.updateProduct, name='updateproduct'),
    path('delete/<str:pk>', views.deleteProduct, name='deleteproduct'),
]
