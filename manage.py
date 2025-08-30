#models.py
from django.db import models
from django.contrib import admin
from .models import MenuItem

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

python manage.py makemigrations
python manage.py migrate

admin.site.register(MenuItem)
