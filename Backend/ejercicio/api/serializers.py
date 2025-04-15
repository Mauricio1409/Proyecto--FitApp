import django.db
from rest_framework.serializers import ModelSerializer, StringRelatedField
from ejercicio.models import Ejercicio, EjercicioDiaRutina

class EjercicioSerializer(ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ['id', 'nombre', 'grupo_muscular', 'descripcion', 'tipo_ejercicio', 'url_video']
        read_only_fields = ['id']


class EjercicioDiaRutinaSerializer(ModelSerializer):
    
    class Meta:
        model = EjercicioDiaRutina
        fields = ['id', 'ejercicio', 'dia_rutina', 'repeticiones', 'series', 'peso', 'orden']