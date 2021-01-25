from django.apps import AppConfig


class SensorConfig(AppConfig):
    name = 'braxcloud.sensor'

    def ready(self):
        import braxcloud.sensor.signals