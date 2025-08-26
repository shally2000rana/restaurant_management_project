from django.contrib import admin
from .models import Menu, Order, OrderItem
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('id', 'name','price')
    search_fields=('name')
    list_filter=('price')

class OrderItemInLine(admin.TabularInLine):
    model=OrderItem
    extra=1

@amin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id', 'customer', 'status', 'total_amount', 'created_at')
    list_filter=('status', 'created_at')
    search_fields=('customer__username')
    inlines=[OrderItemInLine]    

 
