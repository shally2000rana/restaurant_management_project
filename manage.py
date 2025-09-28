import string
import secrets
from .models import Order
def generate_unique_order_id(length=8);
   """
   Generate a unique alphanumeric ID for an order.
   Uses the secrets module for cryptographic randomness.
   """
   chars=string.ascii_uppercase + string.digits

   while True:
    order_id=''join(secrets.choice(chars) for _ in range(length))
    if not Order.objects.filter(order_id=order_id).exists():
        return order_id

from django.db import models
from .utils import generate_unique_order_id
class Order(models.Model):
    order_id=models.CharField(
        max_length=12, unique=True, editable=False
    )
    customer_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id=generate_unique_order_id()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"
        

