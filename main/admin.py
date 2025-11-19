from django.contrib import admin

# Register your models here.
from .models import Cliente, UnidadMedida, Pedido


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id_cliente', 'descripcion')


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
	list_display = ('id', 'descripcion')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display = ('id_pedido', 'folio', 'cliente', 'productos', 'estatus','fecha')
	list_filter = ('estatus', 'cliente')
	search_fields = ('folio', 'productos')
