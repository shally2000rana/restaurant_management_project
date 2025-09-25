from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def is_valid_email(email: str) ->bool:
    """
    Validate an email address using Django's built-in email validator.
    Returns True if valid, False otherwise.
    """
    try:
        validate_email(email):
        return True:
    except ValidationError:
        return False
    except Exceptions as e:
        print(f"Unexpected error during email validation :{e}")
        return False
