from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Categoria, Producto, Pedido, DetallePedido, MovimientoInventario, TipoMovimiento

# UD4.2.a
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# UD4.2.d
from common.mixins import CreateUpdateContextMixin


# Create your views here.
# UD3.7.a
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'core/categoria_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'core/categoria_detail.html'

# UD3.7.a
class ProductoListView(ListView):
    model = Producto
    template_name = 'core/producto_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'core/producto_detail.html'

# UD3.7.a
class PedidoListView(ListView):
    model = Pedido
    template_name = 'core/pedido_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'core/pedido_detail.html'

# UD3.7.a
class DetallePedidoListView(ListView):
    model = DetallePedido
    template_name = 'core/detalle_pedido_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class DetallePedidoDetailView(DetailView):
    model = DetallePedido
    template_name = 'core/detalle_pedido_detail.html'

# UD3.7.a
class MovimientoInventarioListView(ListView):
    model = MovimientoInventario
    template_name = 'core/movimientoinventario_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class MovimientoInventarioDetailView(DetailView):
    model = MovimientoInventario
    template_name = 'core/movimientoinventario_detail.html'

# UD3.7.a
class TipoMovimientoListView(ListView):
    model = TipoMovimiento
    template_name = 'core/tipomovimiento_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class TipoMovimientoDetailView(DetailView):
    model = TipoMovimiento
    template_name = 'core/tipomovimiento_detail.html'
    
# UD4.2

# UD4.2.a
class CategoriaCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = Categoria
    fields = ['nombre', 'descripcion']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear categoria'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('categoria_update', kwargs={'pk': object.id})

# UD4.2.a
class CategoriaUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = Categoria
    fields = ['nombre', 'descripcion']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar categoria'
    url_borrado = 'categoria_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('categoria_update', kwargs={'pk': object.id})

# UD4.2.a
class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar categoria'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este producto?'
    
# UD4.2.a
class ProductoCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = Producto
    fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear producto'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('producto_update', kwargs={'pk': object.id})
    
# UD4.2.a
class ProductoUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = Producto
    fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar producto'
    url_borrado = 'producto_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('producto_update', kwargs={'pk': object.id})
    
# UD4.2.a
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto_list')
    
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar producto'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este producto?'

# UD4.2.a
class PedidoCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = Pedido
    fields = ['cliente', 'n_pedido', 'fecha', 'total']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear pedido'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('pedido_update', kwargs={'pk': object.id})
        
# UD4.2.a
class PedidoUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = Pedido
    fields = ['cliente', 'n_pedido', 'fecha', 'total']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar pedido'
    url_borrado = 'pedido_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('pedido_update', kwargs={'pk': object.id})
        
# UD4.2.a
class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido_list')

    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar pedido'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este pedido?'
    
# UD4.2.a
class DetallePedidoCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = DetallePedido
    fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear detalle de pedido'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('detalle_pedido_update', kwargs={'pk': object.id})

# UD4.2.a
class DetallePedidoUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = DetallePedido
    fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar detalle de pedido'
    url_borrado = 'detalle_pedido_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('detalle_pedido_update', kwargs={'pk': object.id})

# UD4.2.a
class DetallePedidoDeleteView(DeleteView):
    model = DetallePedido
    success_url = reverse_lazy('detalle_pedido_list')

    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar categoria'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este producto?'

# UD4.2.a
class MovimientoInventarioCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = MovimientoInventario
    fields = ['producto', 'tipo', 'fecha', 'cantidad']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear movimiento de inventario'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('movimiento_inventario_update', kwargs={'pk': object.id})

# UD4.2.a
class MovimientoInventarioUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = MovimientoInventario
    fields = ['producto', 'tipo', 'fecha', 'cantidad']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar movimiento de inventario'
    url_borrado = 'movimiento_inventario_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('movimiento_inventario_update', kwargs={'pk': object.id})

# UD4.2.a
class MovimientoInventarioDeleteView(DeleteView):
    model = MovimientoInventario
    success_url = reverse_lazy('movimiento_inventario_list')

    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar categoria'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este producto?'

# UD4.2.a
class TipoMovimientoCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = TipoMovimiento
    fields = ['nombre', 'motivo']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear tipo de movimiento'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('tipo_movimiento_update', kwargs={'pk': object.id})

# UD4.2.a
class TipoMovimientoUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = TipoMovimiento
    fields = ['nombre', 'motivo']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar tipo de movimiento'
    url_borrado = 'tipo_movimiento_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('tipo_movimiento_update', kwargs={'pk': object.id})

# UD4.2.a
class TipoMovimientoDeleteView(DeleteView):
    model = TipoMovimiento
    success_url = reverse_lazy('tipo_movimiento_list')

    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar categoria'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este producto?'