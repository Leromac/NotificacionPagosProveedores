from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
import csv
import random
from django.core.mail import EmailMultiAlternatives
from .forms import sendNotificationForm
from .models import notification, readFile
from supplier.models import supplier

# Create your views here.
def notificationIndex(request):
    form = sendNotificationForm()
    
    if request.method == 'POST':
        #try:
        form = sendNotificationForm(request.POST, request.FILES)

        if form.is_valid():
            newFiletoProcess = notification(baseFile = request.FILES['baseFile'])
            #newFiletoProcess = notification(uploadTo = request.FILES['baseFile'])
                    
            newFiletoProcess.save(form)

            readFile(newFiletoProcess.baseFile)

        #except BaseException as err: 
            #messages.error(request, "Error al consultar los datos \n %s " %err)
            
        
    return render(
        request,
        'notificationIndex.html',
        {'formSendNotification': form}
    )