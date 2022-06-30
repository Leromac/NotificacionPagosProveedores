from django.shortcuts import render
from django.contrib import messages
from .forms import sendNotificationForm
from .models import notification

# Create your views here.
def notificationIndex(request):
    form = sendNotificationForm()
    
    if request.method == 'POST':
        try:
            #form = searchSupplierForm(request.POST)
            pass
               
            
        except BaseException as err: 
            messages.error(request, "Error al consultar los datos \n %s " %err)
    else:
        return render(
        request,
        'notificationIndex.html',
        {'formSendNotification': form}
    )