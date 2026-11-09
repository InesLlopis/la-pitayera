from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Categoria, Producto, Pedido, DetallePedido, MovimientoInventario, TipoMovimiento

# UD4.2.a
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    template_name = 'core/detallepedido_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class DetallePedidoDetailView(DetailView):
    model = DetallePedido
    template_name = 'core/detallepedido_detail.html'

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
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('categoria_update', kwargs={'pk': object.id})

# UD4.2.a
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre', 'descripcion']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('categoria_update', kwargs={'pk': object.id})

# UD4.2.a
class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    
# UD4.2.a
class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('producto_update', kwargs={'pk': object.id})
    
# UD4.2.a
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('producto_update', kwargs={'pk': object.id})
    
# UD4.2.a
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('producto_list')

# UD4.2.a
class PedidoCreateView(CreateView):
    model = Pedido
    fields = ['cliente', 'n_pedido', 'fecha', 'total']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('pedido_update', kwargs={'pk': object.id})
        
# UD4.2.a
class PedidoUpdateView(UpdateView):
    model = Pedido
    fields = ['cliente', 'n_pedido', 'fecha', 'total']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('pedido_update', kwargs={'pk': object.id})
        
# UD4.2.a
class PedidoDeleteView(DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido_list')
    
# UD4.2.a
class DetallePedidoCreateView(CreateView):
    model = DetallePedido
    fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('detalle_pedido_update', kwargs={'pk': object.id})

# UD4.2.a
class DetallePedidoUpdateView(UpdateView):
    model = DetallePedido
    fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('detalle_pedido_update', kwargs={'pk': object.id})

# UD4.2.a
class DetallePedidoDeleteView(DeleteView):
    model = DetallePedido
    success_url = reverse_lazy('detalle_pedido_list')

# UD4.2.a
class MovimientoInventarioCreateView(CreateView):
    model = MovimientoInventario
    fields = ['producto', 'tipo', 'fecha', 'cantidad']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('movimiento_inventario_update', kwargs={'pk': object.id})

# UD4.2.a
class MovimientoInventarioUpdateView(UpdateView):
    model = MovimientoInventario
    fields = ['producto', 'tipo', 'fecha', 'cantidad']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('movimiento_inventario_update', kwargs={'pk': object.id})

# UD4.2.a
class MovimientoInventarioDeleteView(DeleteView):
    model = MovimientoInventario
    success_url = reverse_lazy('movimiento_inventario_list')

# UD4.2.a
class TipoMovimientoCreateView(CreateView):
    model = TipoMovimiento
    fields = ['nombre', 'motivo']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('tipo_movimiento_update', kwargs={'pk': object.id})

# UD4.2.a
class TipoMovimientoUpdateView(UpdateView):
    model = TipoMovimiento
    fields = ['nombre', 'motivo']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('tipo_movimiento_update', kwargs={'pk': object.id})

# UD4.2.a
class TipoMovimientoDeleteView(DeleteView):
    model = TipoMovimiento
    success_url = reverse_lazy('tipo_movimiento_list')