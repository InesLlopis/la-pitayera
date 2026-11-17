# UD4.3

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Categoria, Producto, Pedido, DetallePedido, MovimientoInventario, TipoMovimiento

# UD4.4.e
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML

# UD4.3.a
class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(CategoriaCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('descripcion'), css_class="col-12"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(CategoriaUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('descripcion'), css_class="col-12"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']
    
    # UD4.3.c
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise ValidationError("El precio no puede ser inferior a 0.")
        return precio
    
    # UD4.4.e
    def __init__(self, *args, **kargs):
        super(ProductoCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-6"),
                Div(Field('sku'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('categoria'), css_class="col-6"),
                Div(Field('precio'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('descripcion'), css_class="col-12"),
                css_class="row"
            ),
        )

# UD4.3.a
class ProductoUpdateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'sku', 'categoria', 'descripcion', 'precio']
    
    # UD4.3.c
    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio < 0:
            raise ValidationError("El precio no puede ser inferior a 0.")
        return precio
    
    
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(ProductoUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-6"),
                Div(Field('sku'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('categoria'), css_class="col-6"),
                Div(Field('precio'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('descripcion'), css_class="col-12"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class PedidoCreateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'n_pedido', 'fecha', 'total']
        
    # UD4.3.c
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.now():
            raise ValidationError("La fecha del pedido no puede ser anterior a la actual.")
        return fecha
    
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(PedidoCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('cliente'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('n_pedido'), css_class="col-4"),
                Div(Field('fecha'), css_class="col-4"),
                Div(Field('total'), css_class="col-4"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class PedidoUpdateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'n_pedido', 'fecha', 'total']
        
    # UD4.3.c
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.now():
            raise ValidationError("La fecha del pedido no puede ser anterior a la actual.")
        return fecha
    
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(PedidoUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('cliente'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('n_pedido'), css_class="col-4"),
                Div(Field('fecha'), css_class="col-4"),
                Div(Field('total'), css_class="col-4"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class DetallePedidoCreateForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']
    
    # UD4.3.c
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == 0:
            raise ValidationError("La cantidad de productos del pedido no puede ser 0.")
        return cantidad
    
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(DetallePedidoCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('pedido'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('producto'), css_class="col-4"),
                Div(Field('cantidad'), css_class="col-4"),
                Div(Field('precio_unitario'), css_class="col-4"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class DetallePedidoUpdateForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']
        
    # UD4.3.c
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == 0:
            raise ValidationError("La cantidad de productos del pedido no puede ser 0.")
        return cantidad
    
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(DetallePedidoUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('pedido'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('producto'), css_class="col-4"),
                Div(Field('cantidad'), css_class="col-4"),
                Div(Field('precio_unitario'), css_class="col-4"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class TipoMovimientoCreateForm(forms.ModelForm):
    class Meta:
        model = TipoMovimiento
        fields = ['nombre', 'motivo']
        
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(TipoMovimientoCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('motivo'), css_class="col-12"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class TipoMovimientoUpdateForm(forms.ModelForm):
    class Meta:
        model = TipoMovimiento
        fields = ['nombre', 'motivo']
        
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(TipoMovimientoUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('motivo'), css_class="col-12"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class MovimientoInventarioCreateForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'tipo', 'fecha', 'cantidad']
        
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(MovimientoInventarioCreateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('tipo'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('producto'), css_class="col-6"),
                Div(Field('cantidad'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('fecha'), css_class="col-12"),
                css_class="row"
            ),
        )
        
# UD4.3.a
class MovimientoInventarioUpdateForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'tipo', 'fecha', 'cantidad']
        
# UD4.4.e
    def __init__(self, *args, **kargs):
        super(MovimientoInventarioUpdateForm, self).__init__(*args, **kargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # UD4.4.d
        self.helper.layout = Layout(
            Div(
                Div(Field('tipo'), css_class="col-12"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('producto'), css_class="col-6"),
                Div(Field('cantidad'), css_class="col-6"),
                css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('fecha'), css_class="col-12"),
                css_class="row"
            ),
        )