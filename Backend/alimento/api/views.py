from rest_framework.viewsets import ModelViewSet
from alimento.models import Alimento, AlimentoMomentoDia
from alimento.api.serializers import AlimentoSerializer, AlimentoMomentoDiaSerializer
from Backend.alimento.models import AlimentoMomentoDia
from rest_framework.exceptions import NotFound
from dieta.models import Dieta, DiaDieta
from django.core.exceptions import ObjectDoesNotExist


class AlimentoViewSet(ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    
class AlimentoMomentoDiaViewSet(ModelViewSet):
    """
    API endpoint that allows AlimentoMomentoDia to be viewed or edited.
    """
    
    serializer_class = AlimentoMomentoDiaSerializer
    
    def get_queryset(self):
        dieta_pk = self.kwargs['dieta_pk']
        dia_dieta_pk = self.kwargs['dia_dieta_pk']
        momento_dia_pk = self.kwargs['momento_dia_pk']
        
        # Validar que la dieta, el día de la dieta y el momento del día existen
        try:
            dieta = Dieta.objects.get(id=dieta_pk)
            dia_dieta = DiaDieta.objects.get(id=dia_dieta_pk, dieta=dieta)
            momento_dia = AlimentoMomentoDia.objects.get(id=momento_dia_pk, dia_dieta=dia_dieta)
        except ObjectDoesNotExist:
            raise NotFound('La dieta, el día de la dieta o el momento del día no existen o no están relacionados correctamente.')
        
        # Filtrar los alimentos asociados al momento del día
        return AlimentoMomentoDia.objects.filter(momento_dia=momento_dia)