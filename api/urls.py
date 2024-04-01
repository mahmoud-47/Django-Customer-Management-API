from django.urls import path
from . import views 
urlpatterns = [
    path('',views.getRoutes, name="getRoutes"),
    path('clients/', views.getClients, name="getClients"),
    path('create/', views.addClient, name="addClient"),
    path('update/<int:id>', views.updateClient, name="updateClient"),
    path('delete/<int:id>', views.deleteClient, name="deleteClient"),
]
