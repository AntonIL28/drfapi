from django.contrib import admin

# Register your models here.
from .models import Cliente, UnidadMedida


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id_cliente', 'descripcion')


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
	list_display = ('id', 'descripcion')
