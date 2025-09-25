from django.db import models

class MenuItem(models.Model):
  name=models.CharField(max_length=100)
  description=models.TextField(blank=True, null=True)
  price=models.DecimalField(max_digits=6, decimal_places=2)
  available=models.BooleanField(default=True)

  def__str__(self):
    return self.name

from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields="__all__"

        def validate_price(self, value):
            if value <=0:
                raise serializers.ValidateError("Price must be a positive number.")
            return value

from rest_framework import status, generics
from rest_framework.response import response
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemUpdateView(generics.UpdateAPIView):
    queryset=MenuItem.Objects.all()
    serializer_class=MenuItemSerializer

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

from django.urls import path
from .views import MenuItemUpdateView

urlpatterns=[
    path("menu/<int:pk>/update/", MenuItemUpdateView.as_view(), name="menu-update"),
]
