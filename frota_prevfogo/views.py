from django.shortcuts import render
from django.views.generic import ListView
from .models import Veiculo

class VeiculosListView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'
    context_object_name = 'veiculos'