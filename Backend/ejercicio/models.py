from django.db import models
from rutina.models import DiaRutina

# Create your models here.
class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    grupo_muscular = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_ejercicio = models.CharField(max_length=50, 
                                      choices=[('fuerza', 'Fuerza'),
                                                ('cardio', 'Cardio'),
                                                ('flexibilidad', 'Flexibilidad')])
    url_video = models.URLField(blank=True, null=True)
    dia_rutina = models.ManyToManyField(DiaRutina, related_name='ejercicios', blank=True, through='EjercicioDiaRutina')
    
    def __str__(self):
        return self.nombre
    
class EjercicioDiaRutina(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    dia_rutina = models.ForeignKey(DiaRutina, on_delete=models.CASCADE)
    series = models.IntegerField()
    repeticiones = models.IntegerField()
    peso = models.FloatField()
    orden = models.IntegerField()
    
    def __str__(self):
        return f'{self.ejercicio.nombre} - {self.dia_rutina.descripcion}'
    


