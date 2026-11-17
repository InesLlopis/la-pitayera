from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Categoria, Producto, Pedido, DetallePedido, MovimientoInventario, TipoMovimiento

# UD4.2.a
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# UD4.2.d, UD4.2.f, UD4.2.h, UD4.2.i
from common.mixins import CreateUpdateContextMixin, DeleteMixin, PrecioMixin, CantidadMixin, OrderingByIdMixin
from django.contrib.messages.views import SuccessMessageMixin

# UD4.4.e
from .forms import CategoriaCreateUpdateForm, ProductoCreateUpdateForm, PedidoCreateUpdateForm, DetallePedidoCreateUpdateForm, TipoMovimientoCreateUpdateForm, MovimientoInventarioCreateUpdateForm

# Create your views here.
# UD3.7.a
class CategoriaListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = Categoria
    template_name = 'core/categoria_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'core/categoria_detail.html'

# UD3.7.a
class ProductoListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = Producto
    template_name = 'core/producto_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'core/producto_detail.html'

# UD3.7.a
class PedidoListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = Pedido
    template_name = 'core/pedido_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'core/pedido_detail.html'

# UD3.7.a
class DetallePedidoListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = DetallePedido
    template_name = 'core/detalle_pedido_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class DetallePedidoDetailView(DetailView):
    model = DetallePedido
    template_name = 'core/detalle_pedido_detail.html'

# UD3.7.a
class MovimientoInventarioListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = MovimientoInventario
    template_name = 'core/movimiento_inventario_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class MovimientoInventarioDetailView(DetailView):
    model = MovimientoInventario
    template_name = 'core/movimiento_inventario_detail.html'

# UD3.7.a
class TipoMovimientoListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = TipoMovimiento
    template_name = 'core/tipo_movimiento_list.html'
    # UD3.8.b
    paginate_by = 5

# UD3.7.a
class TipoMovimientoDetailView(DetailView):
    model = TipoMovimiento
    template_name = 'core/tipo_movimiento_detail.html'
    
# UD4.2

# UD4.2.a
class CategoriaCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView): # UD4.2.d
    # model = Categoria
    # fields = ['nombre', 'descripcion']
    
    # UD4.4.e
    form_class = CategoriaCreateUpdateForm

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear categoría'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('categoria_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Categoría '{}' creada correctamente".format(str(self.object))

# UD4.2.a
class CategoriaUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = Categoria
    # fields = ['nombre', 'descripcion']
    
    # UD4.4.e
    form_class = CategoriaCreateUpdateForm

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar categoría'
    url_borrado = 'categoria_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('categoria_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Categoría '{}' actualizada correctamente".format(str(self.object))

# UD4.2.a
class CategoriaDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    
    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar categoría'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar esta categoría?'
    
# UD4.2.a
class ProductoCreateView(SuccessMessageMixin, PrecioMixin, CreateUpdateContextMixin, CreateView): # UD4.2.d y UD4.2.h
    # model = Producto
    # fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']
    
    # UD4.4.e
    form_class = ProductoCreateUpdateForm
    
    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear producto'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('producto_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Producto '{}' creado correctamente".format(str(self.object))
    
# UD4.2.a
class ProductoUpdateView(SuccessMessageMixin, PrecioMixin, CreateUpdateContextMixin, UpdateView): # UD4.2.d y UD4.2.h
    model = Producto
    # fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']
    
    # UD4.4.e
    form_class = ProductoCreateUpdateForm

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar producto'
    url_borrado = 'producto_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('producto_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Producto '{}' actualizado correctamente".format(str(self.object))
    
# UD4.2.a
class ProductoDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = Producto
    success_url = reverse_lazy('producto_list')
    
    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar producto'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este producto?'

# UD4.2.a
class PedidoCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView): # UD4.2.d
    # model = Pedido
    # fields = ['cliente', 'n_pedido', 'fecha', 'total']
    
    # UD4.4.e
    form_class = PedidoCreateUpdateForm

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear pedido'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('pedido_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Pedido '{}' creado correctamente".format(str(self.object))
        
# UD4.2.a
class PedidoUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = Pedido
    # fields = ['cliente', 'n_pedido', 'fecha', 'total']
    
    # UD4.4.e
    form_class = PedidoCreateUpdateForm

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar pedido'
    url_borrado = 'pedido_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('pedido_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Pedido '{}' actualizado correctamente".format(str(self.object))
        
# UD4.2.a
class PedidoDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = Pedido
    success_url = reverse_lazy('pedido_list')

    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar pedido'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este pedido?'
    
# UD4.2.a
class DetallePedidoCreateView(SuccessMessageMixin, CantidadMixin, CreateUpdateContextMixin, CreateView): # UD4.2.d y UD4.2.h
    # model = DetallePedido
    # fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']
    
    # UD4.4.e
    form_class = DetallePedidoCreateUpdateForm

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear detalle de pedido'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('detalle_pedido_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Detalle de pedido '{}' creado correctamente".format(str(self.object))

# UD4.2.a
class DetallePedidoUpdateView(SuccessMessageMixin, CantidadMixin, CreateUpdateContextMixin, UpdateView): # UD4.2.d y UD4.2.h
    model = DetallePedido
    # fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']
    
    # UD4.4.e
    form_class = DetallePedidoCreateUpdateForm

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar detalle de pedido'
    url_borrado = 'detalle_pedido_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('detalle_pedido_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Detalle de pedido '{}' actualizado correctamente".format(str(self.object))

# UD4.2.a
class DetallePedidoDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = DetallePedido
    success_url = reverse_lazy('detalle_pedido_list')

    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar detalle de pedido'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este detalle de pedido?'

# UD4.2.a
class MovimientoInventarioCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView): # UD4.2.d
    # model = MovimientoInventario
    # fields = ['producto', 'tipo', 'fecha', 'cantidad']
    
    # UD4.4.e
    form_class = MovimientoInventarioCreateUpdateForm

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear movimiento de inventario'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('movimiento_inventario_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Movimiento de inventario '{}' creado correctamente".format(str(self.object))

# UD4.2.a
class MovimientoInventarioUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = MovimientoInventario
    # fields = ['producto', 'tipo', 'fecha', 'cantidad']
    
    # UD4.4.e
    form_class = MovimientoInventarioCreateUpdateForm

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar movimiento de inventario'
    url_borrado = 'movimiento_inventario_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('movimiento_inventario_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Movimiento de inventario '{}' actualizado correctamente".format(str(self.object))

# UD4.2.a
class MovimientoInventarioDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = MovimientoInventario
    success_url = reverse_lazy('movimiento_inventario_list')

    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar movimiento de inventario'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este movimiento de inventario?'

# UD4.2.a
class TipoMovimientoCreateView(SuccessMessageMixin, CreateUpdateContextMixin, CreateView): # UD4.2.d
    # model = TipoMovimiento
    # fields = ['nombre', 'motivo']
    
    # UD4.4.e
    form_class = TipoMovimientoCreateUpdateForm

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear tipo de movimiento'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('tipo_movimiento_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Tipo de movimiento '{}' creado correctamente".format(str(self.object))

# UD4.2.a
class TipoMovimientoUpdateView(SuccessMessageMixin, CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = TipoMovimiento
    # fields = ['nombre', 'motivo']
    
    # UD4.4.e
    form_class = TipoMovimientoCreateUpdateForm

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar tipo de movimiento'
    url_borrado = 'tipo_movimiento_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('tipo_movimiento_update', kwargs={'pk': object.id})

    # UD4.4.a
    def get_success_message(self, cleaned_data):
        return "Tipo de movimiento '{}' actualizado correctamente".format(str(self.object))

# UD4.2.a
class TipoMovimientoDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = TipoMovimiento
    success_url = reverse_lazy('tipo_movimiento_list')

    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar tipo de movimiento'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este tipo de movimiento?'