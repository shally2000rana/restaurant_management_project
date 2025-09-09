#models.py
from django.db import models

class Restaurant(model.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    opening_hours=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

python manage.py makemigrations
python manage.py migrate

#views.py
from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    restaurant=Restaurant.objects.first()
    return render(request,'homepage.html',{'restaurant': restaurant})

<!--templates/homepage.html-->
<h1>Welcome to {{restaurant.address }}</h1>

<p><strong>Address:</strong>{{ restaurant.address }}</p>
<p><strong>Phone:</strong>{{restaurant.phone_number}}</p>
<p><strong>Opening Hours:</strong>{{restaurant.opening_hours}}</p>

