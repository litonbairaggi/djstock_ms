from corsheaders import django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.template import context
from zeroconf import re
from .forms import RegisterForm
from category.models import Category
from product.models import Product
from order.models import Order
from supplier.models import Supplier
# Create your views here.

@login_required
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


# login
def login_view(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user_auth = authenticate(username = u, password = p)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Login Success')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username and password')

    return render(request, 'login.html')

# Registration
def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration success, you can login now...')
            return redirect('login')
    else:
        form = RegisterForm
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

# logout
def logout_view(request):
    logout(request)
    return redirect('login')

# change password
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'change_pass.html', context)