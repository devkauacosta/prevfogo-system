from django.db import models


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome_marca = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_marca


class TipoVeiculo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=300)

    def __str__(self):
        return self.tipo