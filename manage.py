#orders/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Coupon(models.Model):
    #Coupon code, must be unique
    code=models.CharField(
        max_length=50,
        unique=True,
    )
    #Discount percentage (e.g., 0.10 for 10% off)
    discount_percentage=models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0),
        MaxValueValidator(1)], #Ensure discount is between 0 and 1 (0% to 100%)
        help_text='Discount as a percentage (e.g., 0.10 for 10% 0ff) '
    )
    #Status :True to enable, False to disable 
    is_active=models.BooleanField(
        default=True,
        help_text='Indicates if the coupon is currently active'
    )
    #Validate period
    valid_from = models.DateField(
        help_text='Date from which the coupon is valid'
    )
    valid_until=models.DateField(
        help_text='Date from which the coupon is valid(inclusive)'
    )
    #Impplement_str_method for better representation in the admin
    def__str__(self):
        return self.code

    class Meta:
        ordering=['-valid_from']
        verbose_name='Coupon'
        verbose_name_plural='Coupons'

#orders/serializers.py
from rest_framework import serializers
class CouponValidationSerializer(serializers.Serializer):
    code=serializers.CharField(max_length=50)

#orders/views.py
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import Status
from .models import Coupon
from .serializers import CouponValidationSerializer
from datetime import date
class CouponValidationSerializer(APIView):
    """
    API endpoint to validate a coupon code.
    Expects a POST request with {'code':'YOURCODE'} in the body.
    """
    def post(self, request, *args, **kwargs):
        #use the serializer to validate the incoming data
        serializer=CouponValidationSerializer(
            data=request.dta
        )