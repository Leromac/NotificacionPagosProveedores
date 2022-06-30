import this
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import email
from .forms import searchSupplierForm, addSupplierForm
from .models import supplier

# Create your views here.
def supplierIndex(request):
    pass

    return render(
        request,
        'supplierIndex.html'
    )

def addSupplier(request):
    form = addSupplierForm()
    
    if request.method == 'POST':
        try:
            form = addSupplierForm(request.POST)
            
            if(supplier.objects.filter(taxIdentificationNumber=form['taxIdentificationNumber'].value()).filter(email=form['email'].value()).exists()==False):
                form.save()
                messages.success(request, "Email (%s) para notificacion agregado correctamente" %form['email'].value())
            else:
                messages.error(request, "El Email (%s) ya se encuentra agregado para este proveedor." %form['email'].value())

            return render(
                request,
                'getSupplier.html',
                {'listEmailSupplier': supplier.objects.filter(taxIdentificationNumber=form['taxIdentificationNumber'].value())}
            )
        except BaseException as err: 
            messages.error(request, "Hubo un error al guardar el Email \n %s " %err)
    else:    
        return render(
            request,
            'addSupplier.html',
            {'formAddSupplier': form}
        )
    
def searchSupplier(request):
    form = searchSupplierForm()
    
    if request.method == 'POST':
        try:
            form = searchSupplierForm(request.POST)
               
            return render(
                request,
                'getSupplier.html',
                {'listEmailSupplier': supplier.objects.filter(taxIdentificationNumber=form['taxIdentificationNumber'].value())}
            )
        except BaseException as err: 
            messages.error(request, "Error al consultar los datos \n %s " %err)
    else:
        return render(
            request,
            'searchSupplier.html',
            {'formSearchSupplier': form}
        )
