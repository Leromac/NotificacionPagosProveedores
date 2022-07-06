from asyncio.windows_events import NULL
from django.db import models
import csv
import random
from datetime import datetime
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from supplier.models import supplier

class notification(models.Model):
    baseFile = models.FileField(name="baseFile", max_length=500)
    uploadTo = models.FileField(upload_to='')
    creationDate = models.DateTimeField(auto_now_add=True)
    

class notificationContent(models.Model):
    customId = models.CharField(name="customId", max_length=50)
    taxIdentificationNumber = models.CharField(name="taxIdentificationNumber", max_length=20)
    accountNumber = models.CharField(name="accountNumber", max_length=50)
    transactionDate = models.DateField(name="transactionDate")
    transactionDocumentType = models.CharField(name="transactionDocumentType", max_length=100)
    icaRetention = models.CharField(name="icaRetention", max_length=20)
    ivaRetention = models.CharField(name="ivaRetention", max_length=20)
    rentaRetention = models.CharField(name="rentaRetention", max_length=20)
    amountPaid = models.CharField(name="amountPaid", max_length=20)
    totalValueInvoice = models.CharField(name="totalValueInvoice", max_length=20)
    note = models.CharField(name="note", max_length=1000)

def readFile (fileName):
    controlList = []
    
    try:
        notificationCustomId = str(random.random())
        notificationCustomId = notificationCustomId.lstrip("0.")
        
        with open('upload\%s' %fileName) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            next(entrada, None)

            for reg in entrada:
                nc = notificationContent()

                nc.customId = notificationCustomId
                nc.taxIdentificationNumber = reg[0]
                nc.accountNumber = reg[1]
                nc.transactionDate = datetime.strptime(reg[2], '%d/%m/%Y')
                nc.transactionDocumentType = reg[3]
                nc.icaRetention = reg[4]
                nc.ivaRetention = reg[5]
                nc.rentaRetention = reg[6]
                nc.amountPaid = reg[7]
                nc.totalValueInvoice = reg[8]
                nc.note = reg[9]

                nc.save()

                if reg[0] not in controlList:
                    controlList.append(reg[0])
                    
            sentNotification(notificationCustomId, controlList)
            sentNotificationToControl(notificationCustomId, controlList)
    except Exception as ex:
        print ("Error al leer el archivo .csv %s " % (ex))
    
def sentNotification(notificationCustomId, supplierTaxIdentificationNumberList):
    try:
        #supplierTaxIdentificationNumberList =  notificationContent.objects.filter(customId="%s" %notificationCustomId).distinct('taxIdentificationNumber')
         
        for i in range(len(supplierTaxIdentificationNumberList)):
            operationList = supplier.objects.filter(taxIdentificationNumber="%s" % supplierTaxIdentificationNumberList[i])
            contentList = notificationContent.objects.filter(customId="%s" %notificationCustomId).filter(taxIdentificationNumber="%s" %supplierTaxIdentificationNumberList[i])
            
            
            x=0
            
            for filas in operationList:
                if not filas:
                    pass
                    #noEnviado+= "</br>"+(filas[x].nit)+" -- "+(filas[x+1].nombre)
                    #print ("NO SE PUDO ENVIAR CORREO A %s " % ((filas[x].nit)+" -- "+(filas[x+1].nombre)))
                else:
                    if(filas.email != ""):
                        #+=1
                        try:
                            sendMail(contentList, filas.email)
                            #models.envioCorreo("no-reply@astivik.com", (filas[x+2].email), listaEnvio[i])
                            #textoEnvioControl += "<tr><td ALIGN=center>" + str(y) + "</td><td ALIGN=left>" + (filas[x+1].nombre) + "</td><td ALIGN=left>" + (filas[x+2].email) + "</td></tr>"
                            #print ("enviado A %s " % ((filas[x].nit)+" -- "+(filas[x+1].nombre)))
                        except Exception as ex:
                            print ("Error al enviar notificacion %s %s" % ((supplierTaxIdentificationNumberList[i]), ex))
                    else:
                        pass
                        #noEnviado+= "</br>"+(filas[x].nit)+" -- "+(filas[x+1].nombre+"</br>")
                                        
                x+=3
    except Exception as ex:
        print ("Error al realizar accion en la base de datos \n %s " % (ex))

def sentNotificationToControl(notificationCustomId, supplierTaxIdentificationNumberList):
    try:
        #supplierTaxIdentificationNumberList =  notificationContent.objects.filter(customId="%s" %notificationCustomId).distinct('taxIdentificationNumber')
         
        for i in range(len(supplierTaxIdentificationNumberList)):
            operationList = supplier.objects.filter(taxIdentificationNumber="%s" % supplierTaxIdentificationNumberList[i])
            contentList = notificationContent.objects.filter(customId="%s" %notificationCustomId).filter(taxIdentificationNumber="%s" %supplierTaxIdentificationNumberList[i])
            
            for filas in operationList:
                if not filas:
                    pass
                    
                else:
                    if(filas.email != ""):
                        try:
                            sendMail(contentList, filas.email)
                        except Exception as ex:
                            print ("Error al enviar notificacion %s %s" % ((supplierTaxIdentificationNumberList[i]), ex))
                    else:
                        pass
    except Exception as ex:
        print ("Error al realizar accion en la base de datos \n %s " % (ex))

def sendMail(body, to):
    try:
        subject = 'Astivik S.A. -- Notificación Pagos Realizados.'
        template = get_template('emailMessage.html')

        content = template.render({
            'NotificacionMessage': body,
        })

        message = EmailMultiAlternatives(subject,
                                        '',
                                        settings.EMAIL_HOST_USER,
                                        to=[
                                            to
                                        ])

        message.attach_alternative(content, 'text/html')
        message.send()
    except Exception as ex:
        print ("Error al enviar correo \n %s " % (ex))