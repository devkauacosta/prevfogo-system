from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Veiculo, DocMvVeiculo, DocOSVeiculo
from .forms import VeiculoModelForm

class VeiculosListView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'
    context_object_name = 'veiculos'


class VeiculoCreate(CreateView):
    model = Veiculo
    form_class = VeiculoModelForm
    template_name = 'novo_veiculo.html'
    success_url = reverse_lazy('lista_veiculos')

    def form_valid(self, form):
        veiculo_instance = form.save()

        lista_mvs = self.request.FILES.getlist('campo_mvs')
        for mv in lista_mvs:
            DocMvVeiculo.objects.create(veiculo=veiculo_instance, documento_mv=mv)

        lista_os = self.request.FILES.getlist('campo_os')
        for os in lista_os:
            DocOSVeiculo.objects.create(veiculo=veiculo_instance, documento_os=os)

        return super().form_valid(form)