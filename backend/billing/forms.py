# UD4.3

from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, Factura, Cobro

# UD4.3.a
class ClienteCreateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'nif', 'email']
        
# UD4.3.a
class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'nif', 'email']
        
# UD4.3.a
class FacturaCreateForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente', 'n_factura', 'concepto', 'fecha', 'total']
        
    # UD4.3.b
    def clean_importe(self):
        total = self.cleaned_data['total']
        if total < 0:
            raise ValidationError("El importe no puede ser inferior a 0.00.")
        return total

# UD4.3.a
class FacturaUpdateForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente', 'n_factura', 'concepto', 'fecha', 'total']
        # UD4.3.b
    def clean_importe(self):
        total = self.cleaned_data['total']
        if total < 0:
            raise ValidationError("El total no puede ser inferior a 0.00.")
        return total

# UD4.3.a
class CobroCreateForm(forms.ModelForm):
    class Meta:
        model = Cobro
        fields = ['factura', 'fecha', 'importe']
        
        # UD4.3.b
    def clean_importe(self):
        importe = self.cleaned_data['importe']
        if importe < 0:
            raise ValidationError("El importe no puede ser inferior a 0.00.")
        return importe
        
# UD4.3.a
class CobroUpdateForm(forms.ModelForm):
    class Meta:
        model = Cobro
        fields = ['factura', 'fecha', 'importe']
        
        # UD4.3.b
    def clean_importe(self):
        importe = self.cleaned_data['importe']
        if importe < 0:
            raise ValidationError("El importe no puede ser inferior a 0.00.")
        return importe
