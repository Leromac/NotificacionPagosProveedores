from django import forms
from .models import supplier

class addSupplierForm(forms.ModelForm):
    
    class Meta:
        model = supplier
        fields = [
            'taxIdentificationNumber',
            'companyName', 
            'email',
            ]
        labels = {
            'taxIdentificationNumber': ('Nit Proveedor '),
            'companyName': ('Razon Social '),
            'email': ('Email Envio Notificaciones '),
            }

class searchSupplierForm(forms.Form):
    taxIdentificationNumber = forms.CharField(label="Nit Proveedor", max_length=12)

