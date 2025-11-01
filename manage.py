from decimal import Decimal, ROUND_HALF_UP
def calculate_tip_amount(order_total, tip_percentage):
    """
    calculate the tip amount for a given total and tip percentage.
    parameters:
      order_total(float or decimal): the total amount of the order before the tip.
      tip_peercentage (int or float): the tip percentage
    returns:
      decimal : the calculated tip qmount, rounded to two decimal places.
    """
    order_total=Decimal(order_total)
    tip_amount=order_total*(Decimal(tip_percentage)/Decimal(100))
    tip_amount=tip_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return tip_amount
        
         
