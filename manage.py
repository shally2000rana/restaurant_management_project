from datetime import datetime
from your_app.models import DailyOperatingHours

def get_today_operating_hours():
    today=datetime.today().strftime('%A')
    try:
        hours=DailyOperatingHours.objects.get(day=today)
        return (hours.open_time, hours.close_time)
    except DailyOperatingHours.DoesNotExist:
        return (None, None)
        
         
