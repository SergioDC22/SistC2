from xmlrpc.client import boolean
from django.db import models

# Create your models here.
class  Cliente(models.Model):
    idCli=models.AutoField(primary_key=True)
    CUIT=models.CharField(max_length=11, unique=True)
    claveFiscal=models.CharField(max_length=64, verbose_name="claveFiscal")
    RazonSocial=models.CharField(max_length=50, verbose_name="RazonSocial")
    isEstado=models.BooleanField(default=1)

    def __str__(self):
        fila= "Id Cliente: "+str(self.idCli)+" - "+"CUIT: "+str(self.CUIT)+" - "+"Clave Fiscal: "+str(self.claveFiscal)+" - "+"Razon Social: "+self.RazonSocial+ " - "+"Estado: "+ str(self.isEstado)
        return fila