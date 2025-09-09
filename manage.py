#forms.py
from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100, required=False)
    email=forms.EmailField(required=True, error_message={
        'required': 'Please enter your email address.',
        'invalid': 'Enter a valid email address.',
    })
    message=forms.CharField(
        widget=forms.Textarea,
        required=True,
        error_message={'required': 'Please enter a message.'}
    )
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            name=form.cleaned_data.get('name','Anonumous')
            print(f"Message from {name} ({email}): {message}")

            return render(request,'contact_success.html')
        else:
            form=ContactForm()
        return render(request, 'contact.html', {'form': form})

<h2>Contact us</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p  }}
  <button type="submit">Send</button>
</form>
