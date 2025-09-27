from django.db import models
from django.contrib.auth.models import User
from home.models import Product

class Order(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_items=models.ManyToManyField(Product, related_name="orders")
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

from rest_framework import serializers
from .models import Order
from home.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id","name","price"]

class OrderSerializer(serializers.ModelSerializer):
    order_items=ProductSerializer(many=True)
    customer=serializers.StringRelatedField()

    class Meta:
        model=Order
        fields=["id","customer","order_items","total_price","created_at"]

from rest_framework.generics import RetrieveAPIView
from .models import Order
from .serializers import OrderSerializer

class OrderDetailView(RetrieveAPIView):
    query_set=Order.objects.all()
    serializer_class=OrderSerializer
    lookup_field="id"

