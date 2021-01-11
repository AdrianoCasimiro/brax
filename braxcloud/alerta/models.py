from django.db import models
from ..sensor.models import SensorTemp


class AlertaTemp(models.Model):
    CHECADO_CHOICES = [
        ('S', 'Sim'), ('N', 'Não')]
    sensor = models.ForeignKey(SensorTemp, related_name='alertas', on_delete=models.CASCADE)
    datahora = models.DateTimeField()
    valor = models.IntegerField()
    checado = models.CharField(max_length=5, choices=CHECADO_CHOICES, default='N')
    descricao_defeito = models.CharField(max_length=200, blank=True, null=True)
    primeiro_aviso = models.BooleanField(default=False)

    def __str__(self):
        return self.sensor_alerta

    class Meta:
        get_latest_by = ['datahora']

