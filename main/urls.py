from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register(r'api/products', ProductViewSet, 'products')
router.register(r'api/marca', MarcaViewSet, 'marca')
router.register(r'api/proveedor', ProveedorViewSet, 'proveedor')
router.register(r'api/clientes', ClienteViewSet, 'clientes')
router.register(r'api/unidad_medida', UnidadMedidaViewSet, 'unidad_medida')
router.register(r'api/pedidos', PedidoViewSet, 'pedidos')
router.register(r'api/categoria', CategoriaViewSet, 'categoria')

urlpatterns = router.urls
