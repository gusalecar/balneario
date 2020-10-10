from django.contrib import admin
from .models import Item, Reserva, ReservaDetalle, Transferencia

admin.site.register(Item)
admin.site.register(Reserva)
admin.site.register(ReservaDetalle)
admin.site.register(Transferencia)
