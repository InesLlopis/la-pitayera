from django.shortcuts import render
from django.views.generic import ListView, DetailView
from billing.models import Cliente, Factura, Cobro

# UD4.2.a
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class ClienteListView(ListView):
    model = Cliente
    template_name = 'billing/cliente_list.html'
    # UD3.8.b
    paginate_by = 5


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'billing/cliente_detail.html'


class FacturaListView(ListView):
    model = Factura
    template_name = 'billing/factura_list.html'
    # UD3.8.b
    paginate_by = 5


class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'billing/factura_detail.html'


class CobroListView(ListView):
    model = Cobro
    template_name = 'billing/cobro_list.html'
    # UD3.8.b
    paginate_by = 5


class CobroDetailView(DetailView):
    model = Cobro
    template_name = 'billing/cobro_detail.html'


# UD4.2

# UD4.2.a
class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellidos', 'nif', 'email']
    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('cliente_update', kwargs={'pk': object.id})

# UD4.2.a
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellidos', 'nif', 'email']

    
    def get_success_url(self):
        object = self.object
        return reverse_lazy('cliente_update', kwargs={'pk': object.id})

# UD4.2.a
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')

# UD4.2.a
class FacturaCreateView(CreateView):
    model = Factura
    fields = ['cliente', 'n_factura', 'concepto', 'fecha', 'total']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('factura_update', kwargs={'pk': object.id})

# UD4.2.a
class FacturaUpdateView(UpdateView):
    model = Factura
    fields = ['cliente', 'n_factura', 'concepto', 'fecha', 'total']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('factura_update', kwargs={'pk': object.id})

# UD4.2.a
class FacturaDeleteView(DeleteView):
    model = Factura
    success_url = reverse_lazy('factura_list')

# UD4.2.a
class CobroCreateView(CreateView):
    model = Cobro
    fields = ['factura', 'fecha', 'importe']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('cobro_update', kwargs={'pk': object.id})

# UD4.2.a
class CobroUpdateView(UpdateView):
    model = Cobro
    fields = ['factura', 'fecha', 'importe']

    def get_success_url(self):
        object = self.object
        return reverse_lazy('cobro_update', kwargs={'pk': object.id})

# UD4.2.a
class CobroDeleteView(DeleteView):
    model = Cobro
    success_url = reverse_lazy('cobro_list')