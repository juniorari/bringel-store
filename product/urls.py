from django.urls import include, path
from . import views

app_name = 'product'

# CRUD Product
urlpatterns = [
    path('', views.getProducts, name='products'),
    path('create', views.addProduct, name='createproduct'),
    path('<str:pk>', views.getProduct, name='readproduct'),
    path('update/<str:pk>', views.updateProduct, name='updateproduct'),
    path('delete/<str:pk>', views.deleteProduct, name='deleteproduct'),
]
