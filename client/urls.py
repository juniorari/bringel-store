from django.urls import path
from . import views

app_name = 'client'

# CRUD client
urlpatterns = [
    path('', views.ClientAPIList.as_view(), name='clients'),
    path('create', views.addClient, name='create_client'),
    path('list/<str:pk>', views.getClient, name='read_client'),
    path('update/<str:pk>', views.updateClient, name='update_client'),
    path('delete/<str:pk>', views.deleteClient, name='delete_client'),
]
