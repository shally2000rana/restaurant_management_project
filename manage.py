from django.db import models
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    is_daily_special=models.BooleanField(default=False)
    def __str__(self):
        return self.name

from rest_framework import serializers
from .models import MenuItem
class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['id','name','price','is_daily_special']

from rest_framework import generics
from .models import MenuItem
from .serializers import DailySpecialSerializer
class DailySpecialSerializer(generics.ListAPIView):
    """
    API view to list all menu items designated as daily specials.
    """
    queryset=MenuItem.objects.filter(is_daily_special=True)
    serializer_class=DailySpecialSerializer
         
