from django.contrib import admin

from .models import Cliente, Planta, Equipamento, Setor

admin.site.register(Cliente)
admin.site.register(Planta)
admin.site.register(Equipamento)
admin.site.register(Setor)
