from django.db import models
from .utils import calculate_discount 
class Order(models.Model):
    def calculate_total(self):
        """
        Calculate the total cost of the ordr by summing up the discounted
        price of all items.
        """
        total=0
        order_items=self.items.all()
        if not order_items.exists():
            return 0
        for item in order_items:
            original_price=item.price
            discounted_price=calculate_discount(original_price, item.discounts)
            total+=discounted_price
            return round(total,2)
class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discount=models.JSONField(default=dict)
         
