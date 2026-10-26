# UD3.3.a

from django.db import models
from django.utils.timezone import now

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    apellidos = models.CharField(max_length=512, verbose_name='Apellidos')
    nif = models.CharField(max_length=20, verbose_name='NIF', unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos + " (" + self.nif + ")"

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
   # pedido = models.ForeignKey("core.Pedido", on_delete=models.PROTECT, null=True, blank=True)
    n_factura = models.CharField(max_length=20, verbose_name='Nº Factura', unique=True)
    concepto = models.TextField(verbose_name='Concepto')
    fecha = models.DateField(default=now, verbose_name='Fecha')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Total')

    def __str__(self):
        return str(self.cliente) + " - " + self.n_factura

class Cobro(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    fecha = models.DateField(default=now, verbose_name='Fecha')
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.factura.n_factura) + " - " + str(self.importe)
