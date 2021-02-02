from django.urls import path, include
from .views import GatewayList

app_name = 'gateway'

urlpatterns = [
    path('list/', GatewayList.as_view(), name='gateway_list'),
]