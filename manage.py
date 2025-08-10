<!DOCTYPE html>
<html>
<head>
  <title>A bout us- My Restaurant</title>
  <style>
    body{
        font-family:Arial,sans-serif;
        background-color:#f7f7f7;
        margin:0;
        padding:0;
    }
    header{
        background-color:#333;
        color:white;
        margin:0;
        padding:0;
    }
    main{
        max-width:80px;
        margin:auto;
        background:white;
        padding:2em;
        box-shadow:0px 2px 8px rgba(0,0,0,.1);
    }
    img{
        width:100px;
        border-radius:8px;
        margin-bottom: 1em;
    }
    h1{
        text-align:center;
    }
  </style>
  <header>
  <h2> My Restaurant</h2>
  <main>
    <img src="{% static 'images/testaurant.jpg' %}" alt="Restaurant Image">
    <h1>About us</h1>
    <p>welcome to my Restaurant, where we serve delicious and freshly prepared meals with love.
      our mission is to create a cozy atmosphere where friends and families can enjoy unforgetable dining experiences.</p>
    <p>we pride ourselves on using the freshest ingredient ,sourced locally whenever possible,to bring you flavours that make every bite special.</p>
 </main>
 </body>
 </html>

<nav>
  <a href="{% url 'home' %}">Home</a>
  <a href="{% url'about' %}">About</a>
</nav>  
