from django.db import models
from ..cliente.models import Cliente
from django.contrib.auth.models import User


class AcessoUsuario(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('usuario', 'cliente'),)

    def __str__(self):
        return self.usuario.username