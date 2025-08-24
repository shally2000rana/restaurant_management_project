<!DOCTYPE html>
<html>
<head>
   <title>Restaurant Homepage</title>
   <style>
    
     body{
        font-family:Arial, sans-serif;
        padding: 0;
        margin:0;
        min-height:100vh;
        display:flex;
        fex-direction:column;
     }
     main{
        flex: 1;
        padding:20px;
     }
    
  
     footer{
        padding:15px 0;
        background-color:#333;
        color:#fff;
        text-align:center;
        margin-top:auto;
     }
   </style>
</head>
<body>
    <main>
       {% block title %} Home- Restaurant{%end block %}
       {% block content %}
    </main>
    <h1>welcome to our restaurant </h1>
    <p>Delicious food, made with love.</p>
   <footer>
    <div class="search-container">
      <form method="GET" action="">
         <input type="text" name="q" placeholder="Search menu items...">
         <button type="submit">Search</button>
      </form>
    </div>
    </footer>
  {% endblock %}
</body>
</html>


 
