from django import forms 
from django.db import models
from django.forms import fields
from .models import Subcategory

class SubcategoryForm(forms.ModelForm):
    subcategory_name = forms.CharField(label="Subcategory Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subcategory'}), required=True, error_messages={'required':'Must Enter a Currect Subcategory Name'})
    model = Subcategory
    fields = ['id', 'subcategory_name', 'category']
    widgets = {
        'category': forms.Select(attrs={'class': 'form-control'}),
    }