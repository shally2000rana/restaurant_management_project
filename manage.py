from django.db import models

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='menu_images/',blank=True, null=True)

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
    path('menu/',view.menu_view, name='menu'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    items=MenuItem.objects.all()
    return render(request, 'menu.html',{'items':items})

