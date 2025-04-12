from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # Datos personales
    edad = models.PositiveIntegerField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True, help_text="Peso en kg")
    altura = models.FloatField(null=True, blank=True, help_text="Altura en cm")

    # Nivel de entrenamiento
    nivel_entrenamiento = models.CharField(
        max_length=20,
        choices=[
            ('principiante', 'Principiante'),
            ('intermedio', 'Intermedio'),
            ('avanzado', 'Avanzado')
        ],
        default='principiante'
    )

    # Objetivo fitness
    objetivo = models.CharField(
        max_length=30,
        choices=[
            ('ganar_masa', 'Ganar masa muscular'),
            ('perder_grasa', 'Perder grasa'),
            ('mantener', 'Mantener forma física')
        ],
        null=True, blank=True
    )
    
    foto_perfil = models.ImageField(upload_to='perfil/', null=True, blank=True)

    def __str__(self):
        return self.username
