pip install djangorestframework

INSTALLED_APPS=[

    'rest_framework',
    'home',
  ]
from rest_framework import serializers
from .models import MenuCategory
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields=['id','name']
