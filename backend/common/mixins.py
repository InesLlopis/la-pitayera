# UD4.2.d

from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse

# UD4.2.g
from billing.models import Cobro
from decimal import Decimal
from django.db.models import Sum


class CreateUpdateContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['titulo_creacion'] = self.titulo_creacion
        context['titulo_actualizacion']= self.titulo_actualizacion
        context['url_borrado'] = self.url_borrado
        
        return context
    
# UD4.2.f
class DeleteMixin:
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, "Existen dependencias para el objeto {}. Elimine antes dichas dependencias".format(str(self.object)))
            return HttpResponseRedirect(reverse('home'))
        
# UD4.2.g
class CobroMixin:
    def form_valid(self, form):
        factura = form.cleaned_data["factura"]
        importe = form.cleaned_data["importe"]
        cobros = Cobro.objects.filter(factura=factura)
        cobro_actual = getattr(self, "object", None)
        
        if cobro_actual is not None:
            cobros = cobros.exclude(pk=cobro_actual.pk)
        
        total_previo = (cobros.aggregate(suma=Sum("importe"))["suma"] or Decimal("0.00"))
        saldo_disponible = factura.total - total_previo
        
        if importe > saldo_disponible:
            form.add_error("importe", f"El cobro ({importe}) supera el saldo pendiente ({saldo_disponible}).")
            return self.form_invalid(form)
        return super().form_valid(form)