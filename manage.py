
from django.db import models

class Ingredient(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    ingredients=models.ManyToManyField(Ingredient, related_name='menu_items')

    def __str__(self):
        return self.name

from rest_framework import serializers
from .models import MenuItem, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['id','name']

class MenuItemSerializer(serializers.ModelSerializer):
    ingredients=IngredientSerializer(many=True, read_only=True)

    class Meta:
        model=MenuItem
        fields=['id','name','ingredients']

from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .models import MenuItem
from .serializers import IngredientSerializer

class MenuItemSerializer(APIView):
    def get(self, request, pk):
        try:
            menu_items=MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)

        ingredients=menu_items.ingredients.all()
        serializer= IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

from django.urls import path
from .views import MenuItemIngredientsView

urlpatterns=[
    path('api/menu-items/<int:pk>/ingredients/', MenuItemIngredientsView.as_view(), name='menuitem-ingredients'),
]
         
