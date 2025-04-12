from django.db import models
from user.models import User
# Create your models here.

class Rutina(models.Model):
    nombre = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rutinas')
    fecha_creacion = models.DateField(auto_now_add=True)
    cantidad_dias = models.IntegerField()
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    
class DiaRutina(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name='dias')
    nro_dia = models.IntegerField()
    descripcion = models.TextField()
    
    def __str__(self):
        return f'Día {self.nro_dia} de {self.rutina.nombre}'
    
    
