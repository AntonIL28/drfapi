from django.db import models

# Create your models here.
class Product(models.Model):
    codigoprov = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    upc1 = models.CharField(max_length=100)
    upc2 = models.CharField(max_length=100)
    mult1 = models.IntegerField(default=0)
    mult2 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
    
class Marca(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Proveedor(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description