from django.db import models
from django.shortcuts import render
from .models import MenuItem


class MenuItem(models.Model):
    name=models.CharField(max_length)
    description=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

def menu_view(request):
    items=MenuItem.objects.all()
    return render(request, 'menu.html', {'items':items})
  
