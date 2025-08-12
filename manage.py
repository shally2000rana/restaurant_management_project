from django.db import models
class RestaurantInfo(models.Model):
     name=models.CharField(max_length=255)
     phone_number=models.CharField(max_length=20)

     def __str__(self):
        retrun self.name
from django.shortcuts import render
from .models import RestaurantInfo

def home(request):
    restaurant=RestaurantInfo.objects.first()
    context={
        'restaurant_name':restaurant.name if restaurant else 'Our Restaurant',
        'restaurant_phone':restaurant.phone_number if restaurant else 'not available'
           }
           retrun render(request,'home.html',context)
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <Meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{restaurant name}}</title>
  <style>
    body{
        font-family:'Segoe UI',Tahoma, Geneva, Verdana,sans-serif;
        background-color:#f8f9fa;
        margin:0;
        padding:0;
    }
    header{
        background-color:#ff5733;
        text-align:center;
        padding:20px 0;
        color: white;
        font-size:28px;
        letter-spacing:1px;
        
    }
    .container{
       max-width:800px;
       margin:50px auto;
       background:white;
       padding: 30px;
       border-radius:8px;
       box-shadow:0px 4px 10px rgba(0,0,0,0.1);
       text-align:center;

    }
    h1{
       color:#333;
       font-size:36px;
       margin-nottom:10px;    
    }
    p{
        color:#666;
        font-size:18px;
        line-height:1.6;
    }
    footer{
        text-align:center;
        background-color:#ff5733;
        color:white;
        padding:15px 0;
        margin-top:50px;

    }
    
  </style>
   
</head>
<body>
  <header>
  {{restaurant_name}}
  </header>

 <div class="container">
  <h1>welcome to {{restaurant_name}}!</h1>
  <p>we are happy to serve you the best food in town.
  Enjoy our delicious menu and cozy atmosphere</p>
  <div class="phone">{{restaurant_phone}}</div>
 </div>
 <footer>
    &copy; 2025{{restaurant_name}}.All rights reserved.
 </footer>
</body>
</html>

 
