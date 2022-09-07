from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def login_view(request):
#     if request.method == 'POST':
#         u = request.POST['username']
#         p = request.POST['password']
#         user_auth = authenticate(username = u, password = p)
#         if user_auth is not None:
#             login(request, user_auth)
#             messages.success(request, 'Login Success') 
#             return redirect('dashboard')
#         else:
#             messages.warning(request, 'Invalid username and password')    

#     return render(request, 'login.html')

# def register_view(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration success, you can login now...')
#             return redirect('login')
#     context = {
#         'form':form
#     }
#     return render(request, 'register.html', context)

# @login_required()    
# def dashboard_view(request):
#     return render(request, 'home.html')

# def logout_view(request):
#     logout(request)
#     return redirect('login')