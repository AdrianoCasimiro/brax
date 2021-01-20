from django.conf.urls import url
from django.urls import path
from .views import PlantaList

app_name = 'cliente'

urlpatterns = [
    path('planta/', PlantaList.as_view(), name='planta_list'),
]