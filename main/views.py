from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Crypto
from rest_framework import viewsets, serializers
import requests


# Create your views here.

def Home(request):
	return render(request, 'main/home.html')

class CryptoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Crypto
		fields = ('cmc_rank', 'name', 'symbol', 'circulatingSupply', 'priceInUSD', 'timeStamp')

class CryptoViewSet(viewsets.ModelViewSet):
	queryset = Crypto.objects.all()
	serialize_class = CryptoSerializer
