from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..utils.getuser import getUser
from .models import AlertaTemp
from .serializers import AlertaTempSerializers

#Autenticação via login do usuário, retorna alerta relacionado a empresa no qual o usuário faz parte
class SensorTempViewSet(viewsets.ModelViewSet):
    serializer_class = AlertaTempSerializers
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cliente_id = getUser(self.request)
        return AlertaTemp.objects.filter(sensor__sensor__cliente=cliente_id)

