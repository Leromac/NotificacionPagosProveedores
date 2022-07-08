from django.db import models

# Create your models here.
class log(models.Model):
    sendedNotificationDate = models.DateTimeField(name="sendedNotificationDate", auto_now=True)
    customIdNotification = models.CharField(name="customIdNotification", max_length=50)