from email import message
from django.contrib import messages
from django.forms import forms
from django.shortcuts import redirect, render
from django.template import context
from subcategory.forms import SubcategoryForm
from .models import Subcategory

# Create your views here.

# Create
def create(request):
    form = SubcategoryForm()
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subcategory Create')
            return redirect('subcategory_read')
    context = {
        'form': form
    }
    return render(request, 'subcategory/create.html', context)

# Read
def subcategory_read(request):
    subcategory_data = Subcategory.objects.all().order_by('-id')
    context = {
        'subcategory_data': subcategory_data
    }
    return render(request, 'subcategory/read.html', context)