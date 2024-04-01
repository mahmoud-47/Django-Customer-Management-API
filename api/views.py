from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientSerializer
from .models import Client

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/clients/',
            'method':'GET',
            'body':None,
            'description':'Liste des clients'
        },
        {
            'Endpoint':'/create/',
            'method':'POST',
            'body':{"body":""},
            'description':'Ajouter un client'
        },
        {
            'Endpoint':'/update/id',
            'method':'PUT',
            'body':{"body":""},
            'description':'Mettre a jour un client'
        },
        {
            'Endpoint':'/delete/id',
            'method':'DELETE',
            'body':{"body":""},
            'description':'Supprimer un client'
        },
        
    ]
    return Response(routes)

@api_view(['GET'])
def getClients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addClient(request):
    data = request.data
    client = Client.objects.create(
        nom = data['nom'],
        email = data['email'],
        phone = data['phone']
    )
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateClient(request, id):
    client = Client.objects.get(id=id)
    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return Response('Client supprimé')