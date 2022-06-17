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
            form.save()
            messages.success(request, "Datos Proveedor Guardados Correctamente %s " %form['taxIdentificationNumber'].value())
        except: 
            messages.error(request, "Hubo un error al guardar el artículo")
        return redirect('getIndividualSupplier', form['taxIdentificationNumber'].value())
        #getIndividualSupplier(getIndividualSupplier, form['taxIdentificationNumber'].value())
    return render(
        request,
        'addSupplier.html',
        {'formAddSupplier': form}
    )
    
def searchSupplier(request):
    form = searchSupplierForm()
    
    if request.method == 'POST':
        form = searchSupplierForm(request.POST)
    
    return render(
        request,
        'searchSupplier.html',
        {'formSearchSupplier': form}
    )
    
def getIndividualSupplier(request, taxIdentificationNumber):
    individualSupplierList = supplier.objects.filter(taxIdentificationNumber=taxIdentificationNumber)
    
    return render(
        request,
        'getSupplier.html',
        {'dataGetSupplier': individualSupplierList}
    )