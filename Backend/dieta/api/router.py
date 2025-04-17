from rest_framework_nested.routers import NestedDefaultRouter
from dieta.api.views import DietaViewSet, DiaDietaViewSet, MomentoDiaViewSet
from rest_framework.routers import DefaultRouter

router_dieta = DefaultRouter()
router_dieta.register(prefix='dietas', viewset=DietaViewSet, basename='dieta')

router_dia_dieta = NestedDefaultRouter(router_dieta, 'dietas', lookup='dieta')
router_dia_dieta.register('dias', DiaDietaViewSet, basename='dieta-dias')

router_momento_dia = NestedDefaultRouter(router_dia_dieta, 'dias', lookup='dia_dieta')
router_momento_dia.register('momentos', MomentoDiaViewSet, basename='dia-momentos')
