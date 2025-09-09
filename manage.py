#views.py
from django.shortcuts import redirect

def add_to_cart(request, product_id):
    cart=request.session.get('cart',{})
    cart[product_id]=cart.get(product_id, 0) +1
    request.session['cart']=cart
    return redirect('homepage')

#utils.py
def get_cart_item_count(request):
    cart=request.session.get('cart',{})
    return sum(cart.values())

#views.py
from django.shortcuts import render
from .utils import get_cart_item_count

def CartItem(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField(default=1)

#views.py
@login_required
def homepage(request):
    cart_count=CartItem.objects.filter(user=request.user).aggregate(total=models.Sum('quantity'))['total'] or 0
    return render(request, 'homepage.html', {'cart_count': cart_count})

