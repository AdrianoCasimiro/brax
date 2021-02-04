from django.conf.urls import url
from django.urls import path
from .views import PlantaList, SetorList

app_name = 'cliente'

urlpatterns = [
    path('planta/', PlantaList.as_view(), name='planta_list'),
    path('setor/', SetorList.as_view(), name='setor_list'),
]