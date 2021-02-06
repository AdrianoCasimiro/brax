from rest_framework import serializers
from .models import AlertaTemp

class AlertaTempSerializers(serializers.ModelSerializer):
    sensor = serializers.CharField()

    class Meta:
        model = AlertaTemp
        fields = '__all__'


