from django.db import models
class Order(models.Model):
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Canceled','Canceled'),
    ]
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
         
