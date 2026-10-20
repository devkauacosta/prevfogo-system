from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from frota_prevfogo.views import VeiculosListView, VeiculoCreate, VeiculoDetail, VeiculoDelete, VeiculoUpdate
from frota_prevfogo.views import MVDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/', VeiculosListView.as_view(), name='lista_veiculos'),
    path('novo_veiculo', VeiculoCreate.as_view(), name='veiculo_novo'),
    path('veiculo/<int:pk>/', VeiculoDetail.as_view(), name='veiculo_detalhe'),
    path('deletar_veiculo/<int:pk>/', VeiculoDelete.as_view(), name='veiculo_delete'),
    path('atualizar_veiculo/<int:pk>/', VeiculoUpdate.as_view(), name='veiculo_update'),
    path('veiculos/doc-mv/<int:pk>/remover', MVDelete.as_view(), name='mv_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
