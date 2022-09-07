from unicodedata import name
from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . forms import OrderForm
from .models import Order
from django.contrib import messages
from product.models import Product
# Create your views here.

# Create
@login_required
def create(request):
    form = OrderForm()
    if request.method == 'POST':
        quantity = request.POST['quantity']
        product_name = Product.objects.all()
        print("============================================")
        print(quantity)
        # print(product_name.product_quantity)
        print("============================================")
        form = OrderForm(request.POST)

        products = Product.objects.all()
        total_products = products.count()

        print("+++++++++++++++++++++")
        print(total_products)
        print("+++++++++++++++++++++")

        if form.is_valid():

            # added_quantity = int(request.POST['quantity'])
            # issued_item.total_quantity += added_quantity
            # issued_item.save()

            form.save()
            messages.success(request, 'Order created')
            return redirect('order_read')
    context = {
        'form':form
    } 
    return render(request, 'order/create.html', context)

# Read
@login_required
def order_read(request):
    order_data = Order.objects.all().order_by('-id')
    context = {
        'order_data': order_data
    }
    return render(request, 'order/read.html', context)

# Update 
@login_required
def order_update(request, pk):
    get_user_data = get_object_or_404(Order, pk=pk)
    form = OrderForm(instance=get_user_data)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated')
            return redirect('order_read') 
    context = {
        'form':form
    }
    return render(request, 'order/create.html', context)

# Delete
@login_required
def order_delete(request, pk):
    get_user = get_object_or_404(Order, pk=pk)
    get_user.delete()
    messages.error(request, 'Order deleted')
    return redirect('order_read')