from .models import *
from rest_framework import serializers, viewsets, permissions
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows marcas to be viewed or edited.
    """
    queryset = Marca.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MarcaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):  
    """
    API endpoint that allows proveedores to be viewed or edited.
    """
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clientes to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer