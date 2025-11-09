class Restaurant(models.Model):
    name=models.CharField(max_length=150)
    address=models.TextField()
    phone=models.CharField(max_length=20)
    opening_hours=models.CharField(max_length=150) 

from rest_framework import serializers
from .models import serializers

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields="__all__"