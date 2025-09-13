from django.shortcuts import render

def faq_view(request):
    faqs=[
        {"question":"what are your opening hours?", "answer":"we are open from 9AM to 10PM every day."},
        {"question":"Do you offer home delivery?", "answer":"Yes, we offer free home delivery within 5 km."},
        {"question":"How can i contact you?", "answer":"You can call us at (123) 456-7890 or email info@restaurant.com."},
    ]

    return render(request,"faq.html", {"faqs": faqs})

<!DOCTYPE html>
<html>
<head>
    <title>FAQs</title>
</head>
<body>
    <h1>Frequently Asked Questions</h1>

    <ul>
      {% for item in faqs %}
        <li>
          <strong>Q: {{item.question }}</strong>
          A: {{item.answer}}
        </li>
      {% endfor %}
    </ul>

    <p><a href="{% url 'home' %}">Back to home </a></p>
</body>
</html>

from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_view, name='home'),
    path('faq/', views.faq.view, name='faq'),
]
<p><a href="{% url 'faq' %}">Visit our FAQ page</a></p>

