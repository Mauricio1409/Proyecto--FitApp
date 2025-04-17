from rest_framework.viewsets import ModelViewSet
from alimento.models import Alimento, AlimentoMomentoDia
from alimento.api.serializers import AlimentoSerializer, AlimentoMomentoDiaSerializer
from dieta.models import MomentoDia
from rest_framework.permissions import IsAuthenticated


class AlimentoViewSet(ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

class AlimentoMomentoDiaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AlimentoMomentoDiaSerializer

    def get_queryset(self):
        momento_dia_pk = self.kwargs['momento_dia_pk']

        # Usamos get_object_or_404 para dar error 404 automáticamente si no existe
        momento_dia = get_object_or_404(MomentoDia, id=momento_dia_pk)

        return AlimentoMomentoDia.objects.filter(momento_dia=momento_dia)

    def perform_create(self, serializer):
        momento_dia_pk = self.kwargs['momento_dia_pk']
        momento_dia = get_object_or_404(MomentoDia, id=momento_dia_pk)
        serializer.save(momento_dia=momento_dia)
