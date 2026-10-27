# UD3.3.a

from django.db import models
from django.utils.timezone import now

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    apellidos = models.CharField(max_length=512, verbose_name='Apellidos')
    nif = models.CharField(max_length=20, verbose_name='NIF', unique=True) # UD3.3.c
    email = models.EmailField(unique=True)

    # UD3.3.c
    class Meta:
        verbose_name = 'Cliente' # UD3.4.e
        verbose_name_plural = 'Clientes' # UD3.4.e
        ordering = ['apellidos', 'nombre'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return self.nombre + " " + self.apellidos + " (" + self.nif + ")"

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    n_factura = models.CharField(max_length=20, verbose_name='Nº Factura', unique=True) # UD3.3.c
    concepto = models.TextField(verbose_name='Concepto')
    fecha = models.DateField(default=now, verbose_name='Fecha')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Total')

    # UD3.3.c
    class Meta:
        verbose_name = 'Factura' # UD3.4.e
        verbose_name_plural = 'Facturas' # UD3.4.e
        ordering = ['n_factura'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return str(self.cliente) + " - " + self.n_factura

class Cobro(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    fecha = models.DateField(default=now, verbose_name='Fecha')
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # UD3.3.c
    class Meta:
        verbose_name = 'Cobro' # UD3.4.e
        verbose_name_plural = 'Cobros' # UD3.4.e
        ordering = ['-fecha'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return str(self.factura.n_factura) + " - " + str(self.importe)
