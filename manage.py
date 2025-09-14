RESTAURANT_PHONE="+91 98765 43210"
from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'phone':settings.RESTAURANT_PHONE})

<div class="contact-info">
   <strong>Call Us:</strong>{{phone}}
</div>

