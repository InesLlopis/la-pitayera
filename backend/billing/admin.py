from django.contrib import admin
from .models import Cliente, Factura, Cobro

# Register your models here.
# UD3.4.b
class ClienteAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('nombre', 'apellidos', 'nif', 'email') # UD3.4.a list_display son las columnas que se muestran en la tabla del administrador, list_display_link permite que se pueda hacer click en ellas y se puedan editar
    list_filter = ('nif',) # UD3.4.a permite filtrar los datos según el criterio dado
    search_fields = ('nombre', 'apellidos', 'nif', 'email') # UD3.4.a campos de búsqueda de datos
    preserve_filters = True # UD3.4.a conserva los filtros aplicados al volver a la lista después de abrir un registro

# UD3.4.b
class FacturaAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('n_factura', 'fecha', 'total') # UD3.4.a list_display son las columnas que se muestran en la tabla del administrador, list_display_link permite que se pueda hacer click en ellas y se puedan editar
    list_filter = ('cliente',) # UD3.4.a permite filtrar los datos según el criterio dado
    search_fields = ('n_factura', 'cliente__nombre', 'cliente__apellidos') # UD3.4.a campos de búsqueda de datos
    preserve_filters = True # UD3.4.a conserva los filtros aplicados al volver a la lista después de abrir un registro

# UD3.4.b
class CobroAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('get_n_factura', 'fecha', 'importe') # UD3.4.a list_display son las columnas que se muestran en la tabla del administrador, list_display_link permite que se pueda hacer click en ellas y se puedan editar
    list_filter = ('factura__cliente',) # UD3.4.a permite filtrar los datos según el criterio dado
    search_fields = ('factura__n_factura', 'factura__cliente__nombre', 'factura__cliente__apellidos') # UD3.4.a campos de búsqueda de datos
    preserve_filters = True # UD3.4.a conserva los filtros aplicados al volver a la lista después de abrir un registro

    @admin.display(description="Nº factura") # busca el numero de una factura y lo devuelve
    def get_n_factura(self, obj):            # para que list_display pueda mostrarlo
        return obj.factura.n_factura


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Cobro, CobroAdmin)