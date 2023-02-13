from django.test import TestCase
from validate_docbr import RENAVAM


class RenavamTestCase(TestCase):
    def test_renavam(self):
        renavam = RENAVAM()
        print(renavam.validate("93250527014"))
