from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from category.models import Category
from product.models import Product
from order.models import Order
from supplier.models import Supplier
# Create your views here.

def home(request):
    total_category = Category.objects.count()
    total_product = Product.objects.count()
    total_order = Order.objects.count()
    total_supplier = Supplier.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
    'category': total_category,
        'name': total_product,
        'product_name': total_order,
        'supplier_name': total_supplier,
        'orders': orders
    }
    return render(request, 'home.html', context)