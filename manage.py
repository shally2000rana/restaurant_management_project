!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Restaurant{% endblock %}</title>
    <style>
      body{
        font-family:Arial, sans-serif;
        margin:0;
        padding:0;
        min-height:100vh;
        display:fkex;
        felx-direction:column;
      }
      main{
        background-color:#333;
        color:#fff;
        text-align: center;
        padding: 15px 0;
        margin-top: auto;
      }
      .footer-hours{
        font-size:14px;
        margin-top:5px;
        color:#add;
      }
    </style>

</head>
<body>
    <main>
      {% block content %}{% endblock %}
    </main>

    <footer>
    <p>|| Our Restaurant - All Rights Reserved &copy; 2025</p>
    <p class="footer-hours">Mon-Fri: 11am-9pm, Sat-Sun: 10am-10pm</p>
    </footer>

</body>
</html>   


 
