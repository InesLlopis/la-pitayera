# UD4.3

from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, Factura, Cobro

# UD4.4.c
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML

# UD4.3.a
class ClienteCreateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'nif', 'email']
    
    # UD4.4.c
    def __init__(self, *args, **kargs):
        super(ClienteCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-3"),
                Div(Field('apellidos'), css_class="col-6"),
                Div(Field('nif'), css_class="col-3"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('email'), css_class="col-12"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'nif', 'email']
        
    # UD4.4.c
    def __init__(self, *args, **kargs):
        super(ClienteUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-3"),
                Div(Field('apellidos'), css_class="col-6"),
                Div(Field('nif'), css_class="col-3"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('email'), css_class="col-12"),
                css_class="row"
            ),
        )
        
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
    
    # UD4.4.c
    def __init__(self, *args, **kargs):
        super(FacturaCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('cliente'), css_class="col-12"),
                css_class="row",
            ),
            HTML('<hr>'),
            Div(
                Div(Field('n_factura'), css_class="col-4"),
                Div(Field('fecha'), css_class="col-4"),
                Div(Field('total'), css_class="col-4"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('concepto'), css_class="col-12"),
                css_class="row",
            ),
        )

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
    
    # UD4.4.c
    def __init__(self, *args, **kargs):
        super(FacturaCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('cliente'), css_class="col-12"),
                css_class="row",
            ),
            HTML('<hr>'),
            Div(
                Div(Field('n_factura'), css_class="col-4"),
                Div(Field('fecha'), css_class="col-4"),
                Div(Field('total'), css_class="col-4"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('concepto'), css_class="col-12"),
                css_class="row",
            ),
        )
    

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
    
    # UD4.4.c
    def __init__(self, *args, **kargs):
        super(CobroCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('factura'), css_class="col-12"),
                css_class="row",
            ),
            HTML('<hr>'),
            Div(
                Div(Field('fecha'), css_class="col-6"),
                Div(Field('importe'), css_class="col-6"),
                css_class="row"
            ),
        )
        
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
    
    # UD4.4.c
    def __init__(self, *args, **kargs):
        super(CobroUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('factura'), css_class="col-12"),
                css_class="row",
            ),
            HTML('<hr>'),
            Div(
                Div(Field('fecha'), css_class="col-6"),
                Div(Field('importe'), css_class="col-6"),
                css_class="row"
            ),
        )
