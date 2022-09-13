from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DonationsSerializer, OrganizationSerializer
from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse("Global Disaster Fund home")


def about(request):
    return HttpResponse("This is the About page")


@api_view(['POST'])
def apply_for_funding(request):
    if request.method == 'POST':
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Apply for funding page")


@api_view(['POST'])
def donate(request):
    if request.method == 'POST':
        serializer = DonationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Make a donation page")


@api_view(['GET'])
def resources(request):
    response = requests.get("https://api.reliefweb.int/v1/sources?appname=apidoc&limit=80")
    relief_resources = response.json()["data"]
    return HttpResponse("Disaster relief resources")
