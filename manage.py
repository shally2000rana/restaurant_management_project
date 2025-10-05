#orders/utils.py
from datetime import datetime
from django.db.models import Sum
from .models import orders
def get_daily_sales_total(date_obj.date)-> float:
    """
    Calculates the total sales for a specific date by summing up
    the total price of all orders placed on that day.
    Args: 
      date_obj:A date object from Python's
      datetime modele (e.g., datetime.date.today()).
      Returns:
        The calculated total sales (a float or Decimal )for the day.
        Returns 0 if no orders are found.
    """
    orders_on_date=
    Orders.objects.filter(created_a6t_date=date_obj)
    total_sales=orders_on_date.aggragate(total_sum=Sum('total_price'))
    return total_sales.get('total_sum') or 0.0
     
