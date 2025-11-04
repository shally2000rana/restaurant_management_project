from datetime import datetime

def format_datetime(dt):
    """
    Returns a formatted string for a given datetime object.
    Example: 'January 1, 2023 at 10:30 AM'
    If dt is None, returns an empty string.
    """
    if dt is None:
        return ""
    if not isinstance(dt, datetime):
        return ""

    return dt.strftime("%B %D, %Y at %I:%M:%p")

        
        
         
