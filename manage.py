from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.core.exceptions import ValidateError
from django.core.validators import vallidate_email

def send_email_util(recipient_email, subject, message_body, from_email=None):
    """
    Utility function to send an email.
    """
    try:
        vallidate_email(recipient_email)
        if not from_email:
            from_email=settings.DEFAULT_FROM_EMAIL

        send_mail(
            subject,
            message_body,
            from_email,
            [recipient_email],
            fail_silently=False,
        )
        return True, "Email sent successfully"
    except ValidateError:
        return False, "Invalid recipient email address"    
    except BadHeaderError:
        return False, "Invalid header found"
    except Exception as e:
        return False, f"Error sending email: {str(e)}"

EMAIL_BACKEND="django.core.email.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER="your-email@gmail.com"
EMAIL_HOST_PASSWORD="your-app-password"
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER

from django.http import JsonResponse
from .utils import send_email_util
def test_email(request):
    success, message=send_email_util(
        recipient_email="test@example.com",
        subject="Test Email",
        message_body="Hello! This is a test email from Django."
    )
    return JsonResponse({"success":success, "message":message})
