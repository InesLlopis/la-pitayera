# UD3.3.a
from decimal import Decimal
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion', blank=True, default="",)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    categoria = models.ForeignKey("core.Categoria", on_delete=models.PROTECT)
    descripcion = models.TextField(verbose_name='Descripcion', blank=True, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"), verbose_name='Precio')

    def __str__(self):
        return self.nombre + " (" + str(self.categoria) + ")"

class Pedido(models.Model):
    cliente = models.ForeignKey("billing.Cliente", on_delete=models.PROTECT)
    n_pedido = models.CharField(max_length=20, unique=True)
    fecha = models.DateField(default=now, verbose_name='Fecha')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"), verbose_name='Total')

    def __str__(self):
        return str(self.cliente) + " - " + self.n_pedido
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"), verbose_name='Precio Unitario')

    def __str__(self):
        return str(self.pedido) + " - " + str(self.producto) + " (" + str(self.cantidad) + ")"
    
class MovimientoInventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    fecha = models.DateField(default=now, verbose_name='Fecha')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')

    def __str__(self):
        return str(self.fecha) + " - " + str(self.producto) + " (" + str(self.cantidad) + ")"

class TipoMovimiento(models.Model):
    movimiento = models.ForeignKey(MovimientoInventario, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    motivo = models.CharField(max_length=256, verbose_name='Motivo')

    def __str__(self):
        return self.nombre + " (" + self.motivo + ")"
