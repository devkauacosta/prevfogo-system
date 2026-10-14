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


class Veiculo(models.Model):
    renavam = models.CharField(primary_key=True, unique=True, max_length=11)
    chassi = models.CharField(max_length=17, blank=True, null=True)
    placa = models.CharField(blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='marca_veiculo', blank=True, null=True)
    modelo = models.CharField(max_length=300)
    ano = models.IntegerField(blank=True, null=True)
    tipo = models.ForeignKey(TipoVeiculo, on_delete=models.PROTECT, related_name='tipo_veiculo', blank=True, null=True)
    patrimonio = models.CharField(max_length=300, blank=True, null=True)
    quilometragem_atual = models.PositiveIntegerField(blank=True, null=True)
    data_revisao = models.DateField(blank=True, null=True)
    km_ultima_rev = models.PositiveIntegerField(blank=True, null=True)
    prox_revisao = models.DateField(blank=True, null=True)
    documentacao_mv = models.FileField(upload_to='docs_mvs/', blank=True, null=True)
    documentacao_os = models.FileField(upload_to='docs_oss/', blank=True, null=True)


    def __str__(self):
        return f"{self.marca} {self.modelo} - Renavam: {self.renavam}"