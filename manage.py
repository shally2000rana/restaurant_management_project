from rest_framework import serializers
#Assuming your Table model is in the 'home' app
from .models import Table
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        #include the fields required by the prompt
        fields=['id','table_number', 'capacity', 'is_available']

from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
class AvailableTablesAPIView(generics.ListAPIView):
    #Specify the serializer to use for the response data
    serializer_class=TableSerializer
    def get_queryset(self):
        """
        Returns the queryset of Table objects, filtered
        to include only those where is_available is True.
        """
        #The core requirement filtering the tables
        return Table.objects.filter(is_available=True)
        #you could also use a simple APIView or a function-based view, but ListAPIView is cleaner.
from django.urls import path
from .views import AvailableTablesAPIView
urlpatterns=[
    #Map the specified URL path to your view path
    ('api/tables/available/',
      AvailableTablesAPIView.as_view(),
      name='available_tables_api').
]
