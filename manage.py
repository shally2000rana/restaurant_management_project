#settings.py
EMAIL_BACKEND='django.core.mail.backends.console.EmailBckend'
DEFAULT)FROM_EMAIL='restaurant@example.com'
#contact/forms.py
from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label="Your Name")

    email=forms.EmailField(label="Your Email")
    message=forms.CharField(widget=forms.Textarea, label="Your Message")
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']

            #send email
            send_mail(
                subject=f"New Contact Form Submision from {name}",
                message=f"Message from {name} ({email}):\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                receipent_list=['restaurant@example.com'],
            )
        return redirect('success')
    else:
        form=ContactForm()
    return render(request, "contact/contact.html", {"form":form})