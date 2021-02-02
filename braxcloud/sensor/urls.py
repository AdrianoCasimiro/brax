from django.urls import path, include
from rest_framework import routers
from .api import SensorTempViewSet, SensorDpuViewSet


api_router = routers.DefaultRouter()
api_router.register(r'temp', SensorTempViewSet)
api_router.register(r'dpu', SensorDpuViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
]