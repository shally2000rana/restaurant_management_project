home/utils.py
from home.models import MenuItem, Cuisine
def get_distinct_cuisnes():
    """
    Returns a list of unique cuisne names currently available
    across all menu items.
    """
    rerurn list(
        MenuItem.objects.values_list('cuisine__name', flat=True).distinct()
    )
        
        
         
