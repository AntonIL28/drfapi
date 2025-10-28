from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register(r'api/products', ProductViewSet, 'products')
router.register(r'api/marca', MarcaViewSet, 'marca')
router.register(r'api/proveedor', ProveedorViewSet, 'proveedor')

urlpatterns = router.urls
