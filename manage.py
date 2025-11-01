from django.db import models

class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField()
    has_delivery=models.BooleanField(default=False)
    def__str__(self):
        return self.name
        
         
