from rest_framework.viewsets import ModelViewSet
from ejercicio.models import Ejercicio, EjercicioDiaRutina
from ejercicio.api.serializers import EjercicioSerializer, EjercicioDiaRutinaSerializer
from rutina.models import DiaRutina, Rutina
from rest_framework.exceptions import NotFound

class EjercicioViewSet(ModelViewSet):
    """
    API endpoint that allows Ejercicios to be viewed or edited.
    """
    serializer_class = EjercicioSerializer
    
    def get_queryset(self):
        nombre = self.request.query_params.get('nombre')
        orden = self.request.query_params.get('orden')
        tipo = self.request.query_params.get('tipo')

        queryset = Ejercicio.objects.all()

        # Filtrar por nombre que comienza con...
        if nombre:
            queryset = queryset.filter(nombre__istartswith=nombre)

        # Filtrar por tipo de ejercicio (contenido parcial, sin importar mayúsculas)
        if tipo:
            queryset = queryset.filter(tipo_ejercicio__icontains=tipo)

        # Ordenar por campo válido
        if orden in ['nombre', '-nombre', 'tipo_ejercicio', '-tipo_ejercicio']:
            queryset = queryset.order_by(orden)

        return queryset

    

    
    
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