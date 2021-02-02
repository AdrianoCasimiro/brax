from django.test import TestCase, RequestFactory
from ..models import Gateway
from django.shortcuts import resolve_url as r
from braxcloud.cliente.models import Cliente, Planta
from ..views import GatewayList
from django.contrib.auth.models import User
from ...accounts.models import AcessoUsuario


class GatewayListTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='Adriano', password='teste123')
        cliente = Cliente.objects.create(cnpj='1234566', razao_social='Tigre SA', nome_fantasia='Tigre',
                                             endereco='dsfsdf', bairro='Centro', cidade='Rio Claro', uf='São Paulo',
                                             cep='135111')

        planta = Planta.objects.create(nome='Tigre', cliente=cliente)
        obj = AcessoUsuario.objects.create(usuario=user, cliente=cliente)

        gateway = Gateway.objects.create(codigo='Gat01', cliente=cliente, planta=planta, hostname='Tigre')

        self.factory = RequestFactory()
        request = self.factory.get((r('gateway:gateway_list')))
        request.user = user
        self.response = GatewayList.as_view()(request)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
