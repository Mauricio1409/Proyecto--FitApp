from django.contrib import admin
from ejercicio.models import Ejercicio, EjercicioDiaRutina

# Register your models here.
@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'grupo_muscular', 'tipo_ejercicio']
    search_fields = ['nombre', 'grupo_muscular']
    list_filter = ['tipo_ejercicio']
    

@admin.register(EjercicioDiaRutina)
class EjercicioDiaRutinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ejercicio', 'dia_rutina', 'series', 'repeticiones', 'peso', 'orden']
    search_fields = ['ejercicio__nombre', 'dia_rutina__descripcion']
    list_filter = ['ejercicio__tipo_ejercicio']
    ordering = ['orden']
