from django.contrib import admin
from alimento.models import Alimento, AlimentoMomentoDia

# Register your models here.
@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'porcion', 'unidad', 'calorias', 'proteinas', 'carbohidratos', 'grasas', 'fibra', 'azucares')
    search_fields = ('nombre',)
    list_filter = ('unidad',)
    ordering = ('nombre',)


@admin.register(AlimentoMomentoDia)
class AlimentoMomentoDiaAdmin(admin.ModelAdmin):
    list_display = ('alimento', 'momento_dia', 'cantidad', 'observaciones')
    search_fields = ('alimento__nombre', 'momento_dia__descripcion')
    list_filter = ('momento_dia',)
    ordering = ('alimento', 'momento_dia')
