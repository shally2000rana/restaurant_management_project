import re

def validate_phone_number(phone_number):
    """
    Validate a phone number format.
    Accepts 10-12 digits, may include optional spaces, hypens,
    or a country code prefix(like '+1')

    Returns:
       True if the phone number matches a valid pattern, otherwise False.
    """
    pattern=r'^(\+?\d{1,3}[-]?)?\d{10,12}$'
    cleaned_number=phone_number.strip()

    return bool(re.match(pattern, cleaned_number))
        
         
