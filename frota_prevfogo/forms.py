from django import forms
from .models import Veiculo

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)


class VeiculoModelForm(forms.ModelForm):
    campo_mvs = MultipleFileField(
        label="Anexar MVs (PDF, JPG, PNG, etc.)",
        required=False
    )

    campo_os = MultipleFileField(
        label="Anexar OSs (PDF, JPG, PNG, etc.)",
        required=False
    )

    class Meta:
        model = Veiculo
        fields = [
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
            'km_ultima_rev',
            'prox_revisao',
        ]