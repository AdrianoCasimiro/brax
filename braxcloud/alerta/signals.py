from django.db.models import signals
from django.dispatch import receiver
from braxcloud.cliente.models import Equipamento
from braxcloud.sensor.models import SensorTemp
from .models import AlertaTemp

@receiver(signals.post_save, sender=SensorTemp)
def get_alerta(sender, instance, created, **kwargs):
    alerta_temp = Equipamento.objects.get(
            tag=instance.sensor.equipamento.tag, setor__planta=instance.sensor.planta)

    if instance.t > alerta_temp.temperatura_max:
        AlertaTemp.objects.create(
            sensor=instance, checado='N', valor=instance.t, datahora=instance.datahora)