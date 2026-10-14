from django.contrib import admin
from django.urls import path
from frota_prevfogo.views import VeiculosListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/', VeiculosListView.as_view(), name='lista_veiculos'),
]
