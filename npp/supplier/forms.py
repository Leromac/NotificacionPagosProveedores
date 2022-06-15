import this
from django import forms

class addSupplierForm(forms.Form):
    taxIdentificationNumber = forms.CharField(label="Nit Proveedor", max_length=12)
    companyName = forms.CharField(label="Razon Social Proveedor", max_length=300)
    email = forms.EmailField(label="Email Para Notificacion", max_length=100)

class searchSupplierForm(forms.Form):
    taxIdentificationNumber = forms.CharField(label="Nit Proveedor", max_length=12)

