from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Veiculo, DocMvVeiculo, DocOSVeiculo
from .forms import VeiculoModelForm
from .filters import VeiculoFilter

class VeiculosListView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'
    context_object_name = 'veiculos'


    def get_queryset(self):
        veiculos = super().get_queryset()
        self.filter = VeiculoFilter(self.request.GET, veiculos)
        return self.filter.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = self.filter
        return context


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

    def form_valid(self, form):
            response = super().form_valid(form) 
    
            for arquivo in form.cleaned_data['campo_mvs']:
                DocMvVeiculo.objects.create(veiculo=self.object, documento_mv=arquivo)
    
            for arquivo in form.cleaned_data['campo_os']:
                DocOSVeiculo.objects.create(veiculo=self.object, documento_os=arquivo)
    
            return response

    def get_success_url(self):
        return reverse_lazy('veiculo_detalhe', kwargs={'pk': self.object.pk})

class MVDelete(DeleteView):
    model = DocMvVeiculo
    template_name = 'delete_mv.html'

    def get_success_url(self):
        return reverse('veiculo_update', kwargs={'pk': self.object.veiculo.pk})


class OSDelete(DeleteView):
    model = DocOSVeiculo
    template_name = 'delete_os.html'

    def get_success_url(self):
        return reverse('veiculo_update', kwargs={'pk': self.object.veiculo.pk})