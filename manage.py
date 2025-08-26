from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
    ]

    customer=models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    total_amount=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    menu_item=models.ForeignKey("Menu", on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"
    
    def get_total_price(self):
        retrun self.menu_item.price *self.quantity

 
