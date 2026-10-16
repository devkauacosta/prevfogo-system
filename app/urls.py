from django.contrib import admin
from django.urls import path
from frota_prevfogo.views import VeiculosListView, VeiculoCreate, VeiculoDetail, VeiculoDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/', VeiculosListView.as_view(), name='lista_veiculos'),
    path('novo_veiculo', VeiculoCreate.as_view(), name='veiculo_novo'),
    path('veiculo/<int:pk>/', VeiculoDetail.as_view(), name='veiculo_detalhe'),
    path('deletar_veiculo/<int:pk>/', VeiculoDelete.as_view(), name='veiculo_delete'),
]
