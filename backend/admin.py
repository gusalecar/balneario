from django.contrib import admin
from .models import Reservable,Carpa,Sombrilla,Estacionamiento,Reserva,ReservaDetalle

admin.site.register(Reservable)

admin.site.register(Carpa)

admin.site.register(Sombrilla)

admin.site.register(Estacionamiento)

admin.site.register(Reserva)

admin.site.register(ReservaDetalle)
