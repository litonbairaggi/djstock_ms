from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Supplier
import calculation

class SupplierForm(forms.ModelForm):
    supplier_name = forms.CharField(label="Supplier Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Supplier Name'}), required=True, error_messages={'required':'Must Enter a Currect Name'})
    address = forms.CharField(label="Address", widget=forms.TextInput({'class': 'form-control', 'placeholder':'Address', 'rows':4, 'cols':50}), required=True, error_messages={'required':'Must Enter Address'})

    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name', 'address', 'phone_number']
        widgets = {
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Phone'}),
        }