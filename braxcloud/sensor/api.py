from rest_framework import viewsets
from .models import SensorTemp, SensorDPU
from .serializers import SensorTempSerializers, SensorDpuSerializers

class SensorTempViewSet(viewsets.ModelViewSet):
    serializer_class = SensorTempSerializers
    queryset = SensorTemp.objects.all()


class SensorDpuViewSet(viewsets.ModelViewSet):
    serializer_class = SensorDpuSerializers
    queryset = SensorDPU.objects.all()

