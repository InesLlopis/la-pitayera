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
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)