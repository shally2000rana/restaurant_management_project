from django.db import models

class MenuCategory(models.Model):
    name=models.CharField(max_length=100, unique=True)
    decsription=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields='__all__'
        
        
         
