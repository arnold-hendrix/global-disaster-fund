import os.path

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DonationsSerializer, OrganizationSerializer
from django.http import HttpResponse
import requests
import datetime
# from globaldisasterfund.settings import api_key


def index(request):
    return HttpResponse("Global Disaster Fund home")


def about(request):
    return HttpResponse("This is the About page")


@api_view(['GET', 'POST'])
def apply_for_funding(request):
    if request.method == 'GET':
        return HttpResponse("Apply for funding page")
    elif request.method == 'POST':
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def donate(request):
    if request.method == 'GET':
        return HttpResponse("Make a donation page")
    elif request.method == 'POST':
        serializer = DonationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def resources(request):
    response = requests.get("https://api.reliefweb.int/v1/sources?appname=apidoc&limit=80")
    relief_resources = response.json()["data"]
    return Response(relief_resources)


@api_view(['GET'])
def climate_news(request):
    base_url = "https://newsapi.org/v2/everything"
    api_key = "91ebd4279b9b42b08c38d4d9b6f6ba58"
    url_params = {
        "q": "climate",
        "from": datetime.date.today(),
        "sortBy": "popularity",
        "apiKey": api_key
    }
    response = requests.get(base_url, params=url_params)
    news = response.json()["articles"]
    return Response(news)
