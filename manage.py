class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6, decimal_places=2)
class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    menu_item=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def get_unique+item_names(self):
        items=self.order_items.all()
        names=[item.menu_item.name for itwm in items]
        unique_names=list(set(names))
        return unique_names
        
         
