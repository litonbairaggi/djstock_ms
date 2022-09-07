from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Order
import calculation

class OrderForm(forms.ModelForm):
    name = forms.CharField(label="Buyer Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name Here'}), required=True, error_messages={'required':'Must Enter a Currect Name'})
    description = forms.CharField(label="Description", widget=forms.Textarea({'class': 'form-control', 'placeholder':'Description', 'rows':4, 'cols':50}), required=True, error_messages={'required':'Must Enter Descriptions'})

    class Meta:
        model = Order
        fields = ['id', 'name', 'mobile', 'product_name', 'category', 'description', 'delivery', 'quantity', 'unit_price']
        widgets = {
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Phone'}),
            'product_name': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'delivery': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Quantity'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Unit Price'}),
            
            
        }