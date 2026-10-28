# UD3.6
from django.db.models import F, CharField
from django.db.models.functions import Cast
from django.utils import timezone
from datetime import timedelta

from billing.models import Cliente, Factura, Cobro

# UD3.6.1
def get_clientes_all():
    return Cliente.objects.all()

# UD3.6.2
def get_factura_first_3():
    return Factura.objects.all()[:3]

# UD3.6.3
def get_factura_0():
    return Factura.objects.filter(total=0)

# UD3.6.4
def get_cliente_not_74():
    return Cliente.objects.exclude(nif__startswith="74")

# UD3.6.5
def get_cliente_nif_apellido():
    return Cliente.objects.filter(nif__exact="92436593F", apellidos__contains="Pérez")

# UD3.6.6
def get_fact_id_lt_2_num_fact_des():
    return Factura.objects.filter(id__lt=2).order_by("-n_factura")

# UD3.6.7
def get_cli_id_gt_2():
    return Cliente.objects.filter(id__gt=2)

# UD3.6.8
def get_fact_des_nom_des():
    return Factura.objects.filter(concepto__contains="PHP").order_by("n_factura")

# UD3.6.9
def get_fact_not_1():
    return Factura.objects.exclude(n_factura__endswith="1")
# UD3.6.10
def get_cobro_python_id2():
    return Cobro.objects.annotate(id_str=Cast('id', CharField())).filter(factura__concepto__contains="python", id_str__endswith="2").first()

# UD3.6.11
def get_cobro_fact6_not_manu():
    return Cobro.objects.filter(factura__n_factura__contains="06").exclude(factura__cliente__nombre__contains="Manu")

# UD3.6.12
def get_fact_gt_5():
    return Factura.objects.filter(total__gte=5)

# UD3.6.13
def get_cobro_5_10():
    return Cobro.objects.filter(importe__range=(5, 10))

# UD3.6.14
def create_cliente():
    return Cliente.objects.create(nombre="Nuevo", apellidos="apellido1 apellido2", nif="741852963")

# UD3.6.15
def create_factura(cliente):
    ayer = timezone.now().date() - timedelta(days=1)
    return Factura.objects.create(cliente=cliente, n_factura="5", concepto="Pedido de ejemplo", fecha=ayer, total=100)

# UD3.6.16
def update_last_factura():
    factura = Factura.objects.latest("fecha")
    factura.concepto += "(última)"
    factura.save(update_fields=["concepto"])
    return factura

# UD3.6.17
def update_cobro_fact2_x2():
    return Cobro.objects.filter(factura__n_factura__endswith="2").update(importe=F("importe")*2)

# UD3.6.18
def update_cobro_fact1_cligonz_div2():
    return Cobro.objects.filter(factura__n_factura__endswith="1", factura__cliente__apellidos__contains="González").update(importe=F("importe")/2)

# UD3.6.19
def delete_cobro_fact_lt_1():
    return Cobro.objects.filter(factura__total__lt=1).delete()

# UD3.6.20
def delete_cobro_cli_pablo():
    return Cobro.objects.filter(factura__cliente__nombre__contains="Pablo").delete()