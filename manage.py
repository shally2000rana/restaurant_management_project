RESTAURANT NAME="The great indian kitchen"
from django.conf import settingd
from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'restaurant_name': settings.RESTAURANT_NAME})
    
 <h1>Welcome to{{restaurant_name}}</h1>   
