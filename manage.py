from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
class TableDetailView(generics.RetrieveAPIView):
    querset=Table.objects.all()
    serializer_class=TableSerializer
         
