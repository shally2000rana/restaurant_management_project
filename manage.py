from rest_framework import serializers
from .models import PaymentMethod

class PaymentMethodSerializer(serializers.ModelSerailizer):
    class Meta:
        model=PaymentMethod
        fields='__all__'

from rest_framework import generics
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer

class PaymentMethodListView(generics.ListAPIView):
    queryset=PaymentMethod.objects.filter(is_active=True)
    serializer_class=PaymentMethodSerializer

        
        
         
