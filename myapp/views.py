from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.
def home(request):
    context = {
        "first_name": "Naynesh",
        "middle_name": "Raghunath",
        "last_name": "Rathod",
    }
    # return  HttpResponse(data)
    return render(request, 'index.html', context=context)
import requests

def index(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'index.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer

class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
