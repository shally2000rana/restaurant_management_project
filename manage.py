from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .models import MenuItems
from .serializers import MenuItemsSerializer

class MenuItemByCategory(APIView):
    def get(self, request, *args, **kwargs):
        """
        An API endpointto retreive menu items
        filtered by category.
        """
        category_name=request.query_params.get('category_name') 
        if not category_name:
            return Response({"error":"Category name parameter is required."}status=status.HTTP_400_BAD_REQUEST)

        menu_items=MenuItems.objects.filter(category_name=category_name)

    MenuItemsSerializer(menu_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)