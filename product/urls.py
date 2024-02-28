from django.urls import include, path
from . import views

app_name = 'product'

# CRUD Product
urlpatterns = [
    path('', views.getProducts),
    # path('create', views.addProduct),
    # path('read/<str:pk>', views.getProduct),
    # path('update/<str:pk>', views.updateProduct),
    # path('delete/<str:pk>', views.deleteProduct),
]
