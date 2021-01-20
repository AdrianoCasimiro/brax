from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from django.http import HttpResponseNotFound, request
from django.views.generic import ListView, DetailView
from .models import Planta
from .. accounts.models import AcessoUsuario

def getUser(request):
    usuario_username = request.user.username
    cliente = AcessoUsuario.objects.filter(usuario__username=usuario_username).values('cliente_id')
    return (cliente[0]['cliente_id'])


class PlantaList(ListView):
    model = Planta

    def get_queryset(self):
        cliente_id = getUser(self.request)
        return Planta.objects.filter(cliente_id=cliente_id)










