from django.db import models

class RestaurantLocation(models.Model):
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length20)

    def __str__(self):
        return f"{self.address},{self.city},{self.state} _{self.zip_code}"


  
