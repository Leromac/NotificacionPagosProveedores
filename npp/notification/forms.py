from django import forms
from .models import notification

class sendNotificationForm(forms.ModelForm):
    
    class Meta:
        model = notification
        
        fields = [
            'baseFile',
            ]
        labels = {
            'baseFile': ('Archivo .csv a procesar '),
            }
