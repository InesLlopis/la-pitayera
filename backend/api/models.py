from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length = 150, verbose_name = "Nombre")
    tipo = models.CharField(max_length = 250, verbose_name = "Tipo")
    descripcion = models.TextField(verbose_name = "Descripcion")
    precio = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Precio")

class Pedido(models.Model):
    fecha_creacion = models.DateField(auto_now_add = True, verbose_name = "Fecha de creacion")

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE, related_name = "lineas",)
    producto = models.ForeignKey(Producto, on_delete = models.PROTECT, related_name = "lineas_pedido",)
    cantidad = models.PositiveIntegerField(verbose_name = "Cantidad")
    precio_unitario = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Precio unitario")

class Factura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete = models.CASCADE, related_name = "factura",)
    estado = models.CharField(max_length = 30, verbose_name = "Estado")
    fecha_creacion = models.DateField(auto_now_add = True, verbose_name = "Fecha de creacion")

class Cobro(models.Model):
    factura = models.ForeignKey(Factura, on_delete = models.CASCADE, related_name = "cobros",)
    importe = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Importe")
    fecha_abono = models.DateField(auto_now_add = True, verbose_name = "Fecha de abono")
