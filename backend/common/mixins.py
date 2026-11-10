# UD4.2.d

from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse


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
            messages.error(
                self.request, f"Existen dependencias para el objeto {self.object}. Elimine antes dichas dependencias"
                )
            return HttpResponseRedirect(reverse('home'))
