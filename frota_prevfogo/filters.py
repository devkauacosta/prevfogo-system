import django_filters
from .models import Veiculo


class VeiculoFilter(django_filters.FilterSet):
    class Meta:
        model = Veiculo
        fields = {
            "marca": ["exact"],
            "tipo": ["exact"],
        } 