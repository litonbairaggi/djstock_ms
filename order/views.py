from django.shortcuts import render,  get_object_or_404, redirect
from . forms import OrderForm
from .models import Order
from django.contrib import messages
from product.models import Product
# Create your views here.

# Create
def create(request):
    form = OrderForm()
    if request.method == 'POST':
        quantity = request.POST['quantity']
        form = OrderForm(request.POST)

        # print(quantity)

        if form.is_valid():
            form.save()
            messages.success(request, 'Order created')
            return redirect('order_read')
    context = {
        'form':form
    } 
    return render(request, 'order/create.html', context)

# Read
def order_read(request):
    order_data = Order.objects.all()
    context = {
        'order_data': order_data
    }
    return render(request, 'order/read.html', context)

# Update 
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
def order_delete(request, pk):
    get_user = get_object_or_404(Order, pk=pk)
    get_user.delete()
    messages.error(request, 'Order deleted')
    return redirect('order_read')