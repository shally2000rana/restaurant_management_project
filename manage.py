from django.db import models
from decimal import Decimal
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
class Order(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
    def calculate_total(self):
        total=Decimal('0.00')
        for item in self.orderitem_set.all():
            total+=item.price*item.quantity
        return total
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x{self.menu_item.name}"

def calculate_total(self):
    total=Decimal('0.00')
    for item in self.orderitem_set.all():
        total+=item.price*item.quantity
    return total

from django.test import TestCase
from .models import Order, OrderItem, MenuItem
from decimal import Decimal
class OrderModelTest(TestCase):
    def test_calculate_total(self):
        order=Order.objects.create()
        pizza=MenuItem.objects.create(name="Pizza", price=Decimal("12.50"))
        burger=MenuItem.objects.create(name="Burger",price=Decimal("8.00"))