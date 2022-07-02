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

class searchSupplierForm(forms.ModelForm):
    #taxIdentificationNumber = forms.CharField(label="Nit Proveedor", max_length=12)
    class Meta:
        model = supplier
        fields = [
            'taxIdentificationNumber',
            ]
        labels = {
            'taxIdentificationNumber': ('Nit Proveedor '),
            }
    