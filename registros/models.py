from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models

from clientes.models import Cliente
from veiculos.models import Veiculo


class AbateDiario(models.Model):
    dia = models.DateField(unique=True)
    cortes_suinos = ArrayField(
        base_field=models.FloatField(validators=[MinValueValidator(0.0)]),
        blank=True,
        null=True,
    )
    cortes_carneiros = ArrayField(
        base_field=models.FloatField(validators=[MinValueValidator(0.0)]),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Abate de {self.dia.strftime('%d/%m/%Y')}"


class Romaneio(models.Model):
    data = models.DateTimeField()
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name="romaneios",
    )


class Pedido(models.Model):
    cortes_suinos = ArrayField(
        base_field=models.FloatField(validators=[MinValueValidator(0.0)]),
        blank=True,
        null=True,
    )
    cortes_carneiros = ArrayField(
        base_field=models.FloatField(validators=[MinValueValidator(0.0)]),
        blank=True,
        null=True,
    )
    abate = models.ForeignKey(
        AbateDiario,
        on_delete=models.CASCADE,
        related_name="pedidos",
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="pedidos",
    )
    romaneio = models.ForeignKey(
        Romaneio,
        on_delete=models.CASCADE,
        related_name="pedidos",
    )
