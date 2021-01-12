from django.db import models
from braxcloud.cliente.models import Cliente, Planta

class Gateway(models.Model):
    codigo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo
