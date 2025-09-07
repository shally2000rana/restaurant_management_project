pip install Pillow
#menu/models.py
from django.db import models
class Restaurant(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=20)
    opening_hours=models.JSONField(default=dict)

    def __str__(self):
        return self.name
json{
    "Monday":"9:00 AM - 10:00 PM",
    "Tuesday":"9:00 AM - 10:00 PM",
    "Wednesday":"9:00 AM - 10:00 PM",
    "Thursday":"9:00 AM - 10:00 PM",
    "Friday":"9:00 AM - 11:00 PM",
    "Saturday":"10:00 AM - 11:00 PM",
    "Sunday":"Closed"
}
python manage.py makemigrations
python manage.py migrate

from django.contrib import admin
from .models import Restaurant
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=("name","phone")
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
    body{font-family:Arial, sans-serif;}
    .hours{
        margin:20px 0;
        padding: 15px;
        border: 1px solid #ddd;
        border-radius:8px;
        background:#f9f9f9;
        max_width:40px;
    }
    .hours h2{margin-top:0;}
    .hours ul{list-style:none; padding:0;}
    .hours li{margin:5px 0;}
    .day{font-weight:bold;}
   </style>
</head>
<body>
   <h1>Welcome to {{restaurant.name}}</h1>
   <p>{{restaurant.address}}</p>
   <p>{{restaurant.phone}}</p>

   <div class="hours">
     <h2>Opening Hours</h2>
     <ul>
       {% for day, time in restaurant.opening_hours.items %}
         <li><span class="day">{{day}}:</span>{{time}}</li>
        {% endfor %}
     </ul>
    </div>
   
</body>
</html>
