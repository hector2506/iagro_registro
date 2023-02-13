from django.test import TestCase
from validate_docbr import CNPJ, CPF


class AnimalTestCase(TestCase):
    def test_cpf_cnpj(self):
        cpf = CPF()
        cnpj = CNPJ()
        print(cpf.validate("49324090364"))
        print(cnpj.validate("24367934000124"))
