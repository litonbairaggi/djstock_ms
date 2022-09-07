from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . forms import SupplierForm
from .models import Supplier
from django.contrib import messages
# Create your views here.

# Create
@login_required
def create(request):
    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier created')
            return redirect('supplier_read')
    context = {
        'form':form
    }
    return render(request, 'supplier/create.html', context)

# Read
@login_required
def supplier_read(request):
    supplier_data = Supplier.objects.all()
    context = {
        'supplier_data': supplier_data
    }
    return render(request, 'supplier/read.html', context)

# Update 
@login_required
def supplier_update(request, pk):
    get_user_data = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(instance=get_user_data)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier updated')
            return redirect('supplier_read') 
    context = {
        'form':form
    }
    return render(request, 'supplier/create.html', context)

# Delete
@login_required
def supplier_delete(request, pk):
    get_user = get_object_or_404(Supplier, pk=pk)
    get_user.delete()
    messages.error(request, 'Supplier deleted')
    return redirect('supplier_read')