from rest_framework import serializers
from .models import SensorTemp, Sensor, SensorDPU

class SensorTempSerializers(serializers.ModelSerializer):
    sensor = serializers.CharField()

    class Meta:
        model = SensorTemp
        fields = ['sensor', 't', 'datahora']

    def create(self, validated_data):
        sensor = validated_data.pop('sensor')
        sensor_instance = Sensor.objects.get(codigo=sensor)
        historico_instance = SensorTemp.objects.create(
            **validated_data, sensor=sensor_instance)
        return historico_instance


class SensorDpuSerializers(serializers.ModelSerializer):
    sensor = serializers.CharField()

    class Meta:
        model = SensorDPU
        fields = ['sensor', 't', 'datahora', 'h', 'f60', 'mcnt']

    def create(self, validated_data):
        sensor = validated_data.pop('sensor')
        sensor_instance = Sensor.objects.get(codigo=sensor)
        historico_instance = SensorDPU.objects.create(
            **validated_data, sensor=sensor_instance)
        return historico_instance
