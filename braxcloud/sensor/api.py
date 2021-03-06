from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import SensorTemp, SensorDPU
from .serializers import SensorTempSerializers, SensorDpuSerializers
from ..utils.getuser import getUser


class SensorTempViewSet(viewsets.ModelViewSet):
    serializer_class = SensorTempSerializers
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cliente_id = getUser(self.request)
        return SensorTemp.objects.filter(sensor__cliente=cliente_id)


class SensorDpuViewSet(viewsets.ModelViewSet):
    serializer_class = SensorDpuSerializers
    queryset = SensorDPU.objects.all()

