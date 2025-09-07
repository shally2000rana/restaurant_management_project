from django.db import models
class Restaurant(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.name

python manage.py makemigrations
python manage.py migrate

from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    Restaurant=Restaurant.objects.first()
    return render(request, "restaurant/homepage.html",{"restaurant": restaurant})
<!DOCTYPE html>
<html>
<head>
   <title>{{restaurant.name}}</title>
   <style>
    body{font-family:Arial, sans-serif; padding:20px;}
    .address-box{
        margin:20px 0;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius:8px;
        background:#f9f9f9;
        max_width:400px;
    }
   
   </style>
</head>
<body>
   <h1>Welcome to {{restaurant.name}}</h1>
   <p>{{restaurant.address}}</p>
   <p>{{restaurant.phone}}</p>

   <div class="address-box">
     <h2>Our Address</h2>
     <p>{{restaurant.address}}</p>
    </div>
   
</body>
</html>
