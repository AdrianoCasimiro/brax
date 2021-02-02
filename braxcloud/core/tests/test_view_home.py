from django.test import TestCase
from django.shortcuts import resolve_url as r
from braxcloud.cliente.models import Cliente
from django.contrib.auth.models import User
from braxcloud.accounts.models import AcessoUsuario

class HomeTest(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(cnpj='1234566', razao_social='Tigre SA', nome_fantasia='Tigre',
                                         endereco='dsfsdf', bairro='Centro', cidade='Rio Claro', uf='São Paulo',
                                         cep='135111')
        user = User.objects.create(username='Adriano', password='teste123')
        self.obj = AcessoUsuario.objects.create(usuario=user, cliente=cliente)
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET/ must return status code 302"""
        self.assertEqual(302, self.response.status_code)
