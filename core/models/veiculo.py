from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='Veiculos')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='Veiculos')
    acessorio = models.ManyToManyField(Acessorio, related_name='Veiculos')

    def __str__(self):
        return f'{self.modelo}, {self.cor} - {self.ano} ({self.id})'

    class Meta:
        verbose_name = 'veículo'
        verbose_name_plural = 'veículos'
