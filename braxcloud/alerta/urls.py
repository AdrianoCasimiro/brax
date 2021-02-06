from django.urls import path, include
from rest_framework import routers
from .api import SensorTempViewSet

app_name = 'alerta'

api_router = routers.DefaultRouter()
api_router.register(r'alertatemp', SensorTempViewSet, basename='AlertaTemp')


urlpatterns = [
    path("api/", include(api_router.urls)),

]