from django.contrib import admin
from .models import Marca, TipoVeiculo, Veiculo

@admin.register(Marca)
class MarcaModelAdmin(admin.ModelAdmin):
    list_display = ('nome_marca',)


@admin.register(TipoVeiculo)
class TipoVeiculoModelAdmin(admin.ModelAdmin):
    list_display = ('tipo', )


@admin.register(Veiculo)
class VeiculoModelAdmin(admin.ModelAdmin):
    list_display = (
        'renavam',
        'chassi',
        'placa',
        'marca',
        'modelo',
        'ano',
        'tipo',
        'patrimonio',
        'quilometragem_atual',
        'data_revisao',
        'km_ultima_rev'
        'prox_revisao',
    )