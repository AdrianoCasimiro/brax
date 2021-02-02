from django.views.generic import ListView
from .models import Gateway
from braxcloud.utils.getuser import getUser

class GatewayList(ListView):
    model = Gateway

    def get_queryset(self):
        cliente_id = getUser(self.request)
        return Gateway.objects.filter(cliente_id=cliente_id)


