from django.db import models

class MenuItem(models.Model):
  name=models.CharField(max_length=200)
  description=models.TextField(blank=True, null=True)
  price=models.DecimalField(max-max_digits=6, decimal_places=2)

  def__str__(self):
    return self.name

from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer
