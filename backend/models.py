from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Reservable(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Carpa(Reservable):
    pass
    def __str__(self):
        return str(self.id)


class Sombrilla(Reservable):
    pass

    def __str__(self):
        return str(self.id)


class Estacionamiento(Reservable):
    pass

    def __str__(self):
        return str(self.id)


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=timezone.now)
    ususario_reservo = models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.id)

class ReservaDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_ini = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField()
    item_reservado = models.ForeignKey(Reservable,on_delete=models.CASCADE,null=True,blank=True)
    item_reserva = models.ForeignKey(Reserva,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.id)
