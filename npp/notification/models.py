from asyncio.windows_events import NULL
from django.db import models
import csv
import random
from django.conf import settings
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
    icaRetention = models.FloatField(name="icaRetention")
    ivaRetention = models.FloatField(name="ivaRetention")
    rentaRetention = models.FloatField(name="rentaRetention")
    amountPaid = models.FloatField(name="amountPaid")
    totalValueInvoice = models.FloatField(name="totalValueInvoice")
    note = models.CharField(name="note", max_length=1000)

    def __init__(self, customId, taxIdentificationNumber, accountNumber, transactionDate, transactionDocumentType, icaRetention, ivaRetention, rentaRetention, amountPaid, totalValueInvoice, note):
        self.customId = customId
        self.taxIdentificationNumber = taxIdentificationNumber
        self.accountNumber = accountNumber
        self.transactionDate = transactionDate
        self.transactionDocumentType = transactionDocumentType
        self.icaRetention = icaRetention
        self.ivaRetention = ivaRetention
        self.rentaRetention = rentaRetention
        self.amountPaid = amountPaid
        self.totalValueInvoice = totalValueInvoice
        self.note = note

def readFile (fileName):
    notificationCustomId = random()
    controlList = []
    #sendList = []
    nc = notificationContent()

    try:
        with open('upload\%s' %fileName) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            next(entrada, None)
                       
            #textoEnvio = ""

            for reg in entrada:
                nc.customId = notificationCustomId
                nc.taxIdentificationNumber = reg[0]
                nc.accountNumber = reg[1]
                nc.transactionDate = reg[2]
                nc.transactionDocumentType = reg[3]
                nc.icaRetention = reg[4]
                nc.ivaRetention = reg[5]
                nc.rentaRetention = reg[6]
                nc.amountPaid = reg[7]
                nc.totalValueInvoice = reg[8]
                nc.note = reg[9]

                nc.save()

                #sendList.append(nf)
                
                if reg[0] not in controlList:
                    controlList.append(reg[0])
                    #textoEnvio += "<tr><td ALIGN=right>" + reg[3] + "</td><td ALIGN=right>" + reg[8] + "</td><td ALIGN=right>" + reg[4] + "</td><td ALIGN=right>" + reg[5] + "</td><td ALIGN=right>" + reg[6] + "</td><td ALIGN=right>" + reg[7] + "</td><td ALIGN=left>" + reg[9] + "</td></tr>"
                #else:
                    #if textoEnvio:
                    #    textoEnvio += "</table><br></br><p>Agradecemos distribuir esta informacion al personal de su empresa que le puedan ser util estos datos.</p>"
                    #    textoEnvio += "<br></br><footer><strong>POR FAVOR NO RESPONDER A ESTA CUENTA DE CORREO, NADIE MONITOREA ESTOS MENSAJES Y SE ELIMINAN AUTOMATICAMENTE.</strong></footer>"
                    #    listaEnvio.append(textoEnvio)
                    #    textoEnvio = ""
                
                    #controlList.append(reg[0])
                    #textoEnvio += "<h3>Cordial Saludo.</h3>"
                    #textoEnvio += "<br></br><h3>Industrias Astivik le informa, que se realizo una transferencia el dia " + reg[2] + " a su cuenta bancaria No " + reg[1] + "</h3>"
                    #textoEnvio += "<br></br><p>Las facturas pagadas fueron las siguientes:</p>"
                    #textoEnvio += '<br></br><table BORDER bordercolor="black" CELLPADDING=10 CELLSPACING=0><tr><th>No FACTURA</th><th>VALOR NETO FACTURA</th><th>VALOR RET ICA</th><th>VALOR RET IVA</th><th>VALOR RET RENTA</th><th>VALOR PAGADO</th><th>NOTA</th></tr>'
                    #textoEnvio += "<tr><td>" + reg[3] + "</td><td ALIGN=right>" + reg[8] + "</td><td ALIGN=right>" + reg[4] + "</td><td ALIGN=right>" + reg[5] + "</td><td ALIGN=right>" + reg[6] + "</td><td ALIGN=right>" + reg[7] + "</td><td ALIGN=left>" + reg[9] + "</td></tr>"
           
            #textoEnvio += "</table><br></br></p>Agradecemos distribuir esta informacion al personal de su empresa que le puedan ser util estos datos.</p>"
            #textoEnvio += "<br></br><footer><strong>POR FAVOR NO RESPONDER A ESTA CUENTA DE CORREO, NADIE MONITOREA ESTOS MENSAJES Y SE ELIMINAN AUTOMATICAMENTE.</strong></footer>"
            #listaEnvio.append(textoEnvio)
            sentNotification(notificationCustomId)
    except Exception as ex:
            print ("Error al leer el archivo .csv \n %s " % (ex))
    
    return True
    
def sentNotification(notificationCustomId):
    try:
        supplierTaxIdentificationNumberList =  notificationContent.objects.filter(customId="%s" %notificationCustomId).distinct('taxIdentificationNumber')
         
        for i in range(len(supplierTaxIdentificationNumberList)):
            operationList = supplier.objects.filter(taxIdentificationNumber="%s" % supplierTaxIdentificationNumberList[i])
            contentList = notificationContent.objects.filter(customId="%s" %notificationCustomId).filter(taxIdentificationNumber="%s" %supplierTaxIdentificationNumberList[i])
            #print ("enviado A %s " % (listaControl[i]))
            
            x=0
            
            for filas in operationList:
                if not filas:
                    pass
                    #noEnviado+= "</br>"+(filas[x].nit)+" -- "+(filas[x+1].nombre)
                    #print ("NO SE PUDO ENVIAR CORREO A %s " % ((filas[x].nit)+" -- "+(filas[x+1].nombre)))
                else:
                    if(filas[x+2].email != ""):
                        y+=1
                        try:
                            sendMail(contentList, filas[x+2].email)
                            #models.envioCorreo("no-reply@astivik.com", (filas[x+2].email), listaEnvio[i])
                            #textoEnvioControl += "<tr><td ALIGN=center>" + str(y) + "</td><td ALIGN=left>" + (filas[x+1].nombre) + "</td><td ALIGN=left>" + (filas[x+2].email) + "</td></tr>"
                            #print ("enviado A %s " % ((filas[x].nit)+" -- "+(filas[x+1].nombre)))
                        except Exception as ex:
                            print ("Error al enviar notificacion %s %s" % ((supplierTaxIdentificationNumberList[i]), ex))
                    else:
                        noEnviado+= "</br>"+(filas[x].nit)+" -- "+(filas[x+1].nombre+"</br>")
                                        
                x+=3
    except Exception as ex:
        print ("Error al realizar accion en la base de datos \n %s " % (ex))

    return True


def sendMail(body, to):
    subject = 'Astivik S.A. -- Notificación Pagos Realizados.'
    template = get_template('templates/emailMessage.html')

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

    return True