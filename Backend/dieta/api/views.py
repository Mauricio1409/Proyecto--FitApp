from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from dieta.models import DiaDieta, Dieta, MomentoDia
from dieta.api.serializer import DiaDietaSerializer, DietaSerializer, MomentoDiaSerializer

class DietaViewSet(ModelViewSet):
    """
    API endpoint that allows users to view or edit dieta instances.
    """
    queryset = Dieta.objects.all()
    serializer_class = DietaSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class DiaDietaViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    
    serializer_class = DiaDietaSerializer
    
    def get_queryset(self):
        
        dieta_id = self.kwargs['dieta_pk']
        return DiaDieta.objects.filter(dieta__id=dieta_id)
    
    def perform_create(self, serializer):
        dieta_id = self.kwargs['dieta_pk']
        dieta = Dieta.objects.get(id=dieta_id)
        serializer.save(dieta=dieta)
        
class MomentoDiaViewSet(ModelViewSet):
        
        permission_classes = [IsAuthenticated]
        
        serializer_class = MomentoDiaSerializer
        
        def get_queryset(self):
            
            dia_dieta_id = self.kwargs['dia_dieta_pk']
            return MomentoDia.objects.filter(dia_dieta__id=dia_dieta_id)
        
        def perform_create(self, serializer):
            
            dia_dieta_id = self.kwargs['dia_dieta_pk']
            dia_dieta = DiaDieta.objects.get(id=dia_dieta_id)
            serializer.save(dia_dieta=dia_dieta)
        
        