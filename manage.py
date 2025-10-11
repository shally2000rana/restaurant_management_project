from django.dn import models
class OrderManager(models.Manager):
    """
    custom manager for the order model to provide common querying
    methods.
    """
    def all_pending(self):
        """
        Returns a queryset of all orders with a 'pending' status.
        """
        return self.filter(status='pending')
    def by_status(self, status_name):
        """
        returns a queryset of all orders matching a given status
        name.
        """
        return self.filter(status=status_name)
class Order(models.Model):
    STATUS_CHOICES=[
        ('pending','PENDING'),
        ('shipped','SHIPPED'),
        ('delivered','DELIVERED'),
        ('canceled','CANCELED'),
    ]
    order_data=models.DateTimeField(auto_now_add=True)
    status=models.CharFIELD(max_length=10, choices=STATUS_CHOICES, default='pending')
    cusyomer=models.ForeignKey('Customer', on_delete=models.CASCADE)
         
