from django.contrib import admin
from .models import Item, Precio, Reserva, ReservaDetalle, Transferencia

admin.site.register(Item)
admin.site.register(Reserva)
admin.site.register(ReservaDetalle)
admin.site.register(Transferencia)
admin.site.register(Precio)
