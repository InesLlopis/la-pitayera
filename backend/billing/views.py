from django.shortcuts import render
from django.views.generic import ListView, DetailView
from billing.models import Cliente, Factura, Cobro

# UD4.2.a
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# UD4.2.d, UD4.2.f, UD4.2.h, UD4.2.i
from common.mixins import CreateUpdateContextMixin, DeleteMixin, CobroMixin, OrderingByIdMixin



class ClienteListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = Cliente
    template_name = 'billing/cliente_list.html'
    # UD3.8.b
    paginate_by = 5


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'billing/cliente_detail.html'


class FacturaListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = Factura
    template_name = 'billing/factura_list.html'
    # UD3.8.b
    paginate_by = 5


class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'billing/factura_detail.html'


class CobroListView(OrderingByIdMixin, ListView): # UD4.2.i
    model = Cobro
    template_name = 'billing/cobro_list.html'
    # UD3.8.b
    paginate_by = 5


class CobroDetailView(DetailView):
    model = Cobro
    template_name = 'billing/cobro_detail.html'


# UD4.2

# UD4.2.a
class ClienteCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = Cliente
    fields = ['nombre', 'apellidos', 'nif', 'email']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear cliente'
    titulo_actualizacion = None
    url_borrado = None
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('cliente_update', kwargs={'pk': object.id})
    
    # UD4.4.a
    def get_success_message(self):
            return "'{}' creado correctamente".format(str(self.object))

# UD4.2.a
class ClienteUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = Cliente
    fields = ['nombre', 'apellidos', 'nif', 'email']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cliente'
    url_borrado = 'cliente_delete'

    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('cliente_update', kwargs={'pk': object.id})
    
    # UD4.4.a
    def get_success_message(self):
        return "'{}' actualizado correctamente".format(str(self.object))

# UD4.2.a
class ClienteDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = Cliente
    success_url = reverse_lazy('cliente_list')
    
    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar cliente'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este cliente?'


# UD4.2.a
class FacturaCreateView(CreateUpdateContextMixin, CreateView): # UD4.2.d
    model = Factura
    fields = ['cliente', 'n_factura', 'concepto', 'fecha', 'total']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear factura'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('factura_update', kwargs={'pk': object.id})
    
    # UD4.4.a
    def get_success_message(self):
            return "'{}' creada correctamente".format(str(self.object))
        
    
# UD4.2.a
class FacturaUpdateView(CreateUpdateContextMixin, UpdateView): # UD4.2.d
    model = Factura
    fields = ['cliente', 'n_factura', 'concepto', 'fecha', 'total']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar factura'
    url_borrado = 'factura_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('factura_update', kwargs={'pk': object.id})
    
    # UD4.4.a
    def get_success_message(self):
        return "'{}' actualizada correctamente".format(str(self.object))

# UD4.2.a
class FacturaDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = Factura
    success_url = reverse_lazy('factura_list')
    
    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar factura'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar esta factura?'


# UD4.2.a
class CobroCreateView(CobroMixin, CreateUpdateContextMixin, CreateView): # UD4.2.d y UD4.2.g
    model = Cobro
    fields = ['factura', 'fecha', 'importe']

    # UD4.2.c    
    template_name = 'common/base_create_update.html'
    titulo_creacion = 'Crear cobro'
    titulo_actualizacion = None
    url_borrado = None

    def get_success_url(self):
        object = self.object
        return reverse_lazy('cobro_update', kwargs={'pk': object.id})
    
    # 4.4.a
    def get_success_message(self):
        return "'{}' creado correctamente".format(str(self.object))


# UD4.2.a
class CobroUpdateView(CobroMixin, CreateUpdateContextMixin, UpdateView): # UD4.2.d y UD4.2.g
    model = Cobro
    fields = ['factura', 'fecha', 'importe']

    # UD4.2.c
    template_name = 'common/base_create_update.html'
    titulo_creacion = None
    titulo_actualizacion = 'Actualizar cobro'
    url_borrado = 'cobro_delete'

    def get_success_url(self):
        object = self.object
        return reverse_lazy('cobro_update', kwargs={'pk': object.id})
    
    # UD4.4.a
    def get_success_message(self):
        return "'{}' actualizado correctamente".format(str(self.object))

# UD4.2.a
class CobroDeleteView(DeleteMixin, DeleteView): # UD4.2.f
    model = Cobro
    success_url = reverse_lazy('cobro_list')
    
    # UD4.2.e
    template_name = 'common/base_confirm_delete.html'
    titulo = 'Eliminar cobro'
    mensaje_confirmacion = '¿Estás seguro de que deseas eliminar este cobro?'
