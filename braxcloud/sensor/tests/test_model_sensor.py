from django.test import TestCase
from braxcloud.sensor.models import Sensor

class SensorModelTest(TestCase):
    def setUp(self):
        self.sensor = Sensor.objects.create(
            codigo='Tp01',
            fase='R',
            disjuntor='E',
            descricao='Teste'
        )

    def test_create(self):
        self.assertTrue(Sensor.objects.exists())


