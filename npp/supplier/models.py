from django.db import models
from django.forms import ModelForm

# Create your models here.

class supplier(models.Model):
    taxIdentificationNumber = models.CharField(name="taxIdentificationNumber", max_length=12)
    companyName = models.CharField(name="companyName", max_length=300)
    email = models.EmailField(name="email", max_length=100)