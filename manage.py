<!--base.html-->
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>{% block title %}Restaurant{% endblock %}</title>
   <link rel="stylesheet" href="{% static 'css/styles.css'  %}">
   <style>
      .breadcrumb{
        font-size:14px;
        margin:15px 0;
        padding:8px 12px;
        background:#f9f9f9;
        border-radius:5px;
      }
      .breadcrumb a{
        text-decoration:none;
        color:#007bff;
      }
      .breadcrumb a:hover{
        text-decoration: underline;
      }
      .breadcrumb span{
        color:#555;
      }
    </style>
</head>
<body>
    <div class="container">
      {% block breadcrumb %}{% endblock %}
      {% block content %}{% endblock %}
    </div>
</body>
</html>

{% extends 'base.html' %}
{% block title %}Home{% endblock %}
{% block breadcrumbs %}
<div class="breadcrumb">
  <span>Home</span>
</div>
{% endblock %}

{% block content %}
<h1>welcome to our Restaurant</h1>
<p>explore our menu, history, and more</p>
{% endblock %}