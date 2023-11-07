from django.shortcuts import render
from .models import Product

def dashboard(request):
    try:
        products = Product.objects.all()
        if not products:
            print("No products found in the database.")
    except Exception as e:
        print(f"Error fetching products: {e}")
    
    return render(request, 'dashboard.html', {'products': products})
