from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from ..models import Planta, Cliente
from braxcloud.accounts.models import AcessoUsuario
from django.shortcuts import resolve_url as r
from ..views import PlantaList

class PlantaListGet(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Adriano', password='teste123')

        self.cliente = Cliente.objects.create(cnpj='1234566', razao_social='Tigre SA', nome_fantasia='Tigre',
                                              endereco='dsfsdf', bairro='Centro', cidade='Rio Claro', uf='São Paulo',
                                              cep='135111')

        self.obj = AcessoUsuario.objects.create(usuario=self.user, cliente=self.cliente)

        self.planta = Planta.objects.create(nome='Tigre',
                                       cliente=self.cliente)

        self.factory = RequestFactory()
        request = self.factory.get((r('cliente:planta_list')))
        request.user = self.user
        self.response = PlantaList.as_view()(request)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)