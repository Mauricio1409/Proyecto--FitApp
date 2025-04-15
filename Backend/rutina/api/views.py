from rest_framework.viewsets import ModelViewSet
from rutina.api.serializers import RutinaSerializer, DiaRutinaSerializer
from rutina.models import Rutina, DiaRutina
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class RutinaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    """
    API endpoint that allows users to view or edit routines.
    """
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer
    
    def perform_create(self, serializer):
        # Asociar la rutina con el usuario logueado
        serializer.save(user=self.request.user)
    
    # @action(detail=True, methods=['get'], url_path='dias', url_name='dias')
    # def get_dias(self, request, *args, **kwargs):
    #     """
    #     Método para obtener los días de una rutina específica.
    #     """
    #     # Obtener la rutina a partir del pk
    #     rutina = self.get_object()
        
    #     # Obtener los días asociados a la rutina
    #     dias = rutina.dias.all()
        
    #     # Serializar los días
    #     serializer = DiaRutinaSerializer(dias, many=True)
        
    #     return Response(serializer.data)

class DiaRutinaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    serializer_class = DiaRutinaSerializer
    
    def get_queryset(self):
        # Obtén el pk de la rutina desde la URL
        rutina_id = self.kwargs['rutina_pk']
        return DiaRutina.objects.filter(rutina__id=rutina_id)
    
    def perform_create(self, serializer):
        # Obtén el objeto Rutina
        rutina_id = self.kwargs['rutina_pk']
        rutina = Rutina.objects.get(id=rutina_id)  # Obtenemos la instancia de Rutina
        
        # Guardamos el objeto DiaRutina con la relación de Rutina
        serializer.save(rutina=rutina)  # Guardar con la instancia de Rutina, no con solo el id
