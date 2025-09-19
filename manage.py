from django.db import models

class OrderStatus(models.Model):
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    #your existing fields(e.g., customer, items, total, etc.)
    status=models.ForeignKey(
        OrderStatus,
        on_deleye=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

