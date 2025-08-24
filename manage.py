{% extends "base.html" %}
{% block title %}Contact Us{% endblock %}

{% block content %}
  <h2>Contact Us</h2>
  <form id="contactForm">
  <p>
    <label for="name">Name:</label><br>
    <input type="name" id="name" name="name" requied>
  <p>
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required>
  </p>
  <p>
    <label for="message">Message:</label><br>
    <textarea id="message" name="message" rows="4" cols="40"></textarea>
  </p>
  <button type="submit">Send</button>
  </form>

  <script>
    document.getElementById("contactForm").addEventListener("submit", function(event){
         let name=document.getElementById("name").value.trim();
         let email=document.getElementById("email").value.trim();

         if(name=== ""|| email===""){
            alert("Please fill in both Name and Email.");
            event.preventDefault();
         }
    });
  </script>
{% endblock %}


 
