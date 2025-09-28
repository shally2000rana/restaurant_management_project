from django.db import models
class ContactFormSubmission(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
from rest_framework import serializers
from .models import ContactFormSubmission
class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model= ContactFormSubmission
        fields=['id','name','email','message','created_at']
from rest_framework import generics
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer

class ContactFormSubmissionView(generics.CreateAPIView):
    queryset=ContactFormSubmission.objects.all()
    serializer_class=ContactFormSubmissionSerializer
from django.urls import path
from .views import ContactFormSubmissionView
urlpatterns=[
    path("contact/", ContactFormSubmissionView.as_view(). name="conatct-form"),
]
        

