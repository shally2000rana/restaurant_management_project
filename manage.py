pip install Pillow
#menu/models.py
from django.db import models
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price-models.DecimalField(max_length=6, decimal_places=2)
    image=models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name

import os
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

from django.conf import settings
from django.conf.urls.static import static
urlpattens=[

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

python manage.py makemigrations
python manage.py migrate

from django.contrib import admin
from .models import MenuItem
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display=('name','price')
<!DOCTYPE html>
<html>
<head>
   <title>Menu</title>
</head>
<body> 
   <h1>Our Menu</h1>
   <ul>
    {% for item in menu_items %}
     <li>
      {% for item in menu_items %}
       <img src="{{item.image.url}}" alt="{{item.name}}" style="width:150px; height:auto; border-radius:8px;">
      {% endif %}
      <h2>{{item.name}}</h2>
      <p>{{item.description}}</p>
      <p><strong>{{item.price}}</strong></p>
     </li>
    {% endfor %}
   </ul>
</body>
</html>
