from django.test import TestCase
from .models import Gateway
from braxcloud.cliente.models import Cliente, Planta


class GatewayModelTest(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(cnpj='1234566',
                                         razao_social='Tigre SA',
                                         nome_fantasia='Tigre',
                                         endereco='dsfsdf',
                                         bairro='Centro',
                                         cidade='Rio Claro',
                                         uf='São Paulo',
                                         cep='135111'
                                         )
        planta = Planta.objects.create(nome='Tigre',
                                       cliente=cliente
                                       )
        self.gateway = Gateway.objects.create(codigo='gat01', cliente=cliente, planta=planta, hostname='Gat01 Tigre Rio Claro ')

    def test_create(self):
        self.assertTrue(Gateway.objects.exists())

    def test_str(self):
        self.assertEqual('gat01', str(self.gateway))
