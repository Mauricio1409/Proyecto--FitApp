from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from rutina.api.views import RutinaViewSet, DiaRutinaViewSet

router = DefaultRouter()
router.register('rutinas', RutinaViewSet, basename='rutina')

# Nested router para los días dentro de una rutina
rutinas_router = NestedDefaultRouter(router, 'rutinas', lookup='rutina')
rutinas_router.register('dias', DiaRutinaViewSet, basename='dia-rutina')