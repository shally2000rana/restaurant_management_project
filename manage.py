from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_deleye=models.CASCADE, releated_name="profile")
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name or self.user.username


 
