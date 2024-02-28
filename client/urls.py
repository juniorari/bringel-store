from django.urls import include, path
from . import views

app_name = 'client'

# CRUD client
urlpatterns = [
    path('', views.getClients, name='clients'),
    path('create', views.addClient, name='createclients'),
    path('read/<str:pk>', views.getClient, name='getclients'),
    path('update/<str:pk>', views.updateClient, name='updateclients'),
    path('delete/<str:pk>', views.deleteClient, name='deleteclients'),
]
