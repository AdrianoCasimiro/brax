from django.test import TestCase
from ..models import AlertaDp
from braxcloud.sensor.models import SensorDPU, Sensor


class AlertaDpModelTest(TestCase):
    def setUp(self):
        sensor = Sensor.objects.create(codigo='DP01', fase='R', disjuntor='E', descricao='Teste')

        self.sensordpu = SensorDPU.objects.create(sensor=sensor, datahora='2020-12-17 02:03:00', t=40, h=50.1, f60=0, mcnt=0)


    def test_create(self):
        alerta = AlertaDp.objects.create(sensor=self.sensordpu, tipo_alerta='SPARK', datahora='2020-12-17 02:03:00',
                                              valor='1',checado='N', primeiro_aviso='False')
        self.assertTrue(AlertaDp.objects.exists())





