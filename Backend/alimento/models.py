from django.db import models
from dieta.models import MomentoDia

# Create your models here.
class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    porcion = models.FloatField()
    unidad = models.CharField(max_length=50)
    calorias = models.FloatField()
    proteinas = models.FloatField()
    carbohidratos = models.FloatField()
    grasas = models.FloatField()
    fibra = models.FloatField(blank=True, null=True)
    azucares = models.FloatField(blank=True, null=True)
    momento_dia = models.ManyToManyField(
        MomentoDia,
        related_name='alimentos',
        blank=True,
        through='AlimentoMomentoDia'
    )
    def __str__(self):
        return self.nombre


class AlimentoMomentoDia(models.Model):
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    momento_dia = models.ForeignKey(MomentoDia, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.alimento.nombre} - {self.momento_dia.descripcion}'