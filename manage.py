from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Cancelled','Cancelled'),
        ('Completed','Completed'),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product=models.CharField(max_length=200)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user','product','status','created_at']

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    @action(detail=True, methods=['delete'])
    def cancel(self, request, pk=None):
        try:
            order=Order.objects.get(pk=pk, user=request.user)
        except Order.DoesNotExist:
            return Response({"error":"Order not found or not yours."}, status=status.HTTP_404_NOT_FOUND)
        if order.status=='Cancelled':
            return Response({"message":"Order already cancelled."}, status=status.HTTP_404_BAD_REQUEST)
        if order.status=='Completed':
            return Response({"message":"Completed orders cannot be cancelled."}, status=status.HTTP_404_BAD_REQUEST)
        orders.status='Cancelled'
        order.save()
        return Response({"message":"Order cancelled successfully."}, status=status.HTTP_200_OK)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router=DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns=[
    path('', include(router.urls)),
]
