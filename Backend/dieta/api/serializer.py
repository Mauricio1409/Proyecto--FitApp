from rest_framework.serializers import ModelSerializer
from dieta.models import Dieta, DiaDieta, MomentoDia
from alimento.api.serializers import AlimentoSerializer, AlimentoMomentoDiaSerializer


class MomentoDiaSerializer(ModelSerializer):
    
    alimentos = AlimentoSerializer(many=True, read_only=True)
    
    class Meta:
        model = MomentoDia
        fields = ['id', 'dia_dieta', 'momento', 'descripcion', 'alimentos']
        read_only_fields = ['id', 'dia_dieta']


class DiaDietaSerializer(ModelSerializer):
    momentos_dia = MomentoDiaSerializer(many=True, read_only=True)
    
    class Meta:
        model = DiaDieta
        fields = ['id', 'dieta', 'fecha', 'dia', 'descripcion', 'momentos_dia']
        read_only_fields = ['id', 'dieta', 'fecha']


class DietaSerializer(ModelSerializer):
    
    dias_dieta = DiaDietaSerializer(many=True, read_only=True)
    class Meta:
        model = Dieta
        fields = ['id', 'nombre', 'usuario', 'fecha_inicio', 'activa', 'dias_dieta']
        read_only_fields = ['id', 'usuario', 'fecha_inicio']
        

