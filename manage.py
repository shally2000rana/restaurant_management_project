import random
from django.db import models

class DailySpecial(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)

    @staticmethod
    def get_random_special():
        specials=list(DailySpecial.objects.all())
        if not specials:
            return None
        return random.choice(specials)
    
    def __str__(self):
        return self.name
        
         
