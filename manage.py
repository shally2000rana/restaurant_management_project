import string
import secrets
from .models import Coupon

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code
    """
    characters=string.ascii_uppercase+string.digits

    while True:
        code=''.join(secrets.choice(characters)for _in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code

from django.db import models
class Coupon(models.Model):
    code=models.CharField(max_length=20, unique=True)
    discount=models.DecimalFiels(max_length=5, decimal_places=2)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.code
from orders.utils import generate_coupon_code

new_code=generate_coupon_code(12)
