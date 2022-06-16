from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    # print(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username = username, password = password)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, 'Login Success') 
            return redirect('login')
        else:
            messages.warning(request, 'Invalid username and password')    

    return render(request, 'register.html')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration success, you can login now...')
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'login.html', context)

@login_required()    
def dashboard_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')