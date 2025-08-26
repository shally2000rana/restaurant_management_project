from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def menu_api(request):
    menu=[
        {"id": 1, "name":"Margherita Pizza", "description": "Classic pizza with cheese and tomato", "price":250},
        {"id": 2, "name":"Veg burger ","description": "veg patty with frsh lettuce and mayo", "price":150},
        {"id": 3, "name":"Pasta alffredo", "description": "Creamy white sauce pasta with herbs", "price":300}
    ]
    return Response(menu)

 
