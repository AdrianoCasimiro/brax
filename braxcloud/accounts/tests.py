from django.test import TestCase
from ..cliente.models import Cliente
from django.contrib.auth.models import User
from .models import AcessoUsuario

class AcessoUsuarioModelTest(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(cnpj='1234566', razao_social='Tigre SA', nome_fantasia='Tigre',
                                         endereco='dsfsdf', bairro='Centro', cidade='Rio Claro', uf='São Paulo',
                                         cep='135111')
        user = User.objects.create(username='Adriano', password='teste123')
        self.obj = AcessoUsuario.objects.create(usuario=user, cliente=cliente)

    def test_create_acesso_usuario(self):
        self.assertTrue(AcessoUsuario.objects.exists())

    def test_str(self):
        self.assertEqual('Adriano', str(self.obj))

    def test_empresa(self):
        self.assertEqual('Tigre', str(self.obj.cliente.nome_fantasia))


