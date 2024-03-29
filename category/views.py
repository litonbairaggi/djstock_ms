from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . forms import CategoryForm
from .models import Category
from django.contrib import messages
# Create your views here.

# Create
@login_required
def create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created')
            return redirect('category_read')
    context = {
        'form':form
    }
    return render(request, 'category/create.html', context)

# Read
@login_required
def category_read(request):
    category_data = Category.objects.all().order_by('-id')
    context = {
        'category_data': category_data
    }
    return render(request, 'category/read.html', context)

# Update 
@login_required
def category_update(request, pk):
    get_user_data = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=get_user_data)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated')
            return redirect('category_read') 
    context = {
        'form':form
    }
    return render(request, 'category/create.html', context)

# Delete
@login_required
def category_delete(request, pk):
    get_user = get_object_or_404(Category, pk=pk)
    get_user.delete()
    messages.error(request, 'Category deleted')
    return redirect('category_read')