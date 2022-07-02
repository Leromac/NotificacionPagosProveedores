from django.shortcuts import render
from django.contrib import messages
from .forms import sendNotificationForm
from .models import notification

# Create your views here.
def notificationIndex(request):
    form = sendNotificationForm()
    
    if request.method == 'POST':
        try:
            form = sendNotificationForm(request.POST, request.FILES)

            if form.is_valid():
                newFiletoProcess = notification(baseFile = request.FILES['uploadTo'])
                newFiletoProcess = notification(uploadTo = request.FILES['uploadTo'])

                newFiletoProcess.save(form)

                messages.success(request, "Archivo recibido para procesamiento %s" %newFiletoProcess.baseFile)
                #procesar_archivo(request.FILES['docfile'])   

            return render(
                request,
                'notificationIndex.html',
                {'formSendNotification': form}
            )
        except BaseException as err: 
            messages.error(request, "Error al consultar los datos \n %s " %err)
    else:
        return render(
        request,
        'notificationIndex.html',
        {'formSendNotification': form}
    )