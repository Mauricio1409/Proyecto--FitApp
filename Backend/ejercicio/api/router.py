from rest_framework.routers import DefaultRouter
from ejercicio.api.views import EjercicioViewSet, EjercicioDiaRutinaViewSet
from rest_framework_nested.routers import NestedSimpleRouter
from rutina.api.router import rutinas_router as dias_router

router = DefaultRouter()
router.register(prefix='ejercicio', basename='ejercicio', viewset=EjercicioViewSet)

# Router anidado para ejercicios por día
diaEjercicio_router = NestedSimpleRouter(dias_router, r'dias', lookup='dia')
diaEjercicio_router.register(r'ejercicios', EjercicioDiaRutinaViewSet, basename='dia-ejercicio')
