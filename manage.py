from django.db import models
class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()

    def __str__(self):
        return self.name
from django.contrib import admin
from .models import Restaurant
admin.site.register(Restaurant)
python manage.py makemigrations
python manage.py migrate

from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    restaurant =Restaurant.objects.first()
    return render(request,"homepage.html",{"restaurant":restaurant})
from django.urls import path
from . import pathurlpatterns=[
    path("",views.homepage,name="homepage"),

]
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepage</title>
</head>
<body>
    <h1>Welcome to {{restaurant.name}}</h1>
    <p><strong>Address:</strong>{{restaurant.address}}</p>
</body>
</html>


  
