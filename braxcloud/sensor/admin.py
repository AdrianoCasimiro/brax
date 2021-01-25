from django.contrib import admin
from .models import Sensor, SensorTemp, SensorDPU

admin.site.register(Sensor)
admin.site.register(SensorTemp)
admin.site.register(SensorDPU)
