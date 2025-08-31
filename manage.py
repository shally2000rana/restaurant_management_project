from django.db import models
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.urls import path
from .import views


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'email']

def home(request):
    if request.method=='POST'
       form=ContactForm(request.POST)
       if form.is_valid():
       form.save()
       return redirect('home')
    else:
        form=ContactForm()
    return render(request, 'home.html', {'form': form})

urlpatterns=[
    path('', views.home, name='home')
]
  
