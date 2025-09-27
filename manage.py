EMAIL_BACKEND="django.core.mail.backend.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER="your_email@gmail.com"
EMAIL_HOST_PASSWORD="your_app_password"
DEAULT_FROM_EMAIL=EMAIL_HOST_USER
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging
logger=logging.getLogger(__name__)
def send_order_confirmation_email(order_id, customer_email, order_items, total_price):
    """
    Sends an order confirmation email to the customer.
    """
    subject=f"Order confirmation - order #{order_id}"
    message=(
        f"Thank you for your order!\n\n"
        f"order ID: {order_id}\n"
        f"Items: {','join(order_items)}\n"
        f"Total Price: {total_price}\n\n"
        f"We will notify you once your order is shipped.\n\n"
        f"Best Regards, \nSmart Restaurant Team"
    )
    from_email=settings.DEAULT_FROM_EMAIL
    receipent_list=[customer_email]
    try:
        send_mail(subject, message, from_email, receipent_list, fail_silently=False)
        logger.info(f"order confirmation email sent to {customer_email} for order ID {order_id}")
        return True
    except BadHeaderError:
        logger.error("Invalid header found while sending email")
        return False
    except Exception as e:
        logger.error(f"Error sending email : {e}")
        return False

