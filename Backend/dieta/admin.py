from django.contrib import admin
from dieta.models import Dieta, DiaDieta, MomentoDia
from alimento.models import AlimentoMomentoDia


class DiaDietaInline(admin.TabularInline):
    model = DiaDieta
    extra = 1
    
    
class MomentoDiaInline(admin.TabularInline):
    model = MomentoDia
    extra = 1
    
class AlimentoMomentoDiaInline(admin.TabularInline):
    model = AlimentoMomentoDia
    extra = 1
    
# Register your models here. 
@admin.register(Dieta)
class DietaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_inicio', 'activa')
    search_fields = ('nombre', 'usuario__username')
    list_filter = ('activa',)
    ordering = ('-fecha_inicio',)
    inlines = [DiaDietaInline]
    
@admin.register(DiaDieta)
class DiaDietaAdmin(admin.ModelAdmin):
    list_display = ('dieta', 'fecha', 'dia', 'descripcion')
    search_fields = ('dieta__nombre', 'dia')
    list_filter = ('dieta',)
    ordering = ('fecha',)
    inlines = [MomentoDiaInline]    
    

@admin.register(MomentoDia)
class MomentoDiaAdmin(admin.ModelAdmin):
    list_display = ('dia_dieta', 'momento', 'descripcion')
    search_fields = ('dia_dieta__dieta__nombre', 'momento')
    list_filter = ('dia_dieta',)
    ordering = ('dia_dieta',)
    inlines = [AlimentoMomentoDiaInline]
    
    
    
