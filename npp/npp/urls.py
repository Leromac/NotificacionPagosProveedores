"""npp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unittest.mock import patch
from django.contrib import admin
from django.urls import path
from main import views as m
from supplier import views as s
from notification import views as n


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', m.index, name='index'),
    path('supplier/', s.supplierIndex, name='supplierIndex'),
    path('supplier/search/', s.searchSupplier, name='searchSupplier'),
    path('supplier/add/', s.addSupplier, name='addSupplier'),
    #path('supplier/get/one/', s.getIndividualSupplier, name='getIndividualSupplier'),
    path('notification/', n.notificationIndex, name='notificationIndex'),
]
