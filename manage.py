<!DOCTYPE html>
<html>
<head>
   <title>Restaurant Homepage</title>
   <style>
     .logo{
        display:block;
        margin:20px auto;
        max-width:200px;
        height:auto;
     }
     body{
        font-family:Arial, sans-serif;
        padding: 20px;
        text-align:center;
     }
     .search-container{
        margin: 20px auto;
        max-width:400px;
     }
     input[type="text"]{
        width:70%;
        padding:10px;
        border-radius:8px;
        border:1px solid #ccc;
        font-size:16px;
     }
     button{
        padding:10px 15px;
        border-radius:8px;
        border:none;
        background-color:#28a745;
        color:white;
        font-size:16px;
        cursor:pointer;
     }
     button:hover{
        background-color:#218838;
     }
   </style>
</head>
<body>
    <header>
        <img src="{% static 'images/restaurant_logo.png' %}" alt="Restaurant Logo" class="logo">
    </header>
    <h1>welcome to our restaurant </h1>

    <div class="search-container">
      <form method="GET" action="">
         <input type="text" name="q" placeholder="Search menu items...">
         <button type="submit">Search</button>
      </form>
    </div>
</body>
</html>


 
