from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from validate_docbr import RENAVAM


def validate_renavam(value):
    if RENAVAM().validate(value):
        return value
    else:
        ValidationError("RENAVAM invalido.")


class Veiculo(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
    )
    placa = models.CharField(
        verbose_name="Placa",
        max_length=7,
        validators=[
            MinLengthValidator(7),
            RegexValidator(
                regex="[A-Z]{3}[0-9][0-9A-Z][0-9]{2}", message="Placa inválida."
            ),
        ],
    )
    renavam = models.CharField(
        verbose_name="Revanam",
        max_length=11,
        unique=True,
        validators=[MinLengthValidator(11), validate_renavam],
    )
