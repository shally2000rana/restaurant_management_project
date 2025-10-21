from rest_framework.decorators import api_view
from rest_framework.response import response
from rest_framework import status
@api_view(['GET'])
def get_order_status(reuest, order_id):
    """
    Retrieve the current status of an order given its ID.
    """
    try:
        order=Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return response
        
         
