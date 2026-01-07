from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Cliente, Proveedor, UnidadMedida, Pedido, Categoria, Product, Marca


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

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('codigoprov', 'descripcion', 'upc1', 'upc2', 'mult1', 'mult2', 'unidad_medida1', 'unidad_medida2', 'categoria', 'precio', 'created_at')
	list_filter = ('categoria', 'codigoprov')
	search_fields = ('descripcion', 'upc1', 'upc2')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('id', 'description')
	search_fields = ('description',)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
	list_display = ('id', 'description')
	search_fields = ('description',)