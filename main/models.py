from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    codigoprov = models.ForeignKey('Proveedor', null=True, blank=True, on_delete=models.SET_NULL, related_name='products', db_column='codigoprov')
    descripcion = models.CharField(max_length=255)
    upc1 = models.CharField(max_length=100)
    upc2 = models.CharField(max_length=100)
    mult1 = models.IntegerField(default=0)
    mult2 = models.IntegerField(default=0)
    unidad_medida1 = models.ForeignKey('UnidadMedida', null=True, blank=True, on_delete=models.SET_NULL, related_name='products_unidad1')
    unidad_medida2 = models.ForeignKey('UnidadMedida', null=True, blank=True, on_delete=models.SET_NULL, related_name='products_unidad2')
    categoria = models.ForeignKey('Categoria', null=True, blank=True, on_delete=models.SET_NULL, related_name='products_categoria')
    precio = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Marca(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Proveedor(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class UnidadMedida(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    folio = models.CharField(max_length=8, help_text="Formato: xx-xxxxx")
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='pedidos')
    productos = models.CharField(max_length=255)
    estatus = models.BooleanField(default=False, help_text="True = Enviado, False = No enviado")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.folio} - {self.cliente.descripcion}"