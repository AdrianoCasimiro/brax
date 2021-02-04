from rest_framework import viewsets
from .models import SensorTemp, SensorDPU
from .serializers import SensorTempSerializers, SensorDpuSerializers

class SensorTempViewSet(viewsets.ModelViewSet):
    serializer_class = SensorTempSerializers

    def get_queryset(self):
        return SensorTemp.objects.filter(sensor__cliente__nome_fantasia='Tigre')


class SensorDpuViewSet(viewsets.ModelViewSet):
    serializer_class = SensorDpuSerializers
    queryset = SensorDPU.objects.all()

