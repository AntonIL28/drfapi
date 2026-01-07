from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Cliente, UnidadMedida, Pedido, Categoria


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id_cliente', 'descripcion')


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
	list_display = ('id', 'descripcion')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	list_display = ('id_pedido', 'cliente', 'productos', 'estatus','created_at', 'total')
	list_filter = ('estatus', 'cliente')
	search_fields = ('folio', 'productos')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id', 'description')