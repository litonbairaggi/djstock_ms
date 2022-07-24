from django.shortcuts import render,  get_object_or_404, redirect
from . forms import ProductForm
from .models import Product
from django.contrib import messages
# Create your views here.

# Create
def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created')
            return redirect('product_read')
    context = {
        'form':form
    }
    return render(request, 'product/create.html', context)

# Read
def product_read(request):
    product_data = Product.objects.all()
    context = {
        'product_data': product_data
    }
    return render(request, 'product/read.html', context)

# Update
def product_update(request, pk):
    get_user_data = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=get_user_data)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated')
            return redirect('product_read') 
    context = {
        'form':form
    }
    return render(request, 'product/create.html', context)

# Delete
def product_delete(request, pk):
    get_user = get_object_or_404(Product, pk=pk)
    get_user.delete()
    messages.error(request, 'Product deleted')
    return redirect('product_read')