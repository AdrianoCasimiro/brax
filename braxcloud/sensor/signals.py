from django.db.models.signals import post_save
from django.dispatch import receiver
from braxcloud.cliente.models import Equipamento
from braxcloud.sensor.models import SensorTemp
from braxcloud.alerta.models import AlertaTemp

@receiver(post_save, sender=SensorTemp)
def get_alerta(sender, instance, created, **kwargs):
    equipamento_alerta = getattr(instance.sensor.equipamento,'temperatura_max')

    if instance.t > equipamento_alerta:
        AlertaTemp.objects.create(
            sensor=instance, checado='N', valor=instance.t, datahora=instance.datahora)