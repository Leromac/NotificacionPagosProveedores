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
            existSupplier = (supplier.objects.filter(taxIdentificationNumber=form['taxIdentificationNumber'].value()).filter(email=form['email'].value()).exists())
            form = addSupplierForm(request.POST)

            if(existSupplier):
                form.save()
                messages.success(request, "Email para notificacion agregado correctamente %s" %existSupplier)
            else:
                messages.error(request, "El Email (%s) ya se encuentra agregado para este proveedor." %form['email'].value())
        except BaseException as err: 
            messages.error(request, "Hubo un error al guardar el artículo \n %s " %err)
        #return redirect('getIndividualSupplier', form['taxIdentificationNumber'].value())
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