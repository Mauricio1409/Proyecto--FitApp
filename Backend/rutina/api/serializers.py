from rest_framework.serializers import ModelSerializer
from rutina.models import Rutina, DiaRutina
from ejercicio.models import Ejercicio
from ejercicio.api.serializers import EjercicioSerializer

class DiaRutinaSerializer(ModelSerializer):
    ejercicios = EjercicioSerializer(many=True, read_only=True)

    class Meta:
        model = DiaRutina
        fields = ['id', 'rutina', 'descripcion', 'nro_dia', 'ejercicios']

class RutinaSerializer(ModelSerializer):
    dias = DiaRutinaSerializer(many=True, read_only=True)

    class Meta:
        model = Rutina
        fields = ['id', 'nombre', 'user', 'fecha_creacion', 'cantidad_dias', 'activa', 'dias']
        read_only_fields = ['id', 'fecha_creacion']
