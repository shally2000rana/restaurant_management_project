from django.contrib import admin
from .models import Order

def mark_orders_processed(modeladmin, request, queryset):
    queryset.update(status='Processed')
mark_orders_processed.short_description="Mark selected orders as Processed"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id', 'customer_name', 'status', 'created_at')
    actions=[mark_orders_processed]

class Order(models.Model):
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Processed','Processed'),
    ]
    customer_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)
        
         
