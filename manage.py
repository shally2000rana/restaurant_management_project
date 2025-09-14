

{% extends 'base.html' %}
{% block title %}Home{% endblock %}
{% block breadcrumbs %}
<div class="breadcrumb">
  <span>Home</span>
</div>
{% endblock %}

{% block content %}
   <div class="welcome-section">
     <h1>welcome to our Restaurant</h1>
     <p class="tagline">"where flavour meets tradition -serving happiness on every plate."</p>
   </div>
   <p>explore our menu, history, and more</p>
{% endblock %}

.welcome-section{
    text-align:center;
    margin:40px 0;
}
.welcome-section h1{
    font-size:2.5rem;
    color:#333;
    margin-bottom:10px;
}
.welcome-section .tagline{
    font-size:1.2rem;
    color:#666;
    font-style: italic;
}

