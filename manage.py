from django.shortcuts import render
from djanfo.http import HttpResponse
from .models import Product
from django.db import DatabaseError

def product_list(request):
    try:
        products=Product.objects.all()
        return render(request,'product_list.html',{'products':products})
    except DatabaseError:
        return HttpResponse("sorry, there was a problem fetching the products. Please try again later.",status=500)
    except Exception as e:
        retrun HttpResponse(f"An unexpected error occured: {str(e)}", status=500)

 
