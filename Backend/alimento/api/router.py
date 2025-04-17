from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from alimento.api.views import AlimentoViewSet, AlimentoMomentoDiaViewSet
from dieta.api.router import router_momento_dia as momento_router


router_alimento = DefaultRouter()
router_alimento.register(prefix='alimentos', viewset=AlimentoViewSet, basename='alimentos')


router_momento_dia_alimento = NestedDefaultRouter(momento_router, 'momentos', lookup='momento_dia')
router_momento_dia_alimento.register('alimentos', AlimentoMomentoDiaViewSet, basename='alimento-momentodia')