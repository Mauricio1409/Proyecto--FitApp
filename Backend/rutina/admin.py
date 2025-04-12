from django.contrib import admin
from rutina.models import Rutina, DiaRutina
from ejercicio.models import Ejercicio, EjercicioDiaRutina

# Clase inline para mostrar los días dentro de la rutina
class DiaRutinaInline(admin.TabularInline):  # Podés usar StackedInline si preferís
    model = DiaRutina
    extra = 1  # Cuántos formularios vacíos aparecen por defecto


class EjercicioDiaRutinaInline(admin.TabularInline):
    model = EjercicioDiaRutina
    extra = 1  # Cuántos formularios vacíos aparecen por defecto

# Admin para la rutina
@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'user', 'fecha_creacion', 'cantidad_dias', 'activa']
    list_filter = ['activa', 'fecha_creacion']
    search_fields = ['nombre', 'user__username']
    inlines = [DiaRutinaInline]  # Mostrar días dentro de rutina

# Admin para los días (opcional, si querés verlos aparte)
@admin.register(DiaRutina)
class DiaRutinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'rutina', 'nro_dia', 'descripcion']
    list_filter = ['rutina']
    search_fields = ['descripcion']
    inlines = [EjercicioDiaRutinaInline]





