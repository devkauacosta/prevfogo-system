import django_filters
from .models import Veiculo


class VeiculoFilter(django_filters.FilterSet):
    class Meta:
        model = Veiculo
        fields = {
            "renavam": ["icontains"],
            "marca": ["exact"],
            "tipo": ["exact"],
        } 