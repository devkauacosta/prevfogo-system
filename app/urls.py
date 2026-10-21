from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from frota_prevfogo.views import VeiculosListView, VeiculoCreate, VeiculoDetail, VeiculoDelete, VeiculoUpdate
from frota_prevfogo.views import MVDelete, OSDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/', VeiculosListView.as_view(), name='lista_veiculos'),
    path('novo_veiculo', VeiculoCreate.as_view(), name='veiculo_novo'),
    path('veiculo/<str:pk>/', VeiculoDetail.as_view(), name='veiculo_detalhe'),
    path('deletar_veiculo/<str:pk>/', VeiculoDelete.as_view(), name='veiculo_delete'),
    path('atualizar_veiculo/<str:pk>/', VeiculoUpdate.as_view(), name='veiculo_update'),
    path('veiculos/doc-mv/<int:pk>/remover', MVDelete.as_view(), name='mv_delete'),
    path('veiculos/doc-os/<int:pk>/remover', OSDelete.as_view(), name='os_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
