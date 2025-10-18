from django.db import models
class MenuCategory(models.Model):
    name=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
from rest_framework import serializers
from .models import MenuCategory
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields='__all__'
from rest_framework import viewsets
from .models import MenuCategory
from .serializers import MenuCategorySerializer
class MenuCategorySerializer(viewsets.ModelViewSet):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet
router=DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet)
urlpatterns=[
    path('', include(router.urls))
]
         
