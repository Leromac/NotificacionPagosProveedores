import email
from django.shortcuts import render
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
        form = addSupplierForm(request.POST)
        
        form.save()
    
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