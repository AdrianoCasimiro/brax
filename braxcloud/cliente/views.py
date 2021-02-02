from django.views.generic import ListView
from .models import Planta
from braxcloud.utils.getuser import getUser


class PlantaList(ListView):
    model = Planta

    def get_queryset(self):
        cliente_id = getUser(self.request)
        return Planta.objects.filter(cliente_id=cliente_id)










