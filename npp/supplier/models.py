from django.db import models

# Create your models here.

class supplier(models.Model):
    taxIdentificationNumber = models.CharField(max_length=12)
    companyName = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    
    def get_queryset(nit):
        listaRs = []
        listaEnvio = []
        
        records = supplier.objects.filter(nit="%s" % nit)
        #print (records)
        fila = list(records)
        #print (fila[0])
        #records = cursor.fetchall()
    
        for fila in records:
            if  fila:
                listaRs.append(fila[1])
                listaRs.append(fila[2])
                listaRs.append(fila[3])
                
                #print "fila 1: %s fila2: %s Fila3: %s --- ListaRs: %s" % (fila[1], fila[2], fila[3], listaRs)
                listaEnvio.append(listaRs)
            
        return (listaEnvio)
        #return ("fila 1: %s fila2: %s Fila3: %s --- ListaRs: %s" % (fila[1], fila[2], fila[3], listaRs))
        
    def __getitem__(self,index):
        return (self.email)

    def __str__(self):
        return self.nit
