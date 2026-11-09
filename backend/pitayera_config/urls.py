"""avaluapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from common import views as common_views
from billing import views as billing_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', common_views.HomeView.as_view(), name='home'),
    path('panel/', common_views.PanelView.as_view(), name='panel'),

    path('cliente_list/', billing_views.ClienteListView.as_view(), name='cliente_list'),
    path('cliente_detail/<int:pk>/', billing_views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('factura_list/', billing_views.FacturaListView.as_view(), name='factura_list'),
    path('factura_detail/<int:pk>/', billing_views.FacturaDetailView.as_view(), name='factura_detail'),
    path('cobro_list/', billing_views.CobroListView.as_view(), name='cobro_list'),
    path('cobro_detail/<int:pk>/', billing_views.CobroDetailView.as_view(), name='cobro_detail'),

    # UD4.2.b
    path('cliente_create/', billing_views.ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente_update/', billing_views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente_delete/', billing_views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('factura_create/', billing_views.FacturaCreateView.as_view(), name='factura_create'),
    path('factura_update/', billing_views.FacturaUpdateView.as_view(), name='factura_update'),
    path('factura_delete/', billing_views.FacturaDeleteView.as_view(), name='factura_delete'),
    path('cobro_create/', billing_views.CobroCreateView.as_view(), name='cobro_create'),
    path('cobro_update/', billing_views.CobroUpdateView.as_view(), name='cobro_update'),
    path('cobro_delete/', billing_views.CobroDeleteView.as_view(), name='cobro_delete'),


    # UD3.7.b
    path('categoria_list/', core_views.CategoriaListView.as_view(),name="categoria_list"),
    path('categoria_detail/<int:pk>/', core_views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('producto_list/', core_views.ProductoListView.as_view(), name='producto_list'),
    path('producto_detail/<int:pk>/', core_views.ProductoDetailView.as_view(), name='producto_detail'),
    path('pedido_list/', core_views.PedidoListView.as_view(), name='pedido_list'),
    path('pedido_detail/<int:pk>/', core_views.PedidoDetailView.as_view(), name='pedido_detail'),
    path('detallepedido_list/', core_views.DetallePedidoListView.as_view(), name='detallepedido_list'),
    path('detallepedido_detail/<int:pk>/', core_views.DetallePedidoDetailView.as_view(), name='detallepedido_detail'),
    path('movimientoinventario_list/', core_views.MovimientoInventarioListView.as_view(), name='movimientoinventario_list'),
    path('movimientoinventario_detail/<int:pk>/', core_views.MovimientoInventarioDetailView.as_view(), name='movimientoinventario_detail'),
    path('tipomovimiento_list/', core_views.TipoMovimientoListView.as_view(), name='tipomovimiento_list'),
    path('tipomovimiento_detail/<int:pk>/', core_views.TipoMovimientoDetailView.as_view(), name='tipomovimiento_detail'),
    
    # UD4.2.b
    path('categoria_create/', core_views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria_update/', core_views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria_delete/', core_views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('producto_create/', core_views.ProductoCreateView.as_view(), name='producto_create'),
    path('producto_update/', core_views.ProductoUpdateView.as_view(), name='producto_update'),
    path('producto_delete/', core_views.ProductoDeleteView.as_view(), name='producto_delete'),
    path('pedido_create/', core_views.PedidoCreateView.as_view(), name='pedido_create'),
    path('pedido_update/', core_views.PedidoUpdateView.as_view(), name='pedido_update'),
    path('pedido_delete/', core_views.PedidoDeleteView.as_view(), name='pedido_delete'),
    path('detalle_pedido_create/', core_views.DetallePedidoCreateView.as_view(), name='detalle_pedido_create'),
    path('detalle_pedido_update/', core_views.DetallePedidoUpdateView.as_view(), name='detalle_pedido_update'),
    path('detalle_pedido_delete/', core_views.DetallePedidoDeleteView.as_view(), name='detalle_pedido_delete'),
    path('movimiento_inventario_create/', core_views.MovimientoInventarioCreateView.as_view(), name='movimiento_inventario_create'),
    path('movimiento_inventario_update/', core_views.MovimientoInventarioUpdateView.as_view(), name='movimiento_inventario_update'),
    path('movimiento_inventario_delete/', core_views.MovimientoInventarioDeleteView.as_view(), name='movimiento_inventario_delete'),
    path('tipo_movimiento_create/', core_views.TipoMovimientoCreateView.as_view(), name='tipo_movimiento_create'),
    path('tipo_movimiento_update/', core_views.TipoMovimientoUpdateView.as_view(), name='tipo_movimiento_update'),
    path('tipo_movimiento_delete/', core_views.TipoMovimientoDeleteView.as_view(), name='tipo_movimiento_delete'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)