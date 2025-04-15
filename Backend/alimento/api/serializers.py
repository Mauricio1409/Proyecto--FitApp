from rest_framework.serializers import ModelSerializer
from alimento.models import Alimento, AlimentoMomentoDia
from Backend.alimento.models import AlimentoMomentoDia

class AlimentoSerializer(ModelSerializer):
    class Meta:
        model = Alimento
        fields = ['id', 'nombre', 'porcion', 'unidad', 'calorias', 'proteinas', 'carbohidratos', 'grasas', 'fibra', 'azucares']
        
class AlimentoMomentoDiaSerializer(ModelSerializer):
    class Meta:
        model = AlimentoMomentoDia
        fields = ['id', 'alimento', 'momento_dia', 'cantidad', 'observaciones']
        read_only_fields = ['id']