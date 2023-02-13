from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from validate_docbr import CNPJ, CPF

from clientes.choices import UF_CHOICES


def validate_cpf_cnpj(value):
    if CNPJ().validate(value) or CPF().validate(value):
        return value
    else:
        ValidationError("CPF ou CNPJ invalidos")


class Cliente(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )
    endereco = models.CharField(
        verbose_name="Endereço",
        max_length=100,
        blank=True,
        null=True,
    )
    bairro = models.CharField(
        verbose_name="Bairro",
        max_length=100,
        blank=True,
        null=True,
    )
    cidade = models.CharField(
        verbose_name="Cidade",
        max_length=100,
        blank=True,
        null=True,
    )
    estado = models.CharField(
        verbose_name="Estado",
        max_length=2,
        choices=UF_CHOICES,
        blank=True,
        null=True,
    )
    cpf_cnpj = models.CharField(
        verbose_name="CPF/CNPJ",
        max_length=14,
        unique=True,
        validators=[MinLengthValidator(11), MaxLengthValidator(14), validate_cpf_cnpj],
    )
    rg = models.CharField(
        verbose_name="RG",
        max_length=7,
        validators=[MinLengthValidator(7)],
        blank=True,
        null=True,
    )
    telefone = models.CharField(
        verbose_name="Telefone de Contato",
        max_length=13,
        validators=[MinLengthValidator(9), MaxLengthValidator(13)],
        blank=True,
        null=True,
    )
