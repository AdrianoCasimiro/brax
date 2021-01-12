from django.test import TestCase
from braxcloud.sensor.models import SensorTemp, Sensor
from braxcloud.cliente.models import Equipamento, Planta, Cliente, Setor
from braxcloud.alerta.models import AlertaTemp


class SensortempModelTest(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(cnpj='1234566',
                                         razao_social='Tigre SA',
                                         nome_fantasia ='Tigre',
                                         endereco='dsfsdf',
                                         bairro='Centro',
                                         cidade='Rio Claro',
                                         uf='São Paulo',
                                         cep='135111'
                                         )

        planta = Planta.objects.create(nome='Tigre',
                                       cliente=cliente
                                       )

        setor = Setor.objects.create(nome='Tigre Rio Claro',
                                     planta=planta
                                     )

        equipamento = Equipamento.objects.create(tag='P1',
                                                 descricao='painel de entrada',
                                                 temperatura_max=70,
                                                 setor=setor
                                                 )

        sensor = Sensor.objects.create(codigo='Tp01',
                                       fase='R',
                                       disjuntor='E',
                                       descricao='Teste',
                                       equipamento=equipamento,
                                       planta=planta,
                                       setor=setor
                                       )

        self.obj = SensorTemp.objects.create(sensor=sensor,
                                             datahora='2020-12-17 02:03:00',
                                             t=600
                                             )

        self.obj_create_alert = SensorTemp.objects.create(sensor=sensor,
                                                          datahora='2020-12-17 02:03:00',
                                                          t=300
                                                          )

    def test_create_sensortemp(self):
        self.assertTrue(SensorTemp.objects.exists())

    def test_sensortemp_temp(self):
        self.assertEqual(63.1, self.obj.t)

    def test_sensortemp_temp_alert(self):
        self.assertEqual(87.1, self.obj_create_alert.t)

    def test_temp_alert_create(self):
        self.assertTrue(AlertaTemp.objects.exists())

    def test_temp_alert_count(self):
        self.assertEqual(1, AlertaTemp.objects.all().count())
