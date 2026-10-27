# UD3.3.a
from decimal import Decimal
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción', blank=True, default="",)

    # UD3.3.c
    class Meta:
        verbose_name = 'Categoría' # UD3.4.e
        verbose_name_plural = 'Categorías' # UD3.4.e
        ordering = ['nombre'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    sku = models.CharField(max_length=20, verbose_name='SKU', unique=True) # UD3.3.c
    categoria = models.ForeignKey("core.Categoria", on_delete=models.PROTECT)
    descripcion = models.TextField(verbose_name='Descripción', blank=True, default="")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"), verbose_name='Precio')

    # UD3.3.c
    class Meta:
        verbose_name = 'Producto' # UD3.4.e
        verbose_name_plural = 'Productos' # UD3.4.e
        ordering = ['nombre', 'sku'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return self.nombre + " (" + str(self.categoria) + ")"

class Pedido(models.Model):
    cliente = models.ForeignKey("billing.Cliente", on_delete=models.PROTECT)
    n_pedido = models.CharField(max_length=20, unique=True) # UD3.3.c
    fecha = models.DateField(default=now, verbose_name='Fecha')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"), verbose_name='Total')

    # UD3.3.c
    class Meta:
        verbose_name = 'Pedido' # UD3.4.e
        verbose_name_plural = 'Pedidos' # UD3.4.e
        ordering = ['n_pedido', '-fecha'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return str(self.cliente) + " - " + self.n_pedido
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"), verbose_name='Precio Unitario')

    # UD3.3.c
    class Meta:
        unique_together = ('pedido', 'producto') # UD3.3.c
        verbose_name = 'Detalle de Pedido' # UD3.4.e
        verbose_name_plural = 'Detalles de Pedido' # UD3.4.e
        ordering = ['pedido', 'producto'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return str(self.pedido) + " - " + str(self.producto) + " (" + str(self.cantidad) + ")"
    
class TipoMovimiento(models.Model):
    # movimiento = models.ForeignKey(MovimientoInventario, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=256, verbose_name='Nombre')
    motivo = models.CharField(max_length=256, verbose_name='Motivo')

    # UD3.3.c
    class Meta:
        verbose_name = 'Tipo de Movimiento' # UD3.4.e
        verbose_name_plural = 'Tipos de Movimiento' # UD3.4.e
        ordering = ['nombre'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return self.nombre + " (" + self.motivo + ")"

class MovimientoInventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoMovimiento, on_delete=models.PROTECT)
    fecha = models.DateField(default=now, verbose_name='Fecha')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad')

    # UD3.3.c
    class Meta:
        verbose_name = 'Movimiento de Inventario' # UD3.4.e
        verbose_name_plural = 'Movimientos de Inventario' # UD3.4.e
        ordering = ['-fecha'] # UD3.4.f

    # UD3.3.b
    def __str__(self):
        return str(self.fecha) + " - " + str(self.tipo) + " - " + str(self.producto) + " (" + str(self.cantidad) + ")"

