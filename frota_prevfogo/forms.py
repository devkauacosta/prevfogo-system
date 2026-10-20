from django import forms
from .models import Veiculo

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return [single_file_clean(data, initial)]


class VeiculoModelForm(forms.ModelForm):
    campo_mvs = MultipleFileField(
        label="Anexar MVs (PDF, JPG, PNG, etc.)",
        required=False
    )

    campo_os = MultipleFileField(
        label="Anexar OSs (PDF, JPG, PNG, etc.)",
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance._state.adding:
            self.fields['renavam'].disabled = True


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