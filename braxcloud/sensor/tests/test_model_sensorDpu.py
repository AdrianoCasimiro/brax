from django.test import TestCase
from braxcloud.sensor.models import SensorDPU, Sensor

class SensorDpuModelTest(TestCase):
    def setUp(self):
        sensor = Sensor.objects.create(codigo='Dpu01', fase='R', disjuntor='E', descricao='Teste')
        self.obj = SensorDPU.objects.create(sensor=sensor, datahora='2020-12-17 02:03:00', t=40, h=50.1, f60=0, mcnt=0)

    def test_create(self):
        self.assertTrue(SensorDPU.objects.exists())


