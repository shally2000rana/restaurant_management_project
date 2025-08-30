#settings.py
RESTAURANT_NAME="Tasty Bites"
#views.py
from django.conf import settings
from django.shortcuts import render
from django.urls import path
from . import views

def home(request):
    restaurant_name=settings.RESTAURANT_NAME
    return render(request,"home.html", {"rrestaurant_name": restaurant_name})

urlpatterns=[
    path('', views.home, name='home').
]

<!DOCTYPE html>
<html>
<head>
    <title>{{restaurant_name}}</title>
</head>
<body>
    <h1>Welcome to {{restaurant_name}}</h1>
</body>
</html>
 
