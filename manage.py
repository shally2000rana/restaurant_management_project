<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Restaurant Menu</title>
  <style>
     body{
       font-family:Aria, sans-serif;
       margin:30px;
       background-color:#f9f9f9;
       }
     h1{
       display:grid;
       grid-template-column:repeat(auto-fill, mimmax(220px, 1fr));
       gap:20px;
       margin-top:20px;
       }
     .menu-item{
       background:white;
       padding:15px;
       border-radius:10px;
       box-shadow:0 2px 6px rgba(0,0,0,0.1);
       }
     .menu-item h3{
       margin:0 0 8px;
       color:#444;
       }
     .menu-item p{
       margin:5px 0;
      font-size:14px;
      color:#666;
       }
     .price{
      font-weight:bold;
      color:#e67e22;
       }
 </style>
</head>
<body>
   <h1>Our Menu</h1>

   <div class="menu">
      {% for item in menu_items %}
        <div class="menu-item">
          <h3>{{ item.name}}</h3>
          <p>{{item.description}}</p>
          <p class="price">${{item.price}}</p>
        </div>
      {% empty %}
          <p>No menu items available right now.</p>
      {% endfor %}
    </div>
</body>
</html>  


 
