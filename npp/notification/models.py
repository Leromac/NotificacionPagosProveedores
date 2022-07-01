from cProfile import label
from django.db import models

class notification(models.Model):
    baseFile = models.FileField(name="baseFile", max_length=500)
    #uploadTo = models.FileField(upload_to='')
    #creationDate = models.DateTimeField(auto_now_add=True)
    

class notificationFields(models.Model):
    pass