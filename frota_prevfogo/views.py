from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Veiculo, DocMvVeiculo, DocOSVeiculo
from .forms import VeiculoModelForm

class VeiculosListView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'
    context_object_name = 'veiculos'


class VeiculoDetail(DetailView):
    model = Veiculo
    template_name = 'detalhe_veiculo.html'


class VeiculoCreate(CreateView):
    model = Veiculo
    form_class = VeiculoModelForm
    template_name = 'form_veiculo.html'
    success_url = reverse_lazy('lista_veiculos')

    def form_valid(self, form):
        response = super().form_valid(form) 

        for arquivo in form.cleaned_data['campo_mvs']:
            DocMvVeiculo.objects.create(veiculo=self.object, documento_mv=arquivo)

        for arquivo in form.cleaned_data['campo_os']:
            DocOSVeiculo.objects.create(veiculo=self.object, documento_os=arquivo)

        return response


class VeiculoDelete(DeleteView):
    model = Veiculo
    template_name = 'delete_veiculo.html'
    context_object_name = 'veiculo'
    success_url = '/veiculos/'


class VeiculoUpdate(UpdateView):
    model = Veiculo
    form_class = VeiculoModelForm
    template_name = 'form_veiculo.html'

    def get_success_url(self):
        return reverse_lazy('veiculo_detalhe', kwargs={'pk': self.object.pk})

class MVDelete(DeleteView):
    model = DocMvVeiculo
    template_name = 'delete_mv.html'
    success_url = 'atualizar_veiculo/<int:pk>/'

    def get_success_url(self):
        return reverse_lazy('veiculo_detalhe', kwargs={'pk': self.object.pk})