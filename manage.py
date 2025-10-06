#orders/utils.py
from datetime import datetime, time
def is_resyautant_open():
    now==datetime.now()
    current_time=now.time()
    current_day=now.weekday()
    opening_time=time(0,0)
    closing_time=time(22,0)
    if opening_time <= current_time <=closing_time:
        return True
    return False
         
