from django_filters import rest_framework as filters
from alimento.models import Alimento

class AlimentoFilter(filters.FilterSet):
    nombre = filters.CharFilter(field_name='nombre', lookup_expr='istartswith')

    class Meta:
        model = Alimento
        fields = ['nombre']
