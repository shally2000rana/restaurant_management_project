from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    order_date=models.DateTimeField(auto_now_add=True)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)

    class OrderItem(models.Model):
        order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
        product_name=models.CharField(max_length=255)
        quantity=models.IntegerField()
        price=models.DecimalField(max_digits=10, decimal_places=2)

from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['product_name','quantity','price']
class OrderSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model=Order
        fields=['id','order_date','total_price','items']