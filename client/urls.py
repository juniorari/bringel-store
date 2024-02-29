from django.urls import path
from . import views

app_name = 'client'

# CRUD client
urlpatterns = [
    path('', views.ClientAPIList.as_view(), name='clients'),
    path('create', views.addClient, name='createclient'),
    path('<str:pk>', views.getClient, name='readclient'),
    path('update/<str:pk>', views.updateClient, name='updateclient'),
    path('delete/<str:pk>', views.deleteClient, name='deleteclient'),
]
