from rest_framework.viewsets import ModelViewSet
from ejercicio.models import Ejercicio, EjercicioDiaRutina
from ejercicio.api.serializers import EjercicioSerializer, EjercicioDiaRutinaSerializer
from rutina.models import DiaRutina, Rutina
from rest_framework.exceptions import NotFound

class EjercicioViewSet(ModelViewSet):
    """
    API endpoint that allows Ejercicios to be viewed or edited.
    """
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
    
    
class EjercicioDiaRutinaViewSet(ModelViewSet):
    """
    API endpoint that allows EjercicioDiaRutina to be viewed or edited.
    """
    
    serializer_class = EjercicioDiaRutinaSerializer
    
    def get_queryset(self):
            rutina_pk = self.kwargs['rutina_pk']
            dia_pk = self.kwargs['dia_pk']
            
            # Validar que el día pertenece a la rutina
            try:
                rutina = Rutina.objects.get(id=rutina_pk)
                dia = DiaRutina.objects.get(id=dia_pk, rutina=rutina)
            except DiaRutina.DoesNotExist:
                raise NotFound('El día no pertenece a la rutina especificada.')
            
            return EjercicioDiaRutina.objects.filter(dia_rutina=dia)
        
        
    # def perform_create(self, serializer):
    #     dia_pk = self.kwargs['dia_pk']
    #     rutina_pk = self.kwargs['rutina_pk']
        
    #     # Validar que el día pertenece a la rutina
    #     try:
    #         rutina = Rutina.objects.get(id=rutina_pk)
    #         dia = DiaRutina.objects.get(id=dia_pk, rutina=rutina)
    #     except DiaRutina.DoesNotExist:
    #         raise NotFound('El día no pertenece a la rutina especificada.')
        
    #     serializer.save(dia_rutina=dia)