from django.contrib import admin
from .models import Categoria, Producto, Pedido, DetallePedido, MovimientoInventario, TipoMovimiento

# Register your models here.
# UD3.4.c
class CategoriaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'descripcion')
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    preserve_filters = True

# UD3.4.c
class ProductoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'sku', 'get_categoria', 'descripcion', 'precio')
    list_filter = ('nombre', 'sku',)
    search_fields = ('nombre', 'sku', 'categoria__nombre')
    preserve_filters = True

    @admin.display(description="Categoria")
    def get_categoria(self, obj):
        return obj.categoria.nombre    

# UD3.4.c
class PedidoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('n_pedido', 'fecha', 'total')
    list_filter = ('cliente',)
    search_fields = ('n_pedido', 'cliente__nombre', 'cliente__apellidos')
    date_hierarchy = ('fecha') # UD3.4.a filtra los datos por fecha
    preserve_filters = True

# UD3.4.c
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('get_n_pedido', 'cantidad', 'precio_unitario')
    list_filter = ('pedido',)
    search_fields = ('pedido__n_pedido', 'producto__nombre')
    preserve_filters = True

    @admin.display(description="Nº Pedido")
    def get_n_pedido(self, obj):
        return obj.pedido.n_pedido

# UD3.4.c
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'motivo')
    list_filter = ('nombre',)
    search_fields = ('nombre',)
    preserve_filters = True

# UD3.4.c
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('tipo', 'fecha', 'cantidad')
    list_filter = ('tipo',)
    search_fields = ('tipo__nombre',)
    date_hierarchy = ('fecha') # UD3.4.a filtra los datos por fecha
    preserve_filters = True

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)
admin.site.register(MovimientoInventario, MovimientoInventarioAdmin)
admin.site.register(TipoMovimiento, TipoMovimientoAdmin)
