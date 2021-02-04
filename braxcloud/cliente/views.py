from django.views.generic import ListView
from .models import Planta, Setor
from braxcloud.utils.getuser import getUser


class PlantaList(ListView):
    model = Planta

    def get_queryset(self):
        cliente_id = getUser(self.request)
        return Planta.objects.filter(cliente_id=cliente_id)

class SetorList(ListView):
    model = Planta

    def get_queryset(self):
        cliente_id = getUser(self.request)
        return Setor.objects.filter(cliente_id=cliente_id)










