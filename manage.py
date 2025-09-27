from rest_framework import serializers
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]

from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer

class UserProfileUpdateView(UpdateAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        return self.request.User

from django.urls import path
from .views import UserProfileUpdateView

urlpatterns=[
    path("profile/update/", UserProfileUpdateView,as_view(), name="profile-update"),
]

