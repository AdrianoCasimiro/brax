from django.test import TestCase
from braxcloud.sensor.models import SensorTemp, Sensor
from braxcloud.cliente.models import Equipamento, Cliente, Setor, Planta
from braxcloud.alerta.models import AlertaTemp


class SensortempModelTest(TestCase):
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
                                   equipamento=equipamento
                                   )
        '''SensorTemp obj that does not generate alarm '''
        self.sensortemp = SensorTemp.objects.create(sensor=sensor, datahora='2020-12-17 02:03:00', t=600)

        '''SensorTemp obj that generates alarm '''
        self.sensortempcreatealert = SensorTemp.objects.create(sensor=sensor, datahora='2020-12-17 02:03:00', t=300)


    def test_create_sensortemp(self):
        self.assertTrue(SensorTemp.objects.exists())

    def test_sensortemp_temp_value(self):
        self.assertEqual(63.1, self.sensortemp.t)


    '''Test AlertaTemp'''
    def test_create_sensortemp_alarm(self):
        self.assertTrue(AlertaTemp.objects.exists())

    def test_sensortemp_temp_value_of_create_alert(self):
        self.assertEqual(87.1, self.sensortempcreatealert.t)




