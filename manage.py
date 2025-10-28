from django.db import models
from django.db.models import Count
class MenuItemManager(models.Manager):
    def get_top_selling_items(self, num_items=5):
        return self.annotate(order_count=Count('orderitem'))\
                   .order_by('order_count')[:num_items]

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    objects=MenuItemManager()
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item=models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orderitem')
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity})"
        
         
