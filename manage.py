class MenuItem(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    is_available=models.BooleanField(default=True)

from rest_framework import srializers
from .models import MenuItem

class MenuItemAvailabilitySerializer(srializers.Serializer):
    is_available=Serializers.BooleanField()

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import status
from .models import MenuItem
from .Serializers import MenuItemAvailabilitySerializer

class UpdateMenuAvailabilityAPIView(APIView):
    def patch(self, request, pk):
        try:
            item=MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        Serializer=MenuItemAvailabilitySerializer(data=request.data)
        Serializer.is_valid(raise_exception=True)