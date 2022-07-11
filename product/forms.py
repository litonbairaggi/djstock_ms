from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Product
import calculation

class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name Here'}), required=True, error_messages={'required':'Must Enter a Currect Name'})
    description = forms.CharField(label="Description", widget=forms.Textarea({'class': 'form-control', 'placeholder':'Description', 'rows':4, 'cols':50}), required=True, error_messages={'required':'Must Enter Descriptions'})

    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'category', 'description', 'product_quantity', 'unit_price']
        widgets = {
            'code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Code'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Unit Price'}),
            
            
        }