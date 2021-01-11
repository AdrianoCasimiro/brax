from rest_framework import status
from rest_framework.test import APITestCase
from braxcloud.cliente.models import Equipamento, Planta, Cliente, Setor
from braxcloud.sensor.models import SensorTemp, Sensor, SensorDPU


class SensorTempSerializerTest(APITestCase):
    def setUp(self):
        cliente = Cliente.objects.create(cnpj='1234566', razao_social='Tigre SA', nome_fantasia ='Tigre',
                                              endereco='dsfsdf', bairro='Centro',cidade='Rio Claro', uf='São Paulo',
                                              cep='135111')
        planta = Planta.objects.create(nome='Tigre', cliente=cliente)
        setor = Setor.objects.create(nome='Tigre Rio Claro', planta=planta)
        equipamento = Equipamento.objects.create(tag='P1', descricao='painel de entrada',
                                                      temperatura_max=70, setor=setor)
        sensor = Sensor.objects.create(codigo='Tp01', fase='R', disjuntor='E', descricao='Teste',
                                            equipamento=equipamento, planta=planta, setor=setor)
        self.obj = SensorTemp.objects.create(sensor=sensor, datahora='2020-12-17 02:03:00', t=600)

    def test_sensortemp_create(self):
        data = {'sensor': 'Tp01', 'datahora': '2020-12-17 02:03:00', 't': '600'}
        response = self.client.post('/sensores/api/temp/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class SensorDpuSerializerTest(APITestCase):
    def setUp(self):
        sensor = Sensor.objects.create(codigo='Dpu01', fase='R', disjuntor='E', descricao='Teste')
        self.obj = SensorDPU.objects.create(sensor=sensor, datahora='2020-12-17 02:03:00', t=40, h=50.1, f60=0, mcnt=0)

    def test_sensordpu_create(self):
        data = {'sensor': 'Dpu01', 'datahora': '2020-12-17 02:03:00', 't': '40', 'h': '50.1', 'f60': '0', 'mcnt': '0'}
        response = self.client.post('/sensores/api/dpu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)