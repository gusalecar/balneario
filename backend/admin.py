from django.contrib import admin
from .models import Item, Reserva, ReservaDetalle

admin.site.register(Item)
admin.site.register(Reserva)
admin.site.register(ReservaDetalle)
