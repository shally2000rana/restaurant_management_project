<!DOCTYPE html>
<html>
<head>
   <title>Home Page</title>
</head>
<body> 
   <h1>Welcome to Our Restaurant</h1>

   <!-- Current Date and Time Section-->
   <section>
      <h2>Current Date and Time</h2>
      <p>{% now "l, d F Y - h:i A" %}</p>
    </section>
</body>
</html>

from django import template
from django.utils import timezone

register=template.Library()

@register.simple_tag
def current_datetime(format_string="%A, %d %B %Y - %I:%M:%p"):
    now=timezone.now()
    return now,strftime(format_string)

