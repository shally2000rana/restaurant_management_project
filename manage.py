from django.shortcuts import render
def menu_list (request):
    menu_items=[
        {'name':'Margherita Pizza', 'price':299},
        {'name':'Veg Burger', 'price':149},
        {'name':'Pasta Alfredo','price':249}
    ]
    context={
        'menu_items':menu_items
    }
    return render(request,'menu_list.html',context)
    <!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <Meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Menu</title>
  <style>
    body{
        font-family:Arial,sans-serif;
        background-color:#f8f9fa;
        margin:0;
        padding:0;
    }
    .container{
        max-width:600px;
        margin:40px auto;
        background:#fff;
        padding:20px;
        border-radius:8px;
        box-shadow:0 4px 8px rgba(0,0,0,0.1);
        
    }
    h2{
        text-align:center;
        color:#333;
    }
    ul{
        list-style:none;
        padding:0;    
    }
    li{
        padding:10px;
        border-bottom:1px solid #ddd;
        display:flex;
        justify-content:space-between;
    }
    li:last-child{
        border-bottom:none;

    }
    .price{
        color:#555;
    }
  </style>
   
</head>
<body>
 <div class="container">
  <h2>Our Menu</h2>
  <ul>
    {% for item in menu_items %}
      <li>
        <span>{{item.name}}</span>
        <span class="price">{{item.price}}</span>
      </li>
    </ul>  
 </div>
</body>
</html>
from django.urls import path
from . import views

urlpatterns=[
    path('menu/', views.menu_list, name='menu-list'),
]

 
