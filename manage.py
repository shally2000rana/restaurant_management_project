from djngo.db import models
class ActiveOrderManager(models.Manager):
    """
    Manager that returns only orders with a 
    status of 'pending' or 'processing'.
    """
    def get_active_orders(self):
        """
        Returns a QuerySet of active orders.
        """
        return self.get_queryset().filter(
            status_in=['pending','processing']
        )
class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('processing','Processing'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    ]
status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

