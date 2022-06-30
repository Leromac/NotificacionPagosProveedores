from django.db import models

class notification(models.Model):
    baseFile = models.FileField(name="baseFile", max_length=50)

class notificationFields(models.Model):
    pass