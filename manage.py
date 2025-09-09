#models.py
from django.db import models

class Restaurant(model.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone_number=models.CharField(max_length=15)
    opening_hours=models.TextField()
    logo=models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.name

import os
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

urlpatterns=[
    path('',views.homepage, name='homepage'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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

