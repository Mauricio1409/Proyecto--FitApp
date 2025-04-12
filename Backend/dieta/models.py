from django.db import models
from user.models import User

# Create your models here.

class Dieta(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dietas')
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    

class DiaDieta(models.Model):
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE, related_name='dias_dieta')
    fecha = models.DateTimeField(auto_now_add=True)
    dia = models.CharField(choices=[('lunes', 'Lunes'), ('martes', 'Martes'),  
                                    ('miercoles', 'Miércoles'), ('jueves', 'Jueves'), 
                                    ('viernes', 'Viernes'), ('sabado', 'Sábado'),
                                    ('domingo', 'Domingo')], max_length=10)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.dieta.nombre} - {self.dia}"
    

class MomentoDia(models.Model):
    dia_dieta = models.ForeignKey(DiaDieta, on_delete=models.CASCADE, related_name='momentos_dia')
    momento = models.CharField(choices=[('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), 
                                        ('cena', 'Cena'), ('snack', 'Snack')], max_length=10)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.dia_dieta.dia} - {self.momento}"
    
    
    
