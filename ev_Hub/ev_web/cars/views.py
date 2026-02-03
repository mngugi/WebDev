from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests

FLASK_API = "http://127.0.0.1:5000"

def car_list(request):
    r = requests.get(f"{FLASK_API}/api/cars")
    data = r.json()
    return JsonResponse({"source": "django", "cars": data})
