from django.db import models

class PaymentMethod(models.Model):
    name=models.CharField(max_length=50, unique=True)
    decsription=models.TextField(blank=True, null=True)
    is_active=models.BooleanField(default=True)

    def__str__(self):
        return self.name
        
        
         
